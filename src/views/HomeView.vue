<template>
    <div class="containerized">
      <img alt="water under a bridge" src="@/assets/bridge.jpg"/>
      <HomeMenu />
    </div>
</template>

<script>
import HomeMenu from '@/components/HomeMenu.vue';

export default {
  components: {
    HomeMenu,
  },
};
</script>

<style>
.containerized{
  display:flex;
  justify-content:center;
  height:400px;
  width:auto;
  flex-direction:row;
  gap:20px;
}

img{
  height:400px;
  border-radius:5px;
}
/* Add any component specific styles here */
</style>
