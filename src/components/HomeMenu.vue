
<template>
  <div>
    <h1>Photogram</h1>
    <p>Share photos of your favourite moments with friend, family and the world.</p>
    <div>
      <RouterLink to="/register">
        <button>Register</button>
      </RouterLink>
      <RouterLink to="/login">
        <button>Login</button>
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
