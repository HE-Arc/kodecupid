import {ApiClient} from '@/clients/apiClient.js';
import router from '@/router';
import axios from 'axios';

export default {
  install:
      (app) => {
        axios.defaults.headers.common['Content-Type'] = 'application/json';
        axios.defaults.headers.common['Authorization'] =
            `Bearer ${localStorage.getItem('accessToken')}`;

        axios.interceptors.response.use(response => response, async (error) => {
          const originalRequest = error.config;
          if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
              const response = await ApiClient.refreshToken();
              if (response) {
                originalRequest.headers.Authorization = `Bearer ${localStorage.getItem('accessToken')}`
                return axios(originalRequest);
              } else {
                router.push({name: 'signin', replace: true, force: true});
              }
            } catch (refreshError) {
              console.error('Error refreshing token:', refreshError);
              router.push({name: 'signin', replace: true, force: true});
            }
          }
          return Promise.reject(error);
        });
      }
};