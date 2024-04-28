<template>
    <div class="containerama">
        <h3>Login</h3>
        <LoginForm />
    </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue';

export default {
  components: {
    LoginForm,
  },
};
</script>

<style>
/* Add any component specific styles here */
.containerama{
  display:grid;
  justify-content:center;
}
</style>
