<template>
    <div class="user-profile-page">
      <h2>User Profile</h2>
      <div class="profile-header">
        <img :src="profilePhoto" alt="Profile Photo">
        <div class="profile-details">
          <h3>{{ username }}</h3>
          <p>{{ location }}</p>
          <p>{{ biography }}</p>
          <button @click="followUser">{{ isFollowing ? 'Following' : 'Follow' }}</button>
          <p>Followers: {{ followerCount }}</p>
        </div>
      </div>
      <div class="user-photos">
        <div v-for="photo in photos" :key="photo.id" class="photo">
          <img :src="photo.url" alt="User Photo">
        </div>
      </div>
    </div>
  </template>
  
  <script>




  function fetchPost(user_id){
      fetch("/api/v1/users/${user_id}/posts", {
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
              post.value = data["post"]
              localStorage.setItem('post', JSON.stringify(data.post));
          })
          .catch(error => {
              console.log(error);
          })
      }
  
      onMounted(() => {
        fetchPost()
      });





  post= localStorage.getItem('post')

  let username = ref(post.username);
  let location = ref(post.location);
  let biography = ref(post.biography);
  let profilePhoto = ref(post.profilePhoto);
  let isFollowing = ref(post.isFollowing);
  let followerCount = ref(post.followerCount);
  let photos = ref(post.photos);



  export default {
    data() {
      return {
        username: '', // User's username
        location: '', // User's location
        biography: '', // User's biography
        profilePhoto: '', // URL of user's profile photo
        isFollowing: false, // Whether the current user is following this user
        followerCount: 0, // Number of followers for this user
        photos: [] // Array of user's photos
      };
    },
    methods: {
      followUser() {
        // Add logic to toggle the follow status and update the follower count
        this.isFollowing = !this.isFollowing;
        if (this.isFollowing) {
          this.followerCount++;

      fetch("/api/v1/users/${user_id}/follow", {
        "headers": {
          "Authorization": `Bearer ${localStorage.getItem('token')}`
        }
      })

    .then(function(response) {
        return response.json();
    })

    .then(function(data) {
        console.log(data);
        fetchResponse.value = data
                    
        if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
                generateToken() 
            }

    })
    .catch(function(error) {
        console.log(error);
    });





        } else {
          this.followerCount--;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .user-profile-page {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .user-profile-page h2 {
    margin-bottom: 20px;
  }
  
  .profile-header {
    display: flex;
    margin-bottom: 20px;
  }
  
  .profile-header img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin-right: 20px;
  }
  
  .profile-details {
    flex-grow: 1;
  }
  
  .profile-details h3 {
    margin-bottom: 10px;
  }
  
  .profile-details p {
    margin-bottom: 10px;
  }
  
  .profile-details button {
    background-color: #007bff;
    color: #fff;
    padding: 5px 10px;
    border: none;
    cursor: pointer;
  }
  
  .profile-details button:hover {
    background-color: #0056b3;
  }
  
  .user-photos {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
  }
  
  .user-photos .photo img {
    width: 100%;
    height: auto;
  }
  </style>