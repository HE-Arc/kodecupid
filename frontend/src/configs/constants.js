
/*
api/users/$ [name='user-list']
api/users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
api/users/add_tag/$ [name='user-add-tag']
api/users/add_tag\.(?P<format>[a-z0-9]+)/?$ [name='user-add-tag']
api/users/remove_tag/$ [name='user-remove-tag']
api/users/remove_tag\.(?P<format>[a-z0-9]+)/?$ [name='user-remove-tag']
api/users/(?P<pk>[^/.]+)/$ [name='user-detail']
api/users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
api/users/(?P<pk>[^/.]+)/tags/$ [name='user-tags']
api/users/(?P<pk>[^/.]+)/tags\.(?P<format>[a-z0-9]+)/?$ [name='user-tags']

api/tags/$ [name='tag-list']
api/tags\.(?P<format>[a-z0-9]+)/?$ [name='tag-list']

api/pictures/$ [name='picture-list']
api/pictures\.(?P<format>[a-z0-9]+)/?$ [name='picture-list']
api/pictures/(?P<pk>[^/.]+)/$ [name='picture-detail']
api/pictures/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='picture-detail']

api/likes/$ [name='like-list']
api/likes\.(?P<format>[a-z0-9]+)/?$ [name='like-list']

api/swipes/random_user/$ [name='swipe-random-user']
api/swipes/random_user\.(?P<format>[a-z0-9]+)/?$ [name='swipe-random-user']
api/swipes/(?P<pk>[^/.]+)/<int:pk>/$ [name='swipe-user-by-id']
api/swipes/(?P<pk>[^/.]+)/<int:pk>\.(?P<format>[a-z0-9]+)/?$ [name='swipe-user-by-id']

api/token/ [name='token_obtain_pair']
api/token/refresh/ [name='token_refresh']
*/



const routes_api = {
    'user-list':  '/api/users/',
    'user-add-tag':'/api/users/add_tag/',
    'user-remove-tag': '/api/users/remove_tag/',
    'user-current':'/api/users/current/',
    'user-tags':'/api/users/{id}/tags/',

    'user-detail':'/api/users/{id}/',

    'tag-list':'/api/tags/',

    'picture-list':'/api/pictures/',
    'picture-detail':'/api/pictures/{id}/',

    'like-list':'/api/likes/',

    'swipe-random-user':'/api/swipes/random_user/',
    'swipe-user-by-id':'/api/swipes/{id}/',
    'swipe-matches':'/api/swipes/matches/',

    'token_obtain_pair':'/api/token/',
    'token_refresh':'/api/token/refresh/',

};

const RouteEnum = {
    USER_LIST: 'user-list',
    USER_ADD_TAG: 'user-add-tag',
    USER_REMOVE_TAG: 'user-remove-tag',
    USER_CURRENT: 'user-current',
    USER_TAGS: 'user-tags',

    USER_DETAIL: 'user-detail',

    TAG_LIST: 'tag-list',

    PICTURE_LIST: 'picture-list',
    PICTURE_DETAIL: 'picture-detail',

    LIKE_LIST: 'like-list',

    SWIPE_RANDOM_USER: 'swipe-random-user',
    SWIPE_USER_BY_ID: 'swipe-user-by-id',
    SWIPE_MATCHES: 'swipe-matches',

    TOKEN_OBTAIN_PAIR: 'token_obtain_pair',
    TOKEN_REFRESH: 'token_refresh',
};

export {routes_api, RouteEnum };