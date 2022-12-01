<script setup>
// IMPORT COMPONENTS
import Ibar from "/src/components/Bars/Ibar.vue";
import Footer from "/src/components/Bars/Footer.vue";
</script>

<template>

  <Ibar />
  <div class="container">
    <img
      id="main-image"
      class="main-image"
      src="https://images.pexels.com/photos/806427/pexels-photo-806427.jpeg?cs=srgb&dl=pexels-miguel-%C3%A1-padri%C3%B1%C3%A1n-806427.jpg&fm=jpg "
      height="50%"
    />
    <div class="section white">
      <div class="row container">
        <h2 class="header">Healthy Fork</h2>
        <p class="grey-text text-darken-3 lighten-3">
          Helathy fork es un proyecto que busca conectar a los pacientes con los
          centros de salud, optimizar los tiempos de atención brindados y
          pertmitir a los pacientes poder tomar y revisar sus signos vitales
          donde deseen.
        </p>
      </div>
    </div>
  </div>
  <Footer />
</template>

<style lang='scss' scoped>
.main-image {
  max-width: 100%;
  max-height: 10%;
}
</style>
