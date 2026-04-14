---
title: "TranTrac"
date: 2026-04-11
draft: false
weight: 2
short_desc: "Family expense tracker with Telegram integration and monthly PDF reports"
live_url: "https://trantrac.webbografico.com"
source_code_url: "https://codeberg.org/webbografico/trantrac"
hero_image: "hero_trantrac.jpg"
technologies:
  - "Django"
  - "TailwindCSS"
  - "HTMX"
  - "PostgreSQL"
  - "Telegram Bot"
gallery:
  - file: "1_responsive.jpg"
    alt: "Transaction entry interface compared between desktop and mobile versions, with amount/date/description form and category selection"
    title: "Responsive Design"
  - file: "2_other.jpg"
    alt: "CSV file upload dialog from bank and monthly reports page on mobile with month/year selection and PDF download"
    title: "CSV Import & Reports"
  - file: "3_telegram.jpg"
    alt: "Three Telegram bot screens: welcome with available commands, expense entry flow with category selection, save confirmation and transaction deletion"
    title: "Telegram Bot"
  - file: "4_theme.jpg"
    alt: "App homepage in light theme on desktop and dark theme on mobile, with entry form and recent categories"
    title: "Light/Dark Theme"

---

TranTrac is a web application for tracking family expenses, designed to simplify daily budget management. It allows you to quickly record each transaction with amount, date, description and category, offering an essential and fast interface usable on mobile too.

The Telegram integration is the heart of the app: through a dedicated bot you can add and delete expenses directly from the chat, without opening a browser. Ideal for recording expenses on the go — at the supermarket, café, or while travelling — with a simple message in the format `AMOUNT/DESCRIPTION`. The bot automatically recognises the user's role (admin or member) and shows the available commands accordingly.

Each month you can upload via the Telegram bot the CSV of transactions exported from your bank: TranTrac automatically imports the movements, matching them to existing categories and reducing manual entry. Access to the app is protected by authentication: the administrator manages users and permissions, ensuring each family member only accesses their own data.

The app generates monthly PDF reports on the first of each month, also downloadable for custom periods. Categories are organised in tabs (recent, most used, all) to reduce clicks during entry. The interface supports keyboard shortcuts, light/dark theme and dynamic updates via HTMX without page reloads.
