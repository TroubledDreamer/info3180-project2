<template>
  <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
    <!-- Error messages -->
  <div v-if="errorMessage" class="alert alert-danger">
    <ul>
      <li v-for="error in errorMessage" :key="error">{{ error }}</li>
    </ul>
  </div>
  <form id="registerForm" @submit.prevent="register">
    <div class="form-group mb-3">
      <label for="username" class="form-label">Username</label>
      <input type="text" name="username" plaeholder="Username" class="form-control"/> </div>
    <div class="form-group mb-3">
      <label for="password" class="form-label">Password</label>
      <input type="text" name="password" plaeholder="Password" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="email" class="form-label">Email</label>
      <input type="text" name="email" plaeholder="Email" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="firstname" class="form-label">Firstname</label>
      <input type="text" name="firstname" plaeholder="Firstname" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="lastname" class="form-label">Lastname</label>
      <input type="text" name="lastname" plaeholder="Lastname" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="location" class="form-label">Location</label>
      <input type="text" name="location" plaeholder="Location" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="biography" class="form-label">Biography</label>
      <input type="text" id="biograph" name="biography" plaeholder="Biography" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="profile" class="form-label">Profile Photo</label>
      <input type="file" name="profile" class="form-control"/>
    </div>
    <button type="submit">Register</button>
  </form>
</template>

<script setup>

import { ref, onMounted } from "vue";

const successMessage = ref('');
const errorMessage = ref('');

let csrf_token = ref("");

function getCsrfToken() {
   fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

const register = () => {
  const registerForm = document.getElementById('registerForm');
  const formData = new FormData(registerForm);

fetch("/api/v1/register", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
.then(response => {
    if (!response.ok) {
      return response.json().then(data => {
        errorMessage.value = data.errors ? Object.values(data.errors) : ['Failed to register'];
        throw new Error('Failed to register');
      });
    }
    return response.json();
  })
.then(data => {
    // Display a success message
    successMessage.value = data.message;
    console.log(data);
  })
.catch(error => {
    console.error('Error:', error);
  });
};
</script>
