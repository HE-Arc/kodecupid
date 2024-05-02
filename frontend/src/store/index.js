import {reactive, ref} from 'vue';


export const store = reactive({
  routes: null,
  error: {message: {}, type: ''},
});


export const setError =
    (message, type) => {
      store.error.message = message;
      store.error.type = type;
    }

export default {store, setError};