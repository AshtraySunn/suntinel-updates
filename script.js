'use strict';

// Contenu public : texte uniquement. Aucune donnée personnelle ou recherche.
const select = (query) => document.querySelector(query);
const element = (tag, className, content) => {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (content !== undefined) node.textContent = String(content);
  return node;
};

const statusLabels = {
  done: 'Évalué avec réserves',
  working: 'En cours',
  planned: 'Prévu'
};

async function loadNews() {
  const milestones = select('#jalons');
  const updates = select('#actualites');

  try {
    const response = await fetch('data/progress.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error('Progress data unavailable');
    const data = await response.json();

    if (!Array.isArray(data.milestones) || !Array.isArray(data.updates)) {
      throw new Error('Invalid progress data');
    }
    select('#date-maj').textContent = String(data.updated_label || '24 octobre 2026');

    const milestoneNodes = data.milestones.map(item => {
      const state = Object.hasOwn(statusLabels, item.status) ? item.status : 'planned';
      const card = element('article', 'roadmap-card');
      const top = element('div', 'roadmap-top');
      top.append(
        element('span', 'roadmap-code', item.code),
        element('span', 'roadmap-status ' + state, statusLabels[state])
      );
      card.append(top, element('h3', '', item.title), element('p', '', item.description));
      return card;
    });

    const updateNodes = data.updates.slice(0, 5).map(item => {
      const row = element('article', 'update-row');
      const date = element('time', '', item.date_label);
      if (item.date_iso) date.dateTime = String(item.date_iso);
      row.append(date, element('h3', '', item.title), element('p', '', item.summary));
      return row;
    });

    milestones.replaceChildren(...milestoneNodes);
    updates.replaceChildren(...updateNodes);
  } catch (_error) {
    // Les liens HTML vers ROADMAP.md et CHANGELOG.md restent utilisables sans JS.
  }
}

select('#annee').textContent = String(new Date().getFullYear());
loadNews();
