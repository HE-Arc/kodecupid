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
    defaultTheme: 'dark',
    themes: {
      light: {
        colors: {
          'like': '#2cc72ca2',
          'dislike': '#902727ad',
        },
      },
      dark: {
        colors: {
          'like': '#2cc72c5d',
          'dislike': '#9027275d',
        },
      },
    },
  },
});

app.use(axiosPluging);
app.use(vuetify);
app.use(router);
app.mount('#app');