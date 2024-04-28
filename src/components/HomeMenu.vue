
<template>
  <div class="containers">
    <header>
      <h2>Photogram</h2>
      <hr />
    </header>
    <p>Share photos of your favourite moments with friend, family and the world.</p>
    <div class="button-container">
      <RouterLink to="/register">
        <button class="register">Register</button>
      </RouterLink>
      <RouterLink to="/login">
        <button class="login">Login</button>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>

import { ref, onMounted } from "vue";
import {RouterLink} from 'vue-router';

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

</script>
<style>
.containers {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 20px;
}


.button-container {
  display: flex;
  justify-content: space-around;
  width: 100%; /* Stretch buttons to container width */
  margin:auto;
}

h2{
  text-align:center;
  margin-bottom:10px;
  margin-top:5px;
}

.register {
  background-color: blue;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 150px;
}

.login {
  background-color: green;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width:150px;
}

</style>
