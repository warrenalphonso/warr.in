/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./theme/templates/**/*.html",
        "./content/**/*.html",
        // Ignore uploads directory
        "!./content/uploads/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
