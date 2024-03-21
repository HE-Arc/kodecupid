<template>
  <v-form @submit.prevent="handleSubmit" >
    <v-container>
      <v-row>
        <v-col>
          <v-img cover class="rounded" src="/logo1024.png"></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>username*</v-label>
          <v-text-field v-model="form.username" label="username" type="username" :rules="usernameRules" required />
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
          <v-btn type="submit" color="primary">signin</v-btn>
        </v-col>
        <v-col class="d-flex">
          <v-label class="mr-4">Need an account?</v-label>
          <v-btn flat class="text-primary" :to="{ name: 'signup' }">Singnup</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
import { getCurrentInstance } from 'vue';
const { appContext } = getCurrentInstance();
const axios = appContext.config.globalProperties.$axios;

import { ref } from 'vue';
import { store } from '@/store';

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
  {
    const jsonForm = JSON.stringify(form.value);
    const response = await axios.post(store.routes['USER_SIGNIN'], jsonForm, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .catch((error) => {
        console.log(error.response);
        return error
      })
      .then(response => {
        if (response.status === 200) {
          localStorage.setItem('accessToken', response.data.access);
          localStorage.setItem('refreshToken', response.data.refresh);
          router.push({ name: 'home'},{ replace: true });
        }
      });
  }
};
</script>