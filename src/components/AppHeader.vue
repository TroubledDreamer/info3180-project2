<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">VueJS with Flask</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li v-if="user_id" class="nav-item">
              <RouterLink class="nav-link" to="/users/${user_id}">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <button class="nav-link" @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink, useRouter } from "vue-router";
import {ref, onMounted} from 'vue';

const token = ref(localStorage.getItem("token") || "");
const user_id = ref(null);
const router = useRouter()

async function logout() {
  try {
    const response = await fetch('/logout', { method: 'POST' }); // Send POST request
    if (!response.ok) {
      throw new Error('Logout failed');
    }
    localStorage.removeItem('token');
    user_id.value = null; 
    router.push('/login');  
  } catch (error) {
    console.error('Logout error:', error);
  }
}

function getToken(token){
  fetch(`api/v1/decode-token/${token}`,{
        method: 'POST'
      })
  .then(response => {
      if (!response.ok) {
        throw new Error(`Error decoding token: ${response.statusText}`);
      }
      return response.json();
  })
  .then(data => {
    user_id = data.token;
    this.error = null;
  })
  .catch(error => {
    console.error('Error decoding token:', error);
    this.error = error.message;
  });
}

onMounted(()=>{
  if(token.value){
    getToken(token);
  };
});
  
</script>

<style>
/* Add any component specific styles here */
</style>
