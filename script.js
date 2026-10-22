'use strict';

const $ = (selector) => document.querySelector(selector);
const make = (tag, className, content) => {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (content !== undefined) node.textContent = content;
  return node;
};

const statusLabels = { done: 'Jalon validé*', working: 'En cours', planned: 'À venir' };

async function loadProgress() {
  const [roadmap, updates] = [$('#roadmap'), $('#updates')];
  try {
    const response = await fetch('data/progress.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error('HTTP ' + response.status);
    const data = await response.json();
    if (!Array.isArray(data.milestones) || !Array.isArray(data.updates)) throw new Error('Données manquantes');
    $('#updated-date').textContent = String(data.updated_label || '22 octobre 2026');
    roadmap.replaceChildren();
    for (const item of data.milestones) {
      const state = Object.hasOwn(statusLabels, item.status) ? item.status : 'planned';
      const card = make('article', 'roadmap-card');
      const head = make('div', 'roadmap-head');
      head.append(make('span', 'roadmap-id', String(item.code)), make('span', 'status ' + state, statusLabels[state]));
      card.append(head, make('h3', '', String(item.title)), make('p', '', String(item.description)));
      roadmap.append(card);
    }
    updates.replaceChildren();
    for (const item of data.updates) {
      const row = make('article', 'update-row');
      const date = make('time', 'update-date', String(item.date_label));
      if (item.date_iso) date.dateTime = String(item.date_iso);
      row.append(date, make('h3', '', String(item.title)), make('p', '', String(item.summary)));
      updates.append(row);
    }
  } catch (error) {
    const message = 'Les mises à jour ne sont pas accessibles actuellement. Consultez le journal Markdown du dépôt.';
    roadmap.replaceChildren(make('div', 'load-error', message));
    updates.replaceChildren(make('div', 'load-error', message));
  }
}

$('#year').textContent = String(new Date().getFullYear());
loadProgress();
