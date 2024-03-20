import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { aliases, mdi } from 'vuetify/iconsets/mdi';

const app = createApp(App);

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },

  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          'like': '#2cc72c',
          'dislike': '#902727',
        },
      },
      dark: {
        colors: {
          'like': '#2cc72c',
          'dislike': '#902727',
        },
      },
    },
  },
});

app.use(vuetify);
app.use(router);

app.mount('#app');