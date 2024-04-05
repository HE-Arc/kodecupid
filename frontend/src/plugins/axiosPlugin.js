import axios from 'axios';
import { store } from '@/store';
import router from '@/router'; // Assuming you have Vue Router set up

export default {
    install: (app) => {
        axios.defaults.headers.common['Content-Type'] = 'application/json';
        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;

        axios.interceptors.response.use(response => response, error => {
            const originalRequest = error.config;
            if (error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                const refreshToken = localStorage.getItem('refreshToken');

                return axios.post(store.routes['USER_TOKEN_REFRESH'], 
                {
                    'refresh': refreshToken
                },
                {
                    withCredentials: true
                })
                .then((response) => 
                {
                    if (response.status === 200)
                    {
                        localStorage.setItem('accessToken', response.data.access);
                        axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;
                        return axios(originalRequest);
                    }
                    else
                    {
                        router.push({ name: 'signin',replace: true, force: true });
                    }
                })
                .catch(() => 
                {
                    router.push({ name: 'signin',replace: true, force: true });
                });
            }
            return Promise.reject(error);
        });
    }
};