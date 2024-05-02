<template>
  <v-app >
    <v-container>
      <v-row justify="center">
        <v-col cols="12" xs="12" sm="10" md="9" lg="7" xl="6">
          <header class="mb-6">
            <ErrorAlert/>
          </header>
          <v-main>
            <RouterView />
          </v-main>
          <footer>
            <Navbar />
          </footer>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue';
import ErrorAlert from '@/components/ErrorAlert.vue';
import { RouterView } from 'vue-router';
</script>