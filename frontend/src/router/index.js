import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('@/views/SearchView.vue')
    },
    {
      path: '/match',
      name: 'match',
      component: () => import('@/views/MatchView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignupView.vue')
    },
    {
      path: '/signin',
      name: 'signin',
      component: () => import('@/views/SigninView.vue')
    },
    {
      path: '/account',
      name: 'account',
      component: () => import('@/views/AccountView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue')
    }
  ],
})



// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth) {

//     axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('accessToken')}`;
//     axios.interceptors.response.use(
//       response => response,
//       error => {
//         if (error.response.status === 401) {
//           localStorage.removeItem('accessToken');
//           next({ name: 'signin' });
//         }
//         return Promise.reject(error);
//       }
//     )
//     if () {
//       // User is authenticated, allow access
//       next();
//     } else {
//       // User is not authenticated, redirect to login page
//       next({ name: 'signin' });
//     }
//   } else {
//     // Route does not require authentication, allow access
//     next();
//   }
// });


export default router
