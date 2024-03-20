<template>
  <v-form ref="form" @submit.prevent="handleSubmit(this)">
    <v-container>
      <v-row>
        <v-col>
          <v-img cover class="rounded" src="/logo1024.png"></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>email*</v-label>
          <v-text-field v-model="email" label="Email" type="email" :rules="emailRules" required />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-label>password*</v-label>
          <v-text-field v-model="password" label="Password" type="password" :rules="passwordRules" required />
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-btn type="submit" color="primary">Register</v-btn>
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
import { useRouter } from 'vue-router'

const email = ref(null);
const password = ref(null);
const emailRules = [
  v => !!v || 'Email is required',
  v => /.+@.+\..+/.test(v) || 'E-mail must be valid'
];
const passwordRules = [
  v => !!v || 'Password is required',
  v => v.length >= 6 || 'Password must be at least 6 characters'
];

const formData = {
  email,
  password
};


const handleSubmit = async (form) => {
  {
    const response = await axios.post(store.routes['USER_SIGNUP'], formData)
    .catch((error) => {
      if (error.response.data.email) {
        form.emailErrors.push(error.response.data.email[0]);
      }
      if (error.response.data.password) {
        form.passwordErrors.push(error.response.data.password[0]);
      }
    });

    if (response.status === 200) {
      store.user.value = response.data;
      router.push({ name: 'signin' });
    }
  }
};
</script>