<template>
  <form id="loginForm" @submit.prevent="login">
    <div>
      <label for="username" class="form-label">Username</label>
      <input type="text" name="username" plaeholder="Username" class="form-control"/>
    </div>
    <div>
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
let userid;

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
    token.value = data[0].token;
    userid = data[0].id;
    console.log(data);
    localStorage.setItem('token',token.value);
    localStorage.setItem('id',userid);
    console.log(userid)
    router.push("/explore")
  })
.catch(error => {
    console.error('Error:', error);
  });
};
</script>

<style>
  #loginForm {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 300px; 
    width: 300px; 
    background-color: white; 
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
  }

  .form-label {
    margin-bottom: 10px;
    font-weight: bold;
  }

  .form-control {
    width: 80%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    margin-bottom: 20px;
  }

  button[type="submit"] {
    width: 80%;
    padding: 10px;
    background-color: green; 
    color: #fff; 
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
  }
</style>
