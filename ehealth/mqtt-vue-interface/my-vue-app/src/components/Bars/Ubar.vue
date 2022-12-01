<script setup>
// IMPORTS
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useStore } from "vuex";
const store = useStore();


// ROUTER VARS
const router = useRouter();
const route = useRoute();

// DISPLAYED NAME
let n = ref("Nombre");

// GET NAME
async function getN() {
  const res = await fetch(
    "http://192.168.100.231:8000/apiV1/patients/" + route.params.id
  );
  const patients = await res.json();
  
  // SET DISPLAYED NAME
  n.value = patients.person.name;
}

function logout(){
   store.dispatch('logout');
  }

onMounted(() => {
  // GET NAME WHEN COMPONENT IS MOUNTED
  getN();
});
</script>

<template>
<!--NORMAL NAVBAR FUNCTIONALITY-->

  <nav class="container blue darken-4">
    <div class="nav-wrapper">
      <a href="" class="brand-logo left"
        ><i class="material-icons">spa</i>Healthy Fork</a
      >
      <ul class="right">
        <li><i class="material-icons">face</i></li>

        <li>
          <a>{{ n }}</a>
        </li>

        <li><i class="material-icons">logout</i></li>

        <li @click='logout'><router-link to="/">Salir</router-link> </li>
      </ul>
    </div>
  </nav>
</template>
