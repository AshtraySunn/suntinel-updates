#!/usr/bin/env python3
"""Contrôles simples de la vitrine publique. Aucun paquet externe nécessaire."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_STATUSES = {"done", "working", "planned"}
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


class LinksParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.links: list[str] = []
        self.one_h1 = 0
        self.lang_fr = False
        self.has_forms = False
        self.external_scripts = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        args = dict(attrs)
        if args.get("id"):
            self.ids.append(args["id"])
        if tag == "html" and args.get("lang") == "fr":
            self.lang_fr = True
        if tag == "h1":
            self.one_h1 += 1
        if tag == "form":
            self.has_forms = True
        if tag == "script" and (args.get("src") or "").startswith(("http:", "https:")):
            self.external_scripts = True
        for key in ("href", "src"):
            if args.get(key):
                self.links.append(args[key])


def check_local_link(origin: str, destination: str, ids: set[str]) -> None:
    if destination.startswith(("#", "https:", "http:", "mailto:", "tel:", "data:")):
        if destination.startswith("#") and origin == "index.html":
            if unquote(destination[1:]) not in ids:
                fail(f"{origin}: ancre introuvable : {destination}")
        return
    clean = unquote(destination.split("#", 1)[0].split("?", 1)[0])
    if not clean:
        return
    target = (ROOT / origin).parent / clean
    if not target.is_file():
        fail(f"{origin}: fichier cible introuvable : {destination}")


def main() -> int:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    js = (ROOT / "script.js").read_text(encoding="utf-8")
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    data = json.loads((ROOT / "data/progress.json").read_text(encoding="utf-8"))

    parser = LinksParser()
    parser.feed(html)
    ids = set(parser.ids)

    if len(ids) != len(parser.ids):
        fail("index.html: plusieurs éléments portent le même identifiant")
    if not parser.lang_fr:
        fail("index.html: langue française absente")
    if parser.one_h1 != 1:
        fail("index.html: exactement un titre principal h1 est attendu")
    if parser.has_forms:
        fail("index.html: aucun formulaire public ne doit être proposé")
    if parser.external_scripts:
        fail("index.html: script hébergé par un tiers non prévu")
    for url in parser.links:
        check_local_link("index.html", url, ids)

    for md in ROOT.glob("*.md"):
        content = md.read_text(encoding="utf-8")
        for url in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            check_local_link(md.name, url, ids)

    required_ids = {
        "accueil", "contenu", "recherches", "outils", "securite",
        "avancement", "journal", "questions", "jalons", "actualites",
        "date-maj", "annee",
    }
    if not required_ids.issubset(ids):
        fail("index.html: certaines sections ou zones dynamiques manquent")
    if not all(token in js for token in ("textContent", "replaceChildren", "data/progress.json")):
        fail("script.js: la génération de contenu public a changé")

    milestones = data.get("milestones")
    updates = data.get("updates")
    if not isinstance(milestones, list) or not milestones:
        fail("data/progress.json: jalons manquants")
    else:
        for item in milestones:
            if item.get("status") not in ALLOWED_STATUSES:
                fail("data/progress.json: statut non autorisé")
            for key in ("code", "title", "description"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    fail(f"data/progress.json: {key} vide")
    if not isinstance(updates, list) or not updates:
        fail("data/progress.json: actualités manquantes")
    else:
        for item in updates:
            for key in ("date_iso", "date_label", "title", "summary"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    fail(f"data/progress.json: {key} manquant")

    public_text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix in {".html", ".css", ".js", ".md", ".json"}
    )
    forbidden = {
        "chemin privé": r"/home/ashtr/",
        "clé privée": r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY",
        "token GitHub": r"github_pat_|ghp_[A-Za-z0-9]{20,}",
        "fichier de sécurité interne": r"security_generation\.json",
    }
    for label, pattern in forbidden.items():
        if re.search(pattern, public_text, flags=re.I):
            fail(f"Information sensible potentielle : {label}")

    if "SunTinel" not in html or "Aucune recherche de personne" not in html:
        fail("index.html: présentation ou avertissement essentiel absent")
    if not css.strip():
        fail("styles.css: fichier vide")

    if ERRORS:
        for error in ERRORS:
            print("ERREUR :", error)
        return 1
    print("OK : liens locaux, navigation, contenu, statuts et garde-fous publics vérifiés.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
