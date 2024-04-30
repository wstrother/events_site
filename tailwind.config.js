/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

// ./tailwind -i ./polls/static/polls/input.css -o ./polls/static/polls/css/style.css --watch


