const API_SERVER_URL = import.meta.env.VITE_API_URL;

export const API_ROUTES = {
    USER_SEARCH: API_SERVER_URL+'/users/search',
    USER_MATCH: API_SERVER_URL+'/users/match',
    USER_LIKE: API_SERVER_URL+'/users/like',
    USER_DISLIKE: API_SERVER_URL+'/users/dislike',
    
    USER_SIGNUP: API_SERVER_URL+'/auth/signup',
    USER_SIGNIN: API_SERVER_URL+'/auth/signin',

    ACCOUNT: API_SERVER_URL+'/account',
};

export default API_ROUTES