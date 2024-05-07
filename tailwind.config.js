/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "app/templates/**/*.html",
    "./templates/**/*.html",
    // "./static/src/**/*.js",
    // "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        "fdt-brown-dark": "#68340E",
        "fdt-brown-normal": "#8B4513",
        "fdt-brown-darker": "#311807",
        "fdt-grey-light-active": "#DEDEDE",
        "fdt-grey-normal": "#939393",
        "fdt-grey-light": "#F4F4F4",
        "fdt-grey-light-hover": "#EFEFEF",
        "fdt-grey-darker": "#333",
        "fdt-brown-light-active": "#DBC5B6",
        "fdt-brown-light-hover": "#EEE3DC",
        "fdt-grey-dark": "#6E6E6E",
        "fdt-brown-light": "#F3ECE7",
        "fdt-grey-dark-active": "#424242",
        "fdt-grey-background": "#F8F8F8"
      },


      animation: {
        'pulse-slow': 'pulse',
      }
      ,
      fontSize: {
        "sm": ["0.875rem", "16.8px"],
        "xl": ["1.125rem", "18px"],
        "3xl": ["1.75rem", "42px"],
        "2xl": ["1.5rem", "24px"]
      },

      fontFamily: {
        "playfair-display": ["Playfair Display", "serif"],
        "Roboto": "Roboto",
        "montserrat": ["Montserrat", "sans-serif"],
        "montserrat-alternates": ["Montserrat Alternates", "sans-serif"],
        "obitron": ["Orbitron", "sans-serif"]
      },

      borderWidth: {
        "1": "1px"
      },

      Keyframes: {
        rollout: {
          "0%": { transform: 'translateY(100%)' },
          "100%": { transform: 'translateY(0)' }
        },
        rollin: {
          "0%": { transform: 'translateY(0)' },
          "100%": { transform: 'translateY(100%)' }
        }
      },
      animation: {
        rollout: 'rollout 1s ease-in-out 1',
        rollin: 'rollin 1s ease-in-out 1'
      },
    },
    screens: {
      'xsm': '400px',
      // => @media (min-width: 580px) { ... }
      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      // 'ml': '968px',
      // => @media (min-width: 968px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
      lgscreen: { 'max': '968px' },
      midscreen: { 'max': '768px' },
      maxscreen: { 'max': '640px' },
      maxmobile: { 'max': '580px' },
      mobile: { 'max': '480px' },
      midmobile: { 'max': '380px' },
      minmobile: { 'max': '280px' }
    }
  },
  plugins: [
    require("flowbite/plugin")
  ],
}

