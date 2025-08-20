/** @type {import('tailwindcss').Config} */

export default {
    content: [
      "./src/**/*.{js,jsx,ts,tsx}", // adjust as needed
    ],
    theme: {
      extend: {
        colors: {
          parchment: "#f9f6f1",
          wood: "#2d221b",
          gold: "#bfa05a",
          bronze: "#836945",
          textmain: "#221a13",
          accent: "#5e4637",
          danger: "#ae3b3b",
          success: "#4c9448",
          info: "#5e8fa3",
        },
        fontFamily: {
          heading: ["Cinzel", "serif"],
          body: ["Merriweather", "serif"],
        },
        dropShadow: {
          'fantasy': '0 4px 12px rgba(94,70,55,0.25)',
        },
        borderRadius: {
          'rpg': '12px',
        },
        backgroundImage: {
          'parchment': "url('/images/parchment-bg.png')", // Add this texture image!
        },
      },
    },
    plugins: {

      tailwindcss: {},
  
      autoprefixer: {},
  
    },
  }
  // PostCSS configuration
