import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Registration from '../components/Registration.vue';
import Explore from '../components/Explore.vue';
import Profile from '../components/Profile.vue';
import NewPost from '../components/NewPost.vue';
import NewPost from '../components/Logout.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/registration', component: Registration },
  { path: '/explore', component: Explore },
  { path: '/profile', component: Profile },
  { path: '/newpost', component: NewPost },
  { path: '/Logout', component: Logout }
];

const router = new VueRouter({
  routes
});

export default router;