<template>
  <div class="container">
    <div class="text-center">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      <h1 class="message">{{ message }}</h1>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.");
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.text-center {
  text-align: center;
}

.logo {
  margin-bottom: 20px;
}

.message {
  font-size: 24px;
  color: #333;
}
</style>