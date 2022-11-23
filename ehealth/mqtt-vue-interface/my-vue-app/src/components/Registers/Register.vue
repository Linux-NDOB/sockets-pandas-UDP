<script setup>
import Ibar from "/src/components/Bars/Ibar.vue";
import Footer from "/src/components/Bars/Footer.vue";
import Rpatient from "/src/components/Registers/Rpatient.vue";
import Rdoctor from "/src/components/Registers/Rdoctor.vue";
import { onMounted } from "vue";

onMounted(() => {
  M.AutoInit();
});
</script>

<template>
  <Ibar />
  <div class="container">
    <br />
    <div class="row">
      <div class="col s12">
        <ul class="tabs">
          <li class="tab col s6">
            <a class="active indigo darken-4 white-text" href="#test1"
              >REGISTRO DE PACIENTES</a
            >
          </li>
          <li class="tab col s6">
            <a class="indigo white-text" href="#test2">REGISTRO DE DOCTORES</a>
          </li>
        </ul>
      </div>
      <div id="test1" class="col s12">
        <Rpatient />
      </div>
      <div id="test2" class="col s12">
        <Rdoctor />
      </div>
    </div>
  </div>
  <Footer />
</template>
