/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.{html,js,jsx}',
        '../../users/templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.{html,js,jsx}',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.{html,js,jsx}',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'

    ],
    theme: {
        extend: {
            colors : {
                transparent: 'transparent',
                current: 'currentColor',
                'primary': {
                    'light': '#38B0B5',
                    'normal': '#1B7F83',
                    'dark': '#10585B',
                },
                'darker': {
                    800: '#2D2D2D',
                    900: '#414141',
                },
                'success': {
                    200: '#00803D',
                    100: '#DCFCE7',
                },
                'error': {
                    200: '#973333',
                    100: '#FFB4B4',
                },
                'warning': {
                    200: '#755F30',
                    100: '#F5D480',
                },
            },
            fontFamily: {
                inter: ['Inter', 'sans-serif'],
                pro: ['Source Sans Pro', 'serif'],
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
