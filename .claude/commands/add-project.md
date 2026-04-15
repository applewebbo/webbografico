# Skill: add-project

Analizza un sito web e crea automaticamente una pagina progetto per webbografico.com in entrambe le lingue (IT e EN).

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
2. **Generazione metadata** — Produce una bozza completa di frontmatter Hugo e testi descrittivi sia in **italiano** che in **inglese**
3. **Revisione utente** — Mostra la bozza e chiede conferma o modifiche prima di procedere
4. **Screenshot** — Chiede all'utente una cartella con gli screenshot già preparati; li analizza per generare `alt` e `title` accurati in entrambe le lingue
5. **Creazione pagine** — Copia le immagini in `static/img/projects/<slug>/`, scrive `index.it.md` e `index.en.md` in `content/projects/<slug>/`

## Site Structure

Il sito usa Hugo con supporto multilingua IT/EN:

- **Contenuto**: `content/projects/<slug>/index.it.md` e `index.en.md`
- **Immagini**: `static/img/projects/<slug>/` (condivise tra le due lingue, NON in content/)
- **URL IT**: `/it/projects/<slug>/`
- **URL EN**: `/en/projects/<slug>/`
- **i18n UI**: stringhe dell'interfaccia in `i18n/it.yaml` e `i18n/en.yaml` (non toccare per i contenuti dei progetti)

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

### Step 3 — Genera bozza metadata e descrizioni

Produci il frontmatter (condiviso tra le due lingue) e due versioni del testo descrittivo:

```yaml
# FRONTMATTER (uguale per IT e EN, solo short_desc cambia)
title: "<nome progetto>"
date: "<data odierna YYYY-MM-DD>"
draft: false
weight: <suggerisci un numero intero, es. 5>
live_url: "<URL fornito>"
source_code_url: "<URL sorgente se trovato, altrimenti chiedi>"
hero_image: "hero_<slug>.jpg"
technologies:
  - "<tech1>"
  - "<tech2>"
  ...

# short_desc IT: una riga, max 80 char, in italiano
# short_desc EN: una riga, max 80 char, in inglese
```

E due versioni della **descrizione** (3–5 paragrafi ciascuna):
- **IT**: in italiano, spiega cos'è, funzionalità principali, scelte tecniche
- **EN**: in inglese, stesso contenuto tradotto

### Step 4 — Mostra bozza e chiedi conferma

Mostra all'utente frontmatter, descrizione IT e descrizione EN in blocchi markdown separati.

Chiedi:
- Conferma per procedere
- Oppure indica cosa modificare

Applica le modifiche richieste prima di procedere.

### Step 5 — Chiedi la cartella degli screenshot

Dopo la conferma dei metadati, chiedi all'utente:

> Indica il percorso della cartella che contiene gli screenshot già preparati (es. `~/Desktop/trantrac-screenshots/`). Il primo file in ordine alfabetico sarà usato come **hero image**; gli altri come gallery. Usa nomi file descrittivi (es. `dashboard.jpg`, `reports.jpg`).

Se le immagini sono già in `content/projects/<slug>/` (caricate manualmente), usale direttamente saltando la copia.

Attendi la risposta dell'utente con il percorso della cartella.

### Step 6 — Analizza le immagini e genera alt/title

Calcola lo `<slug>` dal titolo: lowercase, spazi → trattini, solo caratteri alfanumerici e trattini.

Per ogni file immagine nella cartella fornita (ordine alfabetico):

1. Leggila con il tool `Read` (supporta PNG/JPG)
2. Osserva visivamente cosa mostra: interfaccia, funzionalità, contesto
3. Genera per ciascuna:
   - `alt` IT: descrizione accessibile e dettagliata in italiano
   - `title` IT: etichetta breve per la gallery (2–4 parole, italiano)
   - `alt` EN: stessa descrizione in inglese
   - `title` EN: stessa etichetta in inglese

Il **primo file** (ordine alfabetico) è la **hero image**: rinominalo `hero_<slug>.jpg`.

Mostra all'utente la tabella con alt/title IT e EN proposti e chiedi conferma prima di procedere.

### Step 7 — Copia le immagini in static/

**Le immagini vanno in `static/img/projects/<slug>/`**, NON in `content/projects/<slug>/`.

Crea la cartella `static/img/projects/<slug>/` se non esiste.

Per ogni immagine:
- Hero: copia come `static/img/projects/<slug>/hero_<slug>.jpg`
- Gallery: copia mantenendo il nome originale in `static/img/projects/<slug>/`

Se le immagini erano già in `content/projects/<slug>/`, copiale in static e non rimuoverle dal content (le immagini in content non vengono usate ma non danneggiano).

Usa il tool Bash con `cp` per copiare i file.

### Step 8 — Crea index.it.md e index.en.md

Crea la cartella `content/projects/<slug>/` se non esiste.

Scrivi **due file separati**:

**`content/projects/<slug>/index.it.md`** — versione italiana:
```markdown
---
title: "..."
date: ...
draft: false
weight: ...
short_desc: "... (in italiano)"
live_url: "..."
source_code_url: "..."
hero_image: "hero_<slug>.jpg"
technologies:
  - "..."
gallery:
  - file: "..."
    alt: "... (in italiano)"
    title: "... (in italiano)"
---

<descrizione in italiano>
```

**`content/projects/<slug>/index.en.md`** — versione inglese:
```markdown
---
title: "..."
date: ...
draft: false
weight: ...
short_desc: "... (in inglese)"
live_url: "..."
source_code_url: "..."
hero_image: "hero_<slug>.jpg"
technologies:
  - "..."
gallery:
  - file: "..."
    alt: "... (in inglese)"
    title: "... (in inglese)"
---

<descrizione in inglese>
```

Nota: `title`, `technologies`, `live_url`, `source_code_url`, `hero_image` e i `file` della gallery sono identici in entrambi i file. Cambiano: `short_desc`, `alt`, `title` della gallery e il corpo della descrizione.

### Step 9 — Riepilogo finale

Mostra all'utente:
- Percorsi dei file creati (`index.it.md`, `index.en.md`, immagini in `static/`)
- Lista delle immagini con alt/title IT e EN
- Suggerimento di eseguire `just serve` per verificare il risultato su `/it/projects/<slug>/` e `/en/projects/<slug>/`
- Ricorda di usare `/commit` per committare le modifiche

## Notes

- **Immagini sempre in `static/img/projects/<slug>/`** — mai in `content/` per i progetti
- La hero image è sempre il primo file in ordine alfabetico: suggerisci di nominarla `hero_...` o `01_...`
- `source_code_url` è opzionale ma raccomandata: cercala nel sito o chiedi all'utente
- Il `weight` controlla l'ordine nella lista progetti: valori più bassi appaiono prima
- Non inventare tecnologie: indicale solo se visibili nel sito o deducibili con certezza
- `title` del progetto è invariato tra IT e EN (nome proprio dell'app)
- Se la cartella screenshot non esiste o è vuota, avvisa l'utente e attendi
