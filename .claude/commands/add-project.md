# Skill: add-project

Analizza un sito web e crea automaticamente una pagina progetto per webbografico.com.

## Usage

```
/add-project <url>
```

**Esempio:**
```
/add-project https://trantrac.webbografico.com
```

## What This Skill Does

1. **Analisi del sito** — Visita l'URL con Playwright per esplorare le pagine principali e raccogliere informazioni su titolo, descrizione, tecnologie e funzionalità
2. **Generazione metadata** — Produce una bozza completa di frontmatter Hugo (title, short_desc, technologies, live_url, source_code_url) e un corpo descrittivo in italiano
3. **Revisione utente** — Mostra la bozza e chiede conferma o modifiche prima di procedere
4. **Screenshot** — Chiede all'utente una cartella con gli screenshot già preparati; li analizza per generare `alt` e `title` accurati; il primo file alfabetico è la hero image
5. **Creazione pagina** — Copia le immagini in `content/projects/<slug>/`, scrive `index.md`

## Step-by-step Instructions

### Step 1 — Leggi argomento e controlla prerequisiti

Estrai l'URL dall'argomento `$ARGUMENTS`. Se mancante, chiedi all'utente.

Verifica che la working directory sia `/Users/enricobonardi/CODING/WEBBO_PROJECTS/webbografico`.

### Step 2 — Analisi del sito con Playwright

Usa gli strumenti Playwright (`mcp__playwright__*`) per:

1. Naviga all'URL principale
2. Cattura uno snapshot testuale (`browser_snapshot`) per leggere contenuti, titoli, navigazione
3. Naviga a qualche pagina interna se disponibile (about, features, demo)
4. Annota: nome del progetto, scopo principale, tecnologie visibili (stack, badge, footer), URL sorgente (GitHub/Codeberg link se trovato)

Se Playwright non è disponibile, usa WebFetch sull'URL per estrarre il testo della pagina.

### Step 3 — Genera bozza metadata e descrizione

Produci:

```yaml
# FRONTMATTER PROPOSTO
title: "<nome progetto>"
date: "<data odierna YYYY-MM-DD>"
draft: false
weight: <suggerisci un numero intero, es. 5>
short_desc: "<una riga, max 80 char, in inglese>"
live_url: "<URL fornito>"
source_code_url: "<URL sorgente se trovato, altrimenti chiedi>"
hero_image: "hero_<slug>.jpg"
technologies:
  - "<tech1>"
  - "<tech2>"
  ...
```

E una **descrizione in italiano** (3–5 paragrafi) che spieghi:
- Cos'è il progetto e a chi si rivolge
- Funzionalità principali
- Scelte tecniche interessanti
- Eventuali sfide o aspetti notevoli

### Step 4 — Mostra bozza e chiedi conferma

Mostra all'utente il frontmatter e la descrizione proposti in un blocco markdown.

Chiedi:
- Conferma per procedere con questi dati
- Oppure indica cosa modificare (titolo, descrizione, tecnologie, source_code_url mancante, ecc.)

Applica le modifiche richieste e mostra di nuovo se necessario, prima di procedere.

### Step 5 — Chiedi la cartella degli screenshot

Dopo la conferma dei metadati, chiedi all'utente:

> Indica il percorso della cartella che contiene gli screenshot già preparati (es. `~/Desktop/trantrac-screenshots/`). Il primo file in ordine alfabetico sarà usato come **hero image**; gli altri come gallery. Usa nomi file descrittivi (es. `dashboard.jpg`, `reports.jpg`, `telegram.jpg`).

Attendi la risposta dell'utente con il percorso della cartella.

### Step 6 — Analizza le immagini e genera alt/title

Calcola lo `<slug>` dal titolo: lowercase, spazi → trattini, solo caratteri alfanumerici e trattini.

Per ogni file immagine nella cartella fornita (ordine alfabetico):

1. Leggila con il tool `Read` (supporta PNG/JPG)
2. Osserva visivamente cosa mostra: interfaccia, funzionalità, contesto
3. Genera:
   - `alt`: descrizione accessibile e dettagliata di cosa si vede nell'immagine (in italiano)
   - `title`: etichetta breve per la gallery (in italiano, 2–4 parole)

Il **primo file** (ordine alfabetico) è la **hero image**: rinominalo `hero_<slug>.jpg`.
Gli altri sono la gallery: mantieni il nome originale (senza estensione cambiata).

Mostra all'utente la lista con alt/title proposti e chiedi conferma o correzioni prima di copiare i file.

### Step 7 — Copia le immagini

Crea la cartella `content/projects/<slug>/` se non esiste.

Per ogni immagine:
- Hero: copia come `content/projects/<slug>/hero_<slug>.jpg`
- Gallery: copia mantenendo il nome originale in `content/projects/<slug>/`

Usa il tool Bash con `cp` per copiare i file.

### Step 8 — Crea index.md

Scrivi il file `content/projects/<slug>/index.md` con il frontmatter finale e la descrizione in italiano nel corpo.

Formato esatto:
```markdown
---
title: "..."
date: ...
draft: false
weight: ...
short_desc: "..."
live_url: "..."
source_code_url: "..."
hero_image: "hero_<slug>.jpg"
technologies:
  - "..."
gallery:
  - file: "..."
    alt: "..."
    title: "..."
---

<descrizione in italiano>
```

### Step 9 — Riepilogo finale

Mostra all'utente:
- Percorso della pagina creata
- Lista delle immagini copiate con i rispettivi alt/title
- Suggerimento di eseguire `just serve` per verificare il risultato
- Ricorda di usare `/commit` per committare le modifiche

## Notes

- L'utente gestisce formati e dimensioni degli screenshot — non imporre vincoli di aspect ratio
- La hero image è sempre il primo file in ordine alfabetico: suggerisci all'utente di nominarlo `01_...` o `hero_...` per controllare l'ordine
- `source_code_url` è opzionale ma raccomandata: cercala nel sito o chiedi all'utente
- Il `weight` controlla l'ordine nella lista progetti: valori più bassi appaiono prima
- Non inventare tecnologie: indicale solo se visibili nel sito o deducibili con certezza
- Se la cartella screenshot non esiste o è vuota, avvisa l'utente e attendi
