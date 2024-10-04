/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");

module.exports = {
  content: [
    "./templates/**/*.html",
    "**/templates/**/*.html",
    // https://noumenal.es/notes/tailwind/django-integration/ but breaks Tailwind Intellisense in VSCode so added manually
    ".venv/lib/python3.12/site-packages/crispy_tailwind/templates/**/*.html",],
  theme: {
    extend: {},
  },
  darkMode: ['selector', '[data-theme="dracula"]'],
  theme: {
    container: {
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
  },
  daisyui: {
    themes: ["light", "dracula"],
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    require('daisyui'),
    plugin(function ({ addVariant }) {
      addVariant("htmx-settling", ["&.htmx-settling", ".htmx-settling &"]);
      addVariant("htmx-request", ["&.htmx-request", ".htmx-request &"]);
      addVariant("htmx-swapping", ["&.htmx-swapping", ".htmx-swapping &"]);
      addVariant("htmx-added", ["&.htmx-added", ".htmx-added &"]);
    }),
  ],
};
