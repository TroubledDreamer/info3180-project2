<template>
    <div class="container">
        <h1>New Post</h1>
        <PostForm />
    </div>
</template>

<script>
import PostForm from '@/components/PostForm.vue';

export default {
  components: {
    PostForm,
  },
};
</script>

<style>
/* Add any component specific styles here */
</style>
