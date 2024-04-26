<template>
    <div>
      <h2>Add New Post</h2>
      <form @submit="submitForm">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="title" required>
  
        <label for="content">Content:</label>
        <textarea id="content" v-model="content" required></textarea>
  
        <label for="image">Image URL:</label>
        <input type="text" id="image" v-model="image" required>
  
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: '',
        content: '',
        image: ''
      };
    },
    methods: {
      submitForm() {
        // Perform form submission logic here
        // You can access the form data using this.title, this.content, this.image
        
        // Reset the form fields after submission
        this.title = '';
        this.content = '';
        this.image = '';
      }
    }
  };
  </script>
  
  <style scoped>
  form {
    max-width: 500px;
    margin: 0 auto;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 10px;
  }
  
  input[type="text"],
  textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
  }
  
  textarea {
    height: 100px;
  }
  
  button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  </style>