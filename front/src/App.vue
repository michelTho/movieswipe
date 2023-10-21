<script setup>

import { ref, watch } from 'vue'

import MovieItem from './components/MovieItem.vue'
import VoteBarItem from './components/VoteBarItem.vue'
import { getMovie } from './router/getMovie'

const movieResponse = ref({})
const constantWatchedValue = ref(0)

const changeMovie = () => {
  constantWatchedValue.value++
}

watch(
  constantWatchedValue,
  async () => {
    const response = await getMovie()
    movieResponse.value = response
  },
  { immediate: true }
)

</script>

<template>
  <main>
    <div class="swiper-container">
      <MovieItem :movieResponse="movieResponse" />
      <VoteBarItem :onDislike="changeMovie" :onLike="changeMovie" :onSuperlike="changeMovie" />
    </div>
  </main>
</template>

<style scoped>
.swiper-container {
  position: relative;
  width: 656px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-color: #141414;
}
</style>
