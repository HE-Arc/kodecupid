<template>
  <v-form id="signup-form" @submit.prevent="handleSubmit" @keyup.native.enter="valid && submit($event)">
    <v-container>
      <v-row>
        <v-col>
          <v-img cover class="rounded" src="/logo1024.png"></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>Nom d'utilisateur</v-label>
          <v-text-field v-model="form.username" label="Nom d'utilisateur" type="username" :rules="usernameRules" required  focused/>
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
          <v-btn type="submit" color="primary" form="signup-form">S'inscrire</v-btn>
        </v-col>
        <v-col class="d-flex">
          <v-label class="mr-4">Tu as déjà un compte ?</v-label>
          <v-btn flat class="text-primary" :to="{ name: 'signin' }">Se connecter</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
import { ref } from 'vue';
import {ApiClient} from '@/clients/apiClient.js';

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

  const response = await ApiClient.signupUser(jsonForm);

  if (response){
    router.push({name: 'signin', replace: true, force: true});
  }
  
};
</script>