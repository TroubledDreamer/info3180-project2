<template>
  <UserProfile />
  <div v-for="post in posts" :key="post.id" class="cards">
    <div class="card-content">
      <img :src="`/api/v1/uploads/${post.photo}`" alt="Post">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';
import UserProfile from '@/components/UserProfile.vue';

let posts = ref([]);
const route = useRoute();

const fetchPosts = () => {
  if (!route.params.user_id) {
    console.error("Route params not defined");
    return; // or handle the case where no id is present
  }
  
  fetch(`/api/v1/users/${route.params.user_id}/posts`, {
    headers: {
      'Authorization' : `Bearer ${localStorage.getItem('token')}`,
    }
  })
  .then(response => response.json())
  .then(data => {
    posts.value = data.posts;
    console.log(posts)
  })
  .catch(error => {
    console.error('Error fetching posts:', error);
  });
};

onMounted(fetchPosts);
</script>

<style>
.cards{
    display: grid;;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    margin-top:20px;
    padding:10px;
}

.cards img{
  width: 100%;
  height:auto;
  border-radius:0px;
}

</style>
