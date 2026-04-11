---
title: "WEBBOgrafico"
date: 2024-10-26
draft: false
weight: 1
short_desc: "This portfolio site built with Hugo and tailwindcss"
live_url: "https://webbografico.com"
source_code_url: "https://codeberg.org/webbografico/webbografico"
hero_image: "hero_webbografico.jpg"
technologies:
  - "Hugo"
  - "TailwindCSS"
  - "DaisyUI"
  - "AlpineJS"
gallery:
  - file: "themes.jpg"
    alt: "immagine del sito con tema chiaro/scuro"
    title: "Tema Chiaro/Scuro"
  - file: "responsive.jpg"
    alt: "Sito con varie larghezze della finestra"
    title: "Sito Responsive"
  - file: "navbar.jpg"
    alt: "Barra di navigazione del sito"
    title: "Barra di Navigazione"
  - file: "detail.jpg"
    alt: "Pagina di dettaglio di un progetto"
    title: "Pagina del Progetto"
  - file: "contact.jpg"
    alt: "Pagina di contatto"
    title: "Modulo di Contatto"

---

WEBBOgrafico è il mio sito portfolio personale, nato per raccogliere e presentare i progetti che sviluppo nel tempo libero. È il posto dove mostro cosa so fare, come lo faccio e con quali tecnologie.

Ogni progetto ha una pagina dedicata con descrizione, galleria immagini, link al codice sorgente e al sito live. Il sito supporta tema chiaro/scuro, è completamente responsive e include una pagina contatti.

Il sito è costruito con Hugo per la generazione statica dei contenuti, Tailwind CSS v4 + DaisyUI v5 per lo stile e AlpineJS per i componenti interattivi come la galleria modale. Il deploy avviene tramite Coolify con un Dockerfile multi-stage (build Hugo → serve Nginx).
