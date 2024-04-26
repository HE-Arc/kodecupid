import { reactive, ref } from 'vue';
import API_ROUTES from '@/configs/constants.js';

export const store = reactive({
  routes:API_ROUTES,
  error: {message:{},type:''},
});


export const setError = (message,type) => {
    store.error.message = message;
    store.error.type = type;
}

export default {store, setError};