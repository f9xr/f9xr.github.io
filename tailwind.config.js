/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",
    "!./node_modules/**",
    "!./.git/**"
  ],
  theme: {
    extend: {
      colors: {
        'carbon-black': '#212529',
        'bright-snow': '#f8f9fa',
        'platinum': '#e9ecef',
        'iron-grey': '#495057',
        'gunmetal': '#343a40',
        'accent-blue': '#3b82f6'
      },
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'sans-serif'],
      },
    }
  },
  plugins: []
}
