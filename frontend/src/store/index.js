import { reactive, ref } from 'vue';
import API_ROUTES from '@/configs/constants.js';

export const store = reactive({
  routes:API_ROUTES,
});

export default store;