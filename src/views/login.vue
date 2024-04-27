<template>
    <form @submit.prevent="login"  id="loginForm"  class="login-form">
      <h2>Login</h2>
      <label for="Username">Username:</label>
      <input type="Username" id="Username" v-model="Username" required>
      
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required>
  
      <button type="submit">Submit</button>
    </form>
  </template>



</template>


<script setup>
import { ref , onMounted } from 'vue';
let csrf_token = ref("");
let fetchResponse = ref("");
let fetchResponseType = ref("");



let token = ref("");

onMounted(() => {
    token.value = localStorage.getItem('token');
});

function generateToken() {
    console.log('token is being generated')
    fetch('/api/v1/generate-token')
    .then(resp => resp.json())
    .then(data => {
        token.value = data.token;
        localStorage.setItem('token', data.token)
        emits('show-modal', { message: "Token Successfully Generated!", token: token.value});
    })
    .catch(err => {
        console.log(err)
        emits('show-modal', "Token Generation failed!");
    })
}

  

function getCsrfToken() {

    fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })

}


onMounted(() => {
    getCsrfToken();
})


function login() {
    let loginForm = document.getElementById('loginForm');
    let form_data = new FormData(loginForm);
    


    fetch("/api/v1/auth/login", {
        method: "POST",
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
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
}








</script>

<!--   
  <script>

  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
      submitForm() {
        // Add form submission logic here
        const formData = {
          email: this.email,
          password: this.password
        };
        console.log(formData); // Example: Log form data to the console
      }
    }
  };



  </script> -->
  
  <style scoped>
  .login-form {
    max-width: 300px;
    margin: 0 auto;
  }
  
  .login-form h2 {
    margin-bottom: 20px;
  }
  
  .login-form label {
    display: block;
    margin-bottom: 10px;
  }
  
  .login-form input[type="email"],
  .login-form input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
  }
  
  .login-form button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }
  
  .login-form button[type="submit"]:hover {
    background-color: #0056b3;
  }
  </style>