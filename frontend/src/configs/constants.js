const API_SERVER_URL = import.meta.env.VITE_API_URL;

/*
admin/
api/token/ [name='token_obtain_pair']
api/token/refresh/ [name='token_refresh']
api/user/register/ [name='register']
api/tags/ [name='tag-list']
*/

export const API_ROUTES = {
    USER_SEARCH: API_SERVER_URL+'api/users',
    USER_MATCH: API_SERVER_URL+'/users/match',
    USER_LIKE: API_SERVER_URL+'/users/like',
    USER_DISLIKE: API_SERVER_URL+'/users/dislike',
    
    USER_SIGNUP: API_SERVER_URL+'/api/user/register/',
    USER_SIGNIN: API_SERVER_URL+'/api/token/',
    USER_TOKEN_REFRESH: API_SERVER_URL+'/api/token/refresh/',
    USER_DETAIL: API_SERVER_URL+'/api/user/',

    TAG_LIST: API_SERVER_URL+'/api/tags/',

};

export default API_ROUTES