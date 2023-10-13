<script setup lang="ts">

const emit = defineEmits(["dislike", "like", "superlike"]);

</script>

<template>
  <div class="votebar-container">
    <button class="base-button" @click="emit('dislike')">❌</button>
    <button class="base-button" @click="emit('superlike')">⭐</button>
    <button class="base-button" @click="emit('like')">💚</button>
  </div>  
</template>

<style scoped>
.votebar-container {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  padding: 24px 0px;
  height: 96px
}

.base-button {
  height: 96px;
  width: 96px;
  font-size: 2.4em;
  border-radius: 48px;
  border: 1px solid;
  border-color: #6a6a6a;
  background-color: #666666;
  cursor: pointer;
  box-shadow: 3px 3px 5px #333333;
}

.base-button:hover {
  background-color: #777777;
  border-color: #7a7a7a;
}
</style>