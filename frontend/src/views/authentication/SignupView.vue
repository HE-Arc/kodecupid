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
          <v-label>username*</v-label>
          <v-text-field v-model="form.username" label="username" type="username" :rules="usernameRules" required  focused/>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>password*</v-label>
          <v-text-field v-model="form.password" label="Password" type="password" :rules="passwordRules" required />
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-btn type="submit" color="primary" form="signup-form">Register</v-btn>
        </v-col>
        <v-col class="d-flex">
          <v-label class="mr-4">Already have an account?</v-label>
          <v-btn flat class="text-primary" :to="{ name: 'signin' }">Singnin</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
import { ref } from 'vue';
import { store } from '@/store';
import axios from 'axios';
import router from '@/router';

const form = ref({
  username: '',
  password: ''
});

const usernameRules = [
  v => !!v || 'Username is required',
  v => v.length >= 3 || 'Username must be at least 3 characters'
];
const passwordRules = [
  v => !!v || 'Password is required',
  v => v.length >= 6 || 'Password must be at least 6 characters'
];


const handleSubmit = async () => {
  const jsonForm = JSON.stringify(form.value);
  axios.post(store.routes['USER_SIGNUP'], jsonForm, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': "anonymous"
    }}
    , {  })
    .catch((error) => {
      console.error(error.response.data);
      return error
    })
    .then(response => {
      console.log(response);
      if (response.status === 201) {
        localStorage.setItem('uninitialized', true);
        router.push({ name: 'signin', replace: true, force: true});
      }
    });
};
</script>