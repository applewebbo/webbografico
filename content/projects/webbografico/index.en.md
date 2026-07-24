---
title: "WEBBOgrafico"
date: 2024-10-26
draft: false
weight: 1
short_desc: "This portfolio site built with Hugo and TailwindCSS"
live_url: "https://webbografico.com"
source_code_url: "https://github.com/applewebbo/webbografico"
hero_image: "hero_webbografico.jpg"
technologies:
  - "Hugo"
  - "TailwindCSS"
  - "DaisyUI"
  - "AlpineJS"
gallery:
  - file: "themes.jpg"
    alt: "Site with light and dark theme"
    title: "Light/Dark Theme"
  - file: "responsive.jpg"
    alt: "Site at various window widths"
    title: "Responsive Design"
  - file: "navbar.jpg"
    alt: "Site navigation bar"
    title: "Navigation Bar"
  - file: "detail.jpg"
    alt: "Project detail page"
    title: "Project Page"
  - file: "contact.jpg"
    alt: "Contact page"
    title: "Contact Form"

---

WEBBOgrafico is my personal portfolio site, built to collect and showcase the projects I develop in my spare time. It is the place where I show what I can do, how I do it, and which technologies I use.

Each project has a dedicated page with description, image gallery, link to the source code and to the live site. The site supports light/dark theme, is fully responsive and includes an about page.

The site is built with Hugo for static content generation, Tailwind CSS v4 + DaisyUI v5 for styling and AlpineJS for interactive components such as the modal gallery. Deployment is handled by Coolify with a multi-stage Dockerfile (Hugo build → Nginx serve).
