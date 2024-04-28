<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <div id="app">
    <header>
      <!-- Customize your header/navigation here -->
      <AppHeader />
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  // Add component logic here
};
</script>

<style>
body {
  padding-top: 75px;
  background-color: #fdf7ed;
}
</style>

