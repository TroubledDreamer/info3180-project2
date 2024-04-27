<template>
  <form id="loginForm" @submit.prevent="login">
    <div class="form-group mb-3">
      <label for="username" class="form-label">Username</label>
      <input type="text" name="username" plaeholder="Username" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="password" class="form-label">Password</label>
      <input type="text" name="password" plaeholder="Password" class="form-control"/>
    </div>
    <button type="submit">Login</button>
  </form>
</template>

<script setup>

import { ref, onMounted } from "vue";
import {useRouter} from 'vue-router';

const successMessage = ref('');
const errorMessage = ref('');

let csrf_token = ref("");
let token = ref("")
let router = useRouter();

function getCsrfToken() {
   fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
  token.value = localStorage.getItem('token');
});

const login = () => {
  const loginForm = document.getElementById('loginForm');
  const formData = new FormData(loginForm);

fetch("/api/v1/auth/login", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
.then(response => {
    if (!response.ok) {
      return response.json().then(data => {
        errorMessage.value = data.errors ? Object.values(data.errors) : ['Failed to login'];
        throw new Error('Failed to login');
      });
    }
    return response.json();
  })
.then(data => {
    // Display a success message
    successMessage.value = 'User Logged In';
    token.value = data.token;
    localStorage.setItem('token',data.token);
    router.push("/explore")
  })
.catch(error => {
    console.error('Error:', error);
  });
};
</script>
