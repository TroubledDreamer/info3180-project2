<template>
    <div class="logout-form">
      <h2>Logout</h2>
      <form @submit.prevent="logout">
        <button type="submit">Logout</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        // Add your logout logic here
        // clear session storage, remove tokens, etc.
        // You can also redirect the user to the login page after logout
      }
    }
  };
  </script>
  
  <style>
  .logout-form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  h2 {
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    justify-content: center;
  }
  
  button {
    padding: 10px 20px;
    background-color: #f44336;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #d32f2f;
  }
  </style>