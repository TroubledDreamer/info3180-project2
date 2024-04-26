<template>
    <form @submit.prevent="submitForm" class="login-form">
      <h2>Login</h2>
      <label for="Username">Username:</label>
      <input type="Username" id="Username" v-model="Username" required>
      
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required>
  
      <button type="submit">Submit</button>
    </form>
  </template>
  
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
  </script>
  
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