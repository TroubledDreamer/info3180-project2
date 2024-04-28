<template>
<div class="containerio">
            <div class="img">
                <img class="profileimg" :src="`/api/v1/uploads/${user.profile}`" alt="Card image">
            </div>
                <div class="back">
                    <p class="name">{{user.fullname}}</p>
                    <p class="username text-secondary">{{user.location}}</p>
                    <p class="username text-secondary">{{user.joined}}</p>
                    <p class="bio text-secondary">{{user.biography}}</p>
                </div>
            <div class="lel">
                    <dd class="col-sm-9 "> {{user.posts}} </dd>
                    <dd class="col-sm-9 "> {{user.follows}} </dd>
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
.profile{
    width: 800px;
    height: 330px;
    margin-top:7em;
    display:flex;
    flex-direction: row;
    margin-bottom:4em;
    background-color:white;
}

.profileimg{
    margin-left:1em;
    width:150px;
    height:150px;
    object-fit: cover;
    border-radius: 50%;
}

.container{
    overflow: scroll;
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.card-img-top{
    width:100%;
    height:200px;
    object-fit: cover;
}



div.lel > p{
    margin-top:1em;
    margin-bottom:0em;
}



.name{
    font-weight:700;
    font-size:30px;
    margin-bottom:0em;
}

.username{
    margin-bottom:0em;
    color:rgb(170, 168, 168);
    font-weight:600;
}

.lel{
    margin-left:2.5em;
    width:75%;
}


dl{
    margin-top:1em !important; 
    font-weight:600;
}

.bio{
    margin-right:10em;
    font-size:15px;
    font-weight:600;
}

h1{
    margin-bottom: 1em;
    margin-right: 12em;
}
.btnsmall{
    width:85%;
    padding-top:.3em;
    padding-bottom: .3em;
}

.card-body{
    font-size: 15px;
    padding: .5rem .5rem;
    font-weight:500;
    padding-right:0em;
}

</style>
