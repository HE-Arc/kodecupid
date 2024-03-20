<template>
  <v-form @submit.prevent="handleSubmit">
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

import { ref } from 'vue';
import { store } from '@/store';
import axios from 'axios';
import { useRouter } from 'vue-router'

const router = useRouter()

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

const handleSubmit = async () => {
  {
    const response = await axios.post(store.routes['USER_SIGNIN'], formData).catch((error) => {
      store.user.value = {
        id: -1,
        name: 'User not found',
        bio: 'User not found',
        avatar: 'https://picsum.photos/170',
        tags: ["java", "python", "javascript", "c++"],
      }

      router.push({ name: 'home' });
    });

    if (response.status === 200) {
      store.user.value = response.data;
      router.push({ name: 'home' });
    }
  }
};
</script>