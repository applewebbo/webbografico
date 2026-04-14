---
# webbografico-cl61
title: Navigable gallery modal with AlpineJS
status: completed
type: feature
priority: normal
created_at: 2026-04-14T13:03:38Z
updated_at: 2026-04-14T13:05:32Z
---

Replace current single-image modal with a navigable fullscreen lightbox using AlpineJS. Support prev/next navigation, keyboard arrows, swipe on mobile, and work on all screen sizes. Closes issue #50.

## Summary of Changes\n\n- Rewrote `gallery-modal.html`: navigable lightbox with prev/next buttons, keyboard arrows, swipe touch, dot indicators, works on all screen sizes\n- Updated `single.html`: gallery thumbnails dispatch `gallery-open` event with index instead of old `img-modal`\n- Removed mobile restriction (was disabled under 768px)\n- Recompiled Tailwind CSS
