<script setup>
import { useStore } from "vuex";
const store = useStore();

function logout(){
   store.dispatch('logout');
  }


</script>

<template>
<!--DOCTOR UI NAVBAR, DSPLAYS NAME AND LOGOUT BUTTON-->

  <nav class="container blue darken-4">
    <div class="nav-wrapper">
      <a href="" class="brand-logo left"
        ><i class="material-icons">spa</i>Healthy Fork</a
      >
      <ul class="right">
        <li>
          <a href="/user/{{ data.person.person_id }}">Hola Dr(a) Nombre</a>
        </li>
       <li @click='logout'><router-link to="/">Salir</router-link> </li>
      </ul>
    </div>
  </nav>
</template>
