<script setup>
import Navbar from '@/components/Navbar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="10" md="9" lg="6" xl="6">
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