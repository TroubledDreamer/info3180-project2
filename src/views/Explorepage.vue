<template>
    <div class="explore-page">
      <h2>Explore</h2>
      <div v-for="post in posts" :key="post.id" class="post">
        <img :src="post.photo" alt="Post Image">
        <div class="post-details">
          <h3>{{ post.caption }}</h3>
          <p>Posted by: {{ post.username }}</p>
          <button @click="viewUserProfile(post.user_id)">View Profile</button>

        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let posts = ref([]);
  
  function fetchPosts(){
      fetch("/api/v1/posts", {
        "headers": {
          "Authorization": `Bearer ${localStorage.getItem('token')}`
        }
      })
      .then(response => {
              if(response.ok){return response.json()}
              else{return Promise.reject('Something was wrong with fetch request!')}
          })
          .then(data => {
              console.log(data);
              posts.value = data["posts"]
          })
          .catch(error => {
              console.log(error);
          })
      }
  
      onMounted(() => {
        fetchPosts()
      });






  
  </script>
  
  <style scoped>
  .explore-page {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .explore-page h2 {
    margin-bottom: 20px;
  }
  
  .post {
    display: flex;
    margin-bottom: 20px;
  }
  
  .post img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    margin-right: 20px;
  }
  
  .post-details {
    flex-grow: 1;
  }
  
  .post-details h3 {
    margin-bottom: 10px;
  }
  
  .post-details p {
    margin-bottom: 10px;
  }
  
  .post-details button {
    background-color: #007bff;
    color: #fff;
    padding: 5px 10px;
    border: none;
    cursor: pointer;
  }
  
  .post-details button:hover {
    background-color: #0056b3;
  }
  </style>