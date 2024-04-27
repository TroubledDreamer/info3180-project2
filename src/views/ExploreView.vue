<template>
  <div>
      <div class="card-container">
        <div v-for="post in posts" :key="post.id" class="card">
          <div class="card-content">
            <img :src="post.photo" class="card-img-top" alt="Post">
            <div class="text">
              <p class="card-text">{{ post.description }}</p>
              <p class="card-text">{{post.created_on}}</p>
              <p class="card-text">{{post.likes}}</p>
            </div>
          </div>
        </div>
      </div>
      <RouterLink to="/posts/new">
        <button>New Post</button>
      </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {RouterLink} from 'vue-router';

let posts = ref([]);

const fetchPosts = () => {
  fetch("/api/v1/posts", {
    method: 'GET'
  })
    .then(response => response.json())
    .then(data => {
      posts.value = data.posts;
    })
    .catch(error => {
      console.error('Error fetching posts:', error);
    });
};

onMounted(() => {
  fetchPosts;
});
</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  margin: 20px;
  width: 300px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-img-top {
  width: 100%;
  height: 200px; 
  object-fit: cover; 
}

.text {
  flex: 1;
  padding: 15px;
}

.card-title {
  font-size: 18px;
  margin-top: 0;
}

h5{
  font-weight:bold;
}

.card-text {
  margin-bottom: 0;
}
</style>
