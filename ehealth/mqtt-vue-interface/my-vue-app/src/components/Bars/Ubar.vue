<script setup>
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

let n = ref("Nombre");

async function getN() {
  const res = await fetch(
    "http://localhost:8000/apiV1/patients/" + route.params.id
  );
  const patients = await res.json();

  n.value = patients.person.name;

  console.log(n);
}

onMounted(() => {
  getN();
});
</script>

<template>
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

        <li><router-link to="/">Cerrar sesión</router-link></li>
      </ul>
    </div>
  </nav>
</template>
