<template>
<div class="containerio">
  <div class="toga">
            <div class="img">
                <img class="profileimg" :src="`/api/v1/uploads/${user.profile}`" alt="Card image">
            </div>
                <div class="back">
                    <p class="name">{{user.fullname}}</p>
                    <p class="username">{{user.location}}</p>
                    <p class="usert">{{user.joined}}</p>
                    <p class="bio text-secondary">{{user.biography}}</p>
                </div>
  </div>
            <div class="lel">
              <div class="notif">
                <div class="tri">
                    <p class="powa "> {{user.posts}} </p>
                    <p class="pow">Posts</p>
                </div>
                <div class="tri">
                    <p class="powa"> {{user.follows}} </p>
                    <p class="pow">Followers</p>
                </div>
              </div>
                    <button id="folly" @click="followUser" type="submit">Follow</button>
            </div>
</div>
</template>

<script setup>

import { ref, onMounted} from "vue";
import {useRoute} from 'vue-router';

let csrf_token = ref("");
let user = ref({});
const route = useRoute();
const follow = ref()

function getCsrfToken() {
   fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
      followUser();
    });
}

function followUser(){
  const requestBody = JSON.stringify({id:localStorage.getItem('id')});
  
  fetch(`/api/users/${route.params.user_id}/follow`,{
  method : 'POST',
  body: requestBody,
  headers:{
    'Content-Type': 'application/json',
    'Authorization' : `Bearer ${localStorage.getItem('token')}`,
    'X-CSRFToken': csrf_token.value,
  }
  })
  .then((response)=>response.json())
  .then((data) =>{
    console.log(data);
    follow.value = data[1]
  });

  if (follow.value === 200){
    document.getElementById('folly').classList.add('following');
    user.follows += 1;
    }
  else if(follow.value === 330){
    document.getElementById('folly').classList.add('following');
  }
  else{
    alert("Cannot follow self");
  }
  
}

onMounted(() => {
  getCsrfToken();
  fetch(`/api/user/${route.params.user_id}`,{
    headers: {
      'Authorization' : `Bearer ${localStorage.getItem('token')}`,
    }
  })
.then(response => {
    if (!response.ok) {
      return response.json().then(data => {
        errorMessage.value = data.errors ? Object.values(data.errors) : ['Failed to post'];
        throw new Error('Failed to post', data.errors);
      });
    }else{
    return response.json()
    }
  })
.then(data => {
    user.value = data;
    console.log(data);
  })
.catch(error => {
    console.error('Error:', error);
  });
});

</script>

<style>
.containerio{
  display:flex;
  width:90%;
  max-width:1000px;
  gap: 20px;
  margin:auto;
  justify-content:space-between;
  background-color:white;
  border: 1px #ccc solid;
  padding:10px;
  height: 300px;
}

  .notif{
    display:flex;
    gap:20px;
    font-weight:600;
    text-align:center;
    font-size: 16px;
  }
  .powa{
    margin-bottom:0px;
  }
  .lel{
    display: grid;
    align-items: center;
  }

  #folly{
    height:40px;
    width:150px;
    font-weight:700;
    background-color:#8585FF;
  }

  #folly following{
    background-color: green;
  }

  .pow{
    color:gray;
    font-size:18px;
  }

  .name{
    font-weight:600;
    font-size:20px;
  }

  .username{
    margin-bottom:0px;
    color:gray;
  }

  .usert{
    color:gray;
  }

.toga {
    display: flex;
    align-items: center; 
}

.img {
    flex: 0 0 auto;
    margin-right: 20px; 
}

.profileimg {
  height: 250px;
  width: 200px;
}

.back {
  height: 100%;
  display: grid;
  align-items: center;
}

  




</style>
