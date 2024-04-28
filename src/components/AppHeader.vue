<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Photogram</a>
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
            <li  class="nav-item">
              <RouterLink v-if="logged" to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li  class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li  class="nav-item">
              <a class="nav-link" id="clicked" @click="bothersome">My Profile</a>
            </li>
            <li  class="nav-item">
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
import {ref, onMounted, computed} from 'vue';

const successMessage = ref("");
const router = useRouter();
let csrf_token = ref("");
let id = localStorage.getItem('id');



onMounted(() => {
  getCsrfToken();
});

const logged = computed(() => {
  return localStorage.getItem('token') != null;
});

function bothersome(){
  let child = localStorage.getItem('id');
  if (child){
    router.push(`/users/${child}`);
  } 
  else{
    router.push("/");
  }
}



function getCsrfToken() {
   fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}


const logout = () => {

fetch("/api/v1/auth/logout", {
    method: 'POST',
    headers: {
      'X-CSRF-Token': csrf_token.value,
      'Authorization' : `Bearer ${localStorage.getItem('token')}`,
    }
  })
.then(data => {
    // Display a success message
    localStorage.removeItem('token');
    localStorage.removeItem('id');
    router.push("/")
  })
.catch(error => {
    console.error('Error:', error);
  });
};
</script>
<style>
/* Add any component specific styles here */
#clicked{
  cursor:pointer;
}
</style>
