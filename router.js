import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: HomePage },
  { path: '/register', component: RegisterPage },
  { path: '/login', component: LoginPage },
  { path: '/logout', component: LogoutPage }, 
  { path: '/explore', component: ExplorePage }, 
  { path: '/users/:user_id', component: UserProfilePage },
  { path: '/posts/new', component: NewPostPage }, 
];

const router = new VueRouter({
  routes,
  mode: 'history', // enables clean URLs without hash (#)
});

export default router;