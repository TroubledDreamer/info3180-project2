<template>
  <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
    <!-- Error messages -->
  <div v-if="errorMessage" class="alert alert-danger">
    <ul>
      <li v-for="error in errorMessage" :key="error">{{ error }}</li>
    </ul>
  </div>
  <form id="postForm" @submit.prevent="post">
    <div class="form-group mb-3">
      <label for="photo" class="form-label">Photo</label>
      <input type="file" name="photo" class="form-control"/>
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Caption</label>
      <input type="text" name="description" plaeholder="Write a caption...." class="form-control"/>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>

<script setup>

import { ref, onMounted } from "vue";
import {useRouter} from 'vue-router';

const successMessage = ref(''); const errorMessage = ref('');

let csrf_token = ref("");
let token = ref("")

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

const post = () => {
  const postForm = document.getElementById('postForm');
  const formData = new FormData(postForm);
  const router = useRouter();

fetch("/api/v1/users/{user_id}/posts", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
.then(response => {
    if (!response.ok) {
      return response.json().then(data => {
        errorMessage.value = data.errors ? Object.values(data.errors) : ['Failed to post'];
        throw new Error('Failed to post');
      });
    }
    return response.json();
  })
.then(data => {
    // Display a success message
    successMessage.value = data.message;
  })
.catch(error => {
    console.error('Error:', error);
  });
};
</script>
