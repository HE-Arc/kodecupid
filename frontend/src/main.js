import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { aliases, mdi } from 'vuetify/iconsets/mdi';

import axiosPluging from '@/plugins/axiosPlugin';

// import axios from 'axios';
// axios.defaults.baseURL = import.meta.env.VITE_API_URL;

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

app.use(axiosPluging);
app.use(vuetify);
app.use(router);
app.mount('#app');