import axios from 'axios';
import {ApiClient} from '@/clients/apiClient.js';
import router from '@/router';

export default {
    install: (app) => {
        axios.defaults.headers.common['Content-Type'] = 'application/json';
        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;

        axios.interceptors.response.use(response => response, async error => {
            const originalRequest = error.config;
            if (error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                const response = await ApiClient.refreshToken();
                if (response) {
                    return axios(originalRequest);
                }else{
                    router.push({name: 'signin', replace: true, force: true});
                }
            }
            return Promise.reject(error);
        });
    }
};