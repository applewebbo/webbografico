---
title: "Organizeit!"
date: 2026-04-14
draft: false
weight: 3
short_desc: "Pianifica i tuoi viaggi in modo collaborativo con itinerario e meteo"
live_url: "https://www.organizeit.webbografico.com"
source_code_url: "https://codeberg.org/webbografico/organize_it"
hero_image: "hero_organizeit.jpg"
technologies:
  - "Django"
  - "TailwindCSS"
  - "HTMX"
  - "PostgreSQL"
gallery:
  - file: "1_theme.jpg"
    alt: "Homepage di Organizeit in tema scuro con layout a due colori e call-to-action Crea il tuo primo viaggio"
    title: "Tema Chiaro/Scuro"
  - file: "2_documentation.jpg"
    alt: "Pagina Come funziona con le 8 sezioni concettuali (Viaggi, Giorni, Soggiorni, Esperienze, Pasti, Trasferimenti, Collaborazione, Condivisione) e documentazione in inglese"
    title: "Documentazione"
  - file: "3_trip_detail.jpg"
    alt: "Dettaglio del Viaggio di Nozze 2026 a Roma con immagine hero, date, collaboratori e agenda giornaliera con eventi, meteo e soggiorni"
    title: "Dettaglio Viaggio"
  - file: "4_add_transport.jpg"
    alt: "Modale di aggiunta trasferimento con selezione mezzo (Aeroplano, Treno, Automobile, Altro), form volo con ricerca aeroporto per codice IATA e riepilogo trasferimenti andata/ritorno"
    title: "Aggiungi Trasferimento"
  - file: "5_trip_list.jpg"
    alt: "Lista dei viaggi personali con tre card (Vacanze in Roma completata, Gita a Firenze in corso, Vacanze di Pasqua imminente), previsioni meteo e azioni rapide"
    title: "Lista Viaggi"
  - file: "6_enrich_experience.jpg"
    alt: "Funzione Arricchisci su un evento: confronto tra scheda base (Musei Capitolini, orario) e scheda arricchita con sito web, telefono e orari di apertura recuperati automaticamente"
    title: "Arricchisci Esperienza"
  - file: "7_profile.jpg"
    alt: "Pagina impostazioni con dati personali, indirizzo di casa per precompilare i trasferimenti in auto, selezione avatar e preferenze di viaggio con valuta e viaggio preferito"
    title: "Impostazioni Profilo"

---

Organizeit! è un'applicazione web per pianificare viaggi in modo completo e collaborativo. Permette di strutturare ogni viaggio per giorni, aggiungendo per ciascuno soggiorni, esperienze, pasti e trasferimenti giornalieri, il tutto visualizzabile su mappa interattiva con previsioni meteo integrate.

Il cuore dell'app è l'itinerario giornaliero: ogni giorno del viaggio può contenere eventi categorizzati (musei, ristoranti, hotel, attrazioni) con orari, indirizzi e note. La funzione "Arricchisci" interroga automaticamente fonti esterne per aggiungere agli eventi sito ufficiale, numero di telefono e orari di apertura — riducendo il tempo speso a cercare informazioni sparse.

I trasferimenti principali (andata e ritorno) supportano voli, treni, automobili e altri mezzi: per i voli è disponibile una ricerca aeroporti per nome, città o codice IATA. I trasferimenti in automobile si precompilano con l'indirizzo di casa impostato nel profilo utente.

La collaborazione è nativa: è possibile condividere il piano di viaggio con amici o familiari senza richiedere loro un account. Il viaggio condiviso è visualizzabile in sola lettura da chiunque abbia il link. L'interfaccia è disponibile in italiano e inglese e supporta tema chiaro/scuro.
