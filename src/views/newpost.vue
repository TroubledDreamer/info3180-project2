<template>
  <div>
    <h2>Add New Post</h2>
    <form @submit.prevent="newPost" id="postForm">
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="title" required>

      <label for="content">Content:</label>
      <textarea id="content" v-model="content" required></textarea>

      <label for="image">Image URL:</label>
      <input type="text" id="image" v-model="image" required>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

// Define reactive variables
let csrfToken = ref("");
let fetchResponseType = ref("");
let fetchResponse = ref("");
let title = ref("");
let content = ref("");
let image = ref("");

// Get route parameters
const router = useRouter();
const { params } = router;

// Fetch CSRF token
function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrfToken.value = data.csrf_token;
    })
    .catch((error) => {
      console.error(error);
    });
}

// Call getCsrfToken when the component is mounted
onMounted(() => {
  getCsrfToken();
});

// Handle new post form submission
function newPost() {
  const postForm = document.getElementById("postForm");
  const form_data = new FormData(postForm);

  fetch(`/api/v1/users/${params.id}/posts`, {
    method: "POST",
    body: form_data,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      fetchResponse.value = data;

      if (data.hasOwnProperty("errors")) {
        fetchResponseType.value = "danger";
      } else {
        fetchResponseType.value = "success";
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
</script>

<style scoped>
form {
  max-width: 500px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
}

textarea {
  height: 100px;
}

button {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
