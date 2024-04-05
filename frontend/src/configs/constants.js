const API_SERVER_URL = import.meta.env.VITE_API_URL;

/*
'admin/'
'api/token/'
'api/token/refresh/'
'api/user/'
'api/tags/'
'api/like/'
*/

export const API_ROUTES = {
    USER_SEARCH: API_SERVER_URL+'/api/user/',
    USER_MATCH: API_SERVER_URL+'/api/users/match/',
    USER_LIKE: API_SERVER_URL+'/api/like/',
    
    USER_SIGNUP: API_SERVER_URL+'/api/user/',
    USER_SIGNIN: API_SERVER_URL+'/api/token/',
    USER_TOKEN_REFRESH: API_SERVER_URL+'/api/token/refresh/',
    
    USER: API_SERVER_URL+'/api/user/',
    USER_RANDOM: API_SERVER_URL+'/api/user/random',
    
    TAG_LIST: API_SERVER_URL+'/api/tags/',
    
    USER_TAG_ADD: API_SERVER_URL+'/api/tags/',
    USER_TAG_REMOVE: API_SERVER_URL+'/api/tags/',

    USER_TAGS: API_SERVER_URL+'/api/user/tags'

};

export default API_ROUTES