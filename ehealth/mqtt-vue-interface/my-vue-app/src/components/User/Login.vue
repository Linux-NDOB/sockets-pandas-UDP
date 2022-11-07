<script setup>
import Ibar from "/src/components/Bars/Ibar.vue";
import Footer from "/src/components/Bars/Footer.vue";
import Lpatient from "/src/components/User/Lpatient.vue";
import Ldoctor from "/src/components/User/Ldoctor.vue";
import { onMounted } from 'vue';

onMounted(()=>{
  M.AutoInit();
});
</script>

<template>
<Ibar/>
<div class='container'>
<br>
<div class="row">
    <div class="col s12">
      <ul class="tabs">
        <li class="tab col s6"><a class='active indigo darken-4 white-text' href="#test1">INICIO DE PACIENTES</a></li>
        <li class="tab col s6"><a class="indigo white-text" href="#test2">INICIO DE DOCTORES</a></li>
      </ul>
    </div>
    <div id="test1" class="col s12">
    <Lpatient/>
    </div>
    <div id="test2" class="col s12">
    <Ldoctor/>
    </div>
  </div>
</div>
<Footer/>
</template>