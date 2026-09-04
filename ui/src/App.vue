<script setup>
import Cbutton from './components/cbutton.vue';
import {ref} from 'vue'
import Title from "./components/title.vue"
import SearchBar from './components/searchBar.vue';
import result from './components/result.vue'

const isClicked = ref(false)
const searchText = ref('')
const result = ref('')
function submit() {

  text = fetch('http://127.0.0.1:8000/submit', {
    method:'POST'
  })
  result = text.json()
  return result

}

</script>

<template>
  <div>
   <Title>

   </Title>
   <SearchBar v-model="searchText">

   </SearchBar>
   <div>
    <br>

   </div>
    <Cbutton @click="submit">
      Submit
    </Cbutton>
  </div>


  <div>
    <result v-model="result"></result>
  </div>
</template>

<style>
#app {
  background-image: linear-gradient(beige,rgb(203, 160, 156),rgb(246, 214, 234));
  
}
</style>


