<script setup>

import { ref, watch } from 'vue'

import MovieItem from './components/MovieItem.vue'
import VoteBarItem from './components/VoteBarItem.vue'
import { getMovie } from './router/getMovie'
import { postVote } from './router/postVote'

const movieResponse = ref({})
const constantWatchedValue = ref(0)

const likeMovie = async () => {
  await postVote({movieId: movieResponse.value.id, isUpvote: true})
  changeMovie()
}

const dislikeMovie = async () => {
  await postVote({movieId: movieResponse.value.id, isUpvote: false})
  changeMovie()
}

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
      <VoteBarItem :onDislike="dislikeMovie" :onLike="likeMovie" :onSuperlike="likeMovie" />
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
