<template>
    <template v-if="showError" >
      <v-alert v-model="error" :type="error.type" variant="tonal" closable @click:close="clearError" :border="true">
        <v-list bg-color="transparent">
          <v-list-item v-for="(value, key) in error.message" :key="key">
            <v-list-item-title>{{ key }}</v-list-item-title>
            <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-alert>
    </template>
  </template>
  
  <script setup>

  import { store } from '@/store';
  import { computed } from 'vue';

  
  const error = computed(() => store.error);
  const showError = computed(() => store.error.type != '');

  const clearError = () => {
    store.error = {message:{}, type:''};
  };
  </script>