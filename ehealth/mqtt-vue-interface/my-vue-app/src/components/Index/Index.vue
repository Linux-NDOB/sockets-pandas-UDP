<script setup>
import { onMounted } from 'vue';
import Ibar from "/src/components/Bars/Ibar.vue";
import Footer from "/src/components/Bars/Footer.vue";
</script>

<template>
    <Ibar/>
  <div class="container">
    <img id='main-image' class="main-image" 
    src="https://images.pexels.com/photos/806427/pexels-photo-806427.jpeg?cs=srgb&dl=pexels-miguel-%C3%A1-padri%C3%B1%C3%A1n-806427.jpg&fm=jpg "
    height="50%"
    >     
      <div class="section white">
        <div class="row container">
          <h2 class="header">Healthy Fork</h2>
          <p class="grey-text text-darken-3 lighten-3">
            Parallax is an effect where the background content or image in this
            case, is moved at a different speed than the foreground content while
            scrolling.
          </p>
        </div>
      </div>  
  </div>
  <Footer/>
</template>

<style lang='scss' scoped>
.main-image{
  max-width: 100%;
  max-height: 10%;
}
</style>