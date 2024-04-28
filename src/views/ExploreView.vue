<template>
  <div class="corpo">
      <div class="post">
        <div v-for="post in posts" :key="post.id">
          <div class="postcontainer">
          <RouterLink :to='"/users/" + post.user_id' class="madness">
              <div class="profileset">
                <img :src="`/api/v1/uploads/${post.profile}`" alt="user_profile" class="post-image">
                <p id="username">{{post.username}}</p>
              </div>
          </RouterLink>
            <div class="imageset">
              <img :src="`/api/v1/uploads/${post.photo}`"  alt="Post">
                <p >{{ post.description }}</p>
            </div>
            <div class="bottomset">
              <p class="clicker" @click="like(post.id)" >{{post.likes}} Likes</p>
              <p>{{post.created_on}}</p>
            </div>
          </div>
        </div>
      </div>
      <RouterLink to="/posts/new" class="madness">
        <button>New Post</button>
      </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {RouterLink} from 'vue-router';

let posts = ref([]);
let likes = ref();
let csrf_token = ref("");

const fetchPosts = () => {
  fetch("/api/v1/posts", {
    method: 'GET',
    headers: {
      'Authorization' : `Bearer ${localStorage.getItem('token')}`,
    }
  })
    .then(response => response.json())
    .then(data => {
      posts.value = data.posts;
      console.log(posts);
    })
    .catch(error => {
      console.error('Error fetching posts:', error);
    });
};

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

function like(post_id){
  const requestBody = JSON.stringify({user_id:localStorage.getItem("id")});
  const postIndex = posts.value.findIndex(post => post.id === post_id);
  const poster = posts.value[postIndex];
  fetch(`/api/v1/posts/${post_id}/like`, {
    method: 'POST',
    body: requestBody,
    headers: {
      'Content-Type': 'application/json',
      'Authorization' : `Bearer ${localStorage.getItem('token')}`,
      'X-CSRFToken': csrf_token.value,
    }
  })
    .then(response => response.json())
    .then(data => {
      likes.value = data[1];
      console.log(poster);
      console.log(likes.value);
      if (likes.value==200){
        poster.likes++;
      }
    })
    .catch(error => {
      console.error('Error fetching posts:', error);
    });
};

  fetchPosts();
</script>
<style scoped>

.post {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.postcontainer {
  width: 500px; 
  height: 550px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  display: grid;
  grid-template-rows: 7% 70% auto;
  gap: 10px; 
}

.profileset {
  display: flex;
}

.profileset img {
  margin-right: 10px;
}

.profileset p{
  margin-bottom:0px;
}

.imageset {
  display: flex;
  flex-direction: column;
}

.imageset img {
  width: 100%;
  height: 90%;
}

.imageset p {
  margin: 10px 0;
  margin-bottom: 0px;
  margin-top: 20px;
}

.bottomset {
  display: flex;
  justify-content: space-between;
  align-items: end;
}

.bottomset p {
  margin: 0;
}

  body{
    background-color: #fbeeda;
  }

button {
  display: block;
  width: 100%;
  min-width: 200px;
  padding: 10px;
  margin: 20px auto;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.madness{
  margin-top:0px;
  margin-bottom:0px;
  width: 50px;
  height: 50px;
}
    .corpo{
      display:flex;
      justify-content:center;
      gap:30px;
    }

    .clicker{
      cursor:pointer;
    }


</style>
