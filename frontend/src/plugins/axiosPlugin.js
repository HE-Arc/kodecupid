import axios from 'axios';
import { store } from '@/store';

export default {
    install: (app) => {
        console.log('axios plugin installed');
        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;
        axios.interceptors.response.use(response => response, error => {
            if (error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                const refreshToken = localStorage.getItem('refreshToken');

                return axios.post(store.routes['USER_SIGNIN'], {
                    'refresh': refreshToken
                }).then((response) => {
                    if (response.status === 200) {
                        localStorage.setItem('accessToken', response.data.access);
                        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;
                    }

                    return axios(originalRequest);
                });
            }
            return Promise.reject(error);
        });
        app.config.globalProperties.$axios = axios;
    }
};