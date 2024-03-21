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
      component: () => import('@/views/cupid/SearchView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/match',
      name: 'match',
      component: () => import('@/views/cupid/MatchView.vue'),
      meta: { requiresAuth: true } 
    },
    {
      path: '/authentication',
      name: 'authentication',
      component: () => import('@/views/authentication/AuthenticationView.vue'),
      children: [
        { path: '', name: 'signin', component: () => import('@/views/authentication/SigninView.vue') },
        { path: 'signup', name: 'signup', component: () => import('@/views/authentication/SignupView.vue') },
      ]
    },
    {
      path: '/account',
      name: 'account',
      component: () => import('@/views/account/AccountView.vue'),
      meta: { requiresAuth: true },
      children: [
        { path: '', name: 'account-show', component: () => import('@/views/account/ShowView.vue') },
        { path: 'edit',name: 'account-edit', component: () => import('@/views/account/EditView.vue') }
      ]
    }
  ],
})

router.beforeEach((to, from, next) => {
  // Check if the route requires authentication
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Check if the user is authenticated (e.g., by checking if the JWT token exists)
    const jwtToken = localStorage.getItem('accessToken');
    if (!jwtToken) {
      // If the user is not authenticated, redirect to the login page
      next({ name: 'signin', query: { redirect: to.fullPath } });
    } else {
      // If the user is authenticated, proceed to the route
      next();
    }
  } else {
    // If the route doesn't require authentication, proceed to the route
    next();
  }
});

export default router
