/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        flame: '#FF4D6D',
        gold: '#FFD166',
        teal: '#06D6A0',
        violet: '#9B5DE5',
        muted: '#7A7A9A',
      }
    }
  },
  plugins: []
}