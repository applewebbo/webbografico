---
title: "Organizeit!"
date: 2026-04-14
draft: false
weight: 3
short_desc: "Collaborative trip planner with itinerary, transfers and weather"
live_url: "https://www.organizeit.webbografico.com"
source_code_url: "https://github.com/applewebbo/organize_it"
hero_image: "hero_organizeit.jpg"
technologies:
  - "Django"
  - "TailwindCSS"
  - "HTMX"
  - "PostgreSQL"
gallery:
  - file: "1_theme.jpg"
    alt: "Organizeit homepage in dark mode with two-tone layout and Create your first trip call-to-action"
    title: "Light/Dark Theme"
  - file: "2_documentation.jpg"
    alt: "How it works page showing 8 concept sections (Trips, Days, Stays, Experiences, Meals, Transfers, Collaboration, Sharing) alongside the English documentation page"
    title: "Documentation"
  - file: "3_trip_detail.jpg"
    alt: "Trip detail for Viaggio di Nozze 2026 in Rome with hero image, dates, collaborators and daily agenda showing events, weather and accommodations"
    title: "Trip Detail"
  - file: "4_add_transport.jpg"
    alt: "Add return transfer modal with transport type selection (Plane, Train, Car, Other), flight form with IATA airport search and outbound/return transfer summary"
    title: "Add Transfer"
  - file: "5_trip_list.jpg"
    alt: "Personal trips list with three cards (Rome holiday completed, Florence trip in progress, Easter holiday upcoming) with weather forecasts and quick actions"
    title: "Trips List"
  - file: "6_enrich_experience.jpg"
    alt: "Enrich feature on an event: comparison between basic card (Musei Capitolini, time) and enriched card with website, phone number and opening hours fetched automatically"
    title: "Enrich Experience"
  - file: "7_profile.jpg"
    alt: "Settings page with personal details, home address to pre-fill car transfers, avatar selection and travel preferences including currency and favourite trip"
    title: "Profile Settings"

---

Organizeit! is a web application for planning trips in a comprehensive and collaborative way. It lets you structure every trip by day, adding stays, experiences, meals and daily transfers to each one — all viewable on an interactive map with integrated weather forecasts.

At the core of the app is the daily itinerary: each day of the trip can contain categorised events (museums, restaurants, hotels, attractions) with times, addresses and notes. The Enrich feature automatically queries external sources to add the official website, phone number and opening hours to any event — reducing the time spent hunting for scattered information.

Main transfers (outbound and return) support flights, trains, cars and other transport: for flights, an airport search by name, city or IATA code is available. Car transfers are pre-filled with the home address set in the user profile.

Collaboration is built in: the trip plan can be shared with friends or family without requiring them to create an account. The shared trip is viewable in read-only mode by anyone with the link. The interface is available in Italian and English and supports light/dark theme.
