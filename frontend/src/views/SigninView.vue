<script setup>

</script>

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

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      emailRules: [
        v => !!v || 'Email is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => v.length >= 6 || 'Password must be at least 6 characters'
      ],
    };
  },
  methods: {
    handleSubmit() {
      // Handle form submission here
    }
  },

  name: 'SinginView',
};
</script>