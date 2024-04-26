<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <div id="app">
    <header>
      <!-- Customize your header/navigation here -->
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/Register">Register</router-link>
        <router-link to="/Login">Login</router-link>
        <router-link to="/Explore">Explore</router-link>
        <router-link to="/Profile">Profile</router-link>
        <router-link to="/Newpost">Newpost</router-link>
        <router-link to="/Logout">Logout</router-link>
      </nav>
    </header>

    <main>
      <router-view></router-view>
    </main>

    <footer>
      <!-- Customize your footer here -->
      <p>&copy; 2024 Your Website. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  // Add component logic here
};
</script>

<style>
/* Add component styles here */
header {
  background-color: #f5f5f5;
  padding: 10px;
}

nav {
  display: flex;
  justify-content: center;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
}

footer {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: center;
  font-size: 14px;
}
</style>