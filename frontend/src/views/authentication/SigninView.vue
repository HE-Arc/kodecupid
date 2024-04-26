<template>
  <v-form id="signin-form" @submit.prevent="handleSubmit" @keyup.native.enter="valid && submit($event)">
    <v-container>
      <v-row>
        <v-col>
          <v-img cover class="rounded" src="/logo1024.png"></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>Nom d'utilisateur</v-label>
          <v-text-field v-model="form.username" label="Nom d'utilisateur" type="username" :rules="usernameRules"
            required focused />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>Mot de passe</v-label>
          <v-text-field v-model="form.password" label="Mot de passe" type="password" :rules="passwordRules" required />
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-btn type="submit" color="primary" form="signin-form">Se connecter</v-btn>
        </v-col>
        <v-col class="d-flex">
          <v-label class="mr-4">Tu n'as pas de compte ?</v-label>
          <v-btn flat class="text-primary" :to="{ name: 'signup' }">S'inscrire</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
import axios from 'axios';

import { ref } from 'vue';
import { store } from '@/store';
import { setError } from '@/store';

import router from '@/router';

const uninitialized = ref(localStorage.getItem('uninitialized'));

const form = ref({
  username: '',
  password: ''
});

const usernameRules = [
  v => !!v || 'Le nom d\'utilisateur est obligatoire',
  v => v.length >= 3 || 'Le nom d\'utilisateur doit contenir min. 3 caractères'
];
const passwordRules = [
  v => !!v || 'Le mot de passe est obligatoire',
  v => v.length >= 6 || 'Le mot de passe doit contenir min. 6 caractères'
];


const handleSubmit = async () => {
  const jsonForm = JSON.stringify(form.value);

  axios.post(store.routes['USER_SIGNIN'], jsonForm, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `anonymous`
    }
  })
    .catch((error) => {
      console.error("Signin error", error.response.data);
      setError(error.response.data,'error');
      return error
    })
    .then(response => {
      if (response.status === 200) {
        localStorage.setItem('accessToken', response.data.access);
        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;
        localStorage.setItem('refreshToken', response.data.refresh);
        if (uninitialized.value) {
          router.push({ name: 'account-edit', replace: true, force: true });
        }
        else {
          router.push({ name: 'account-show', replace: true, force: true });
        }

      }
    });
};

</script>