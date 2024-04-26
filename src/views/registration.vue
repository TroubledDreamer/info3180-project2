<template>
  <form @submit.prevent="submitForm" class="registration-form">
    <h2>Registration</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" v-model="username" required>
    
    <label for="password">Password:</label>
    <input type="password" id="password" v-model="password" required>
    
    <label for="firstname">First Name:</label>
    <input type="text" id="firstname" v-model="firstname" required>
    
    <label for="lastname">Last Name:</label>
    <input type="text" id="lastname" v-model="lastname" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" v-model="email" required>
    
    <label for="location">Location:</label>
    <input type="text" id="location" v-model="location">
    
    <label for="biography">Biography:</label>
    <textarea id="biography" v-model="biography"></textarea>
    
    <label for="profile-photo">Profile Photo:</label>
    <input type="file" id="profile-photo" @change="handlePhotoUpload" accept="image/*">
    
    <button type="submit">Submit</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      firstname: '',
      lastname: '',
      email: '',
      location: '',
      biography: '',
      profilePhoto: null
    };
  },
  methods: {
    submitForm() {
      // Add form submission logic here
      const formData = {
        username: this.username,
        password: this.password,
        firstname: this.firstname,
        lastname: this.lastname,
        email: this.email,
        location: this.location,
        biography: this.biography,
        profilePhoto: this.profilePhoto
      };
      console.log(formData); // Example: Log form data to the console
    },
    handlePhotoUpload(event) {
      const file = event.target.files[0];
      this.profilePhoto = file;
    }
  }
};
</script>

<style scoped>
.registration-form {
  max-width: 300px;
  margin: 0 auto;
}

.registration-form h2 {
  margin-bottom: 20px;
}

.registration-form label {
  display: block;
  margin-bottom: 10px;
}

.registration-form input[type="text"],
.registration-form input[type="email"],
.registration-form input[type="password"],
.registration-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
}

.registration-form button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.registration-form button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>