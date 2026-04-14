---
title: "TranTrac"
date: 2026-04-11
draft: false
weight: 2
short_desc: "Gestione spese familiari con bot Telegram e report PDF mensili"
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
    alt: "Interfaccia di inserimento transazione a confronto tra versione desktop e mobile, con form importo/data/descrizione e selezione categorie"
    title: "Design Responsive"
  - file: "2_other.jpg"
    alt: "Dialog di caricamento file CSV da banca e pagina report mensili su mobile con selezione mese/anno e download PDF"
    title: "Carica CSV e Report"
  - file: "3_telegram.jpg"
    alt: "Tre schermate del bot Telegram: benvenuto con comandi disponibili, flusso di inserimento spesa con selezione categoria, conferma salvataggio ed eliminazione transazione"
    title: "Bot Telegram"
  - file: "4_theme.jpg"
    alt: "Homepage dell'app in tema chiaro su desktop e tema scuro su mobile, con form di inserimento e categorie recenti"
    title: "Tema Chiaro/Scuro"

---

TranTrac è un'applicazione web per il tracciamento delle spese familiari, pensata per semplificare la gestione quotidiana del budget. Permette di registrare rapidamente ogni transazione con importo, data, descrizione e categoria, offrendo un'interfaccia essenziale e veloce da usare anche da mobile.

L'integrazione con Telegram è il cuore dell'app: tramite un bot dedicato è possibile aggiungere ed eliminare spese direttamente dalla chat, senza aprire il browser. Ideale per registrare le spese sul momento — al supermercato, al bar, in mobilità — con un semplice messaggio nel formato `IMPORTO/DESCRIZIONE`. Il bot riconosce automaticamente il ruolo dell'utente (admin o membro) e mostra i comandi disponibili di conseguenza.

Ogni mese è possibile caricare tramite il bot Telegram il CSV delle transazioni esportato dalla propria banca: TranTrac importa automaticamente i movimenti, abbinandoli alle categorie esistenti e riducendo l'inserimento manuale. L'accesso all'app è protetto da autenticazione: l'amministratore gestisce utenti e permessi, garantendo che ogni membro della famiglia acceda solo ai propri dati.

L'app genera report mensili in PDF il primo di ogni mese, scaricabili anche per periodi personalizzati. Le categorie sono organizzate in tab (recenti, più usate, tutte) per ridurre i click durante l'inserimento. L'interfaccia supporta keyboard shortcuts, tema chiaro/scuro e aggiornamenti dinamici via HTMX senza ricaricare la pagina.
