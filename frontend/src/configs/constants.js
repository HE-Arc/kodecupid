const API_SERVER_URL = import.meta.env.VITE_API_URL;

/*
'admin/'
'api/token/'
'api/token/refresh/'
'api/user/register/'
'api/tags/'
'api/like/'
*/

export const API_ROUTES = {
    USER_SEARCH: API_SERVER_URL+'api/users',
    USER_MATCH: API_SERVER_URL+'/users/match',
    USER_LIKE: API_SERVER_URL+'/like',
    
    USER_SIGNUP: API_SERVER_URL+'/api/user/register/',
    USER_SIGNIN: API_SERVER_URL+'/api/token/',
    USER_TOKEN_REFRESH: API_SERVER_URL+'/api/token/refresh/',
    
    USER_DETAIL: API_SERVER_URL+'/api/user/',
    
    TAG_LIST: API_SERVER_URL+'/api/tags/',

};

export default API_ROUTES