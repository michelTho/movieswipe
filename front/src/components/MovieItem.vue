<script setup>

import { defineProps, toRefs } from "vue";

const props = defineProps({
  movieResponse: {
    image_url: String,
    title: String,
    description: String,
  },
});

const { movieResponse } = toRefs(props);

</script>

<template>
  <div class="movie-container">
    <img :src="movieResponse?.image_url" alt="image"/>
    <h1>{{ movieResponse?.title }}</h1>
    <p class="cutoff-text">{{ movieResponse?.description }}</p>
  </div>
</template>

<style scoped>

.movie-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

h1 {
  position: absolute;
  bottom: calc(156px + 1.2em);
  left: 24px;
  color: #ffffff;
  font-size: 3em;
}

p {
  position: absolute;
  bottom: 140px;
  left: 24px;
  color: #ffffff;
  font-size: 1.2em;
  width: calc(100% - 48px);
  padding: 24 0 24 0;
}

.cutoff-text {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3; 
  -webkit-box-orient: vertical;
}

img {
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  height: 100%;
  width: 100%;
  -webkit-mask-image: -webkit-gradient(linear, 0% 60%, 0% 100%, from(#000000ff), to(#00000000));
  mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));
}

</style>