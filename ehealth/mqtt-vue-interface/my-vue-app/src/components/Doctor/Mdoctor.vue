<script>
//IMPORTS
import Ubar from "/src/components/Bars/Ubar.vue";
import { onMounted } from "@vue/runtime-core";
import { useRouter, useRoute } from "vue-router";
import { reactive, computed, ref } from "vue";
import Footer from "/src/components/Bars/Footer.vue";

import Dfilter from "/src/components/Doctor/Dfilter.vue";
import Dupdate from "/src/components/Doctor/Dupdate.vue";
import Dwriter from "/src/components/Doctor/Dwriter.vue";

//COMPONENTS AND LOGIC PART
export default {
  components: {
    Ubar,
    Footer,
    Dfilter,
    Dupdate,
    Dwriter,
  },
  data() {
    return {
      data: {
        name: "",
      },
    };
  },
  setup() {
    const router = useRouter();
    const route = useRoute();
  },
  methods: {
    //GET DOCTOR DATA FROM API
    get: async function () {
      const res = await fetch(
        "http://192.168.100.231:8000/apiV1/persons/" + this.$route.params.id
      );

      const us = await res.json();

      this.data.name = us.person.name;
    },
  },
  mounted() {
    M.AutoInit();

    this.get();
  },
};
</script>

<template>
  <Ubar />

  <div class="section white">
    <div class="row container">
      <h2 class="header">Hola {{ data.name }}</h2>
      <p class="grey-text text-darken-3 lighten-3">
      Esta es tu interfaz principal, donde podrás buscar pacientes y ver sus signos vitales.
       
      </p>
    </div>
  </div>

  <div class="container">
    <div class="row">
      <div class="col s12">
        <ul class="tabs">
          <li class="tab col s4">
            <a href="#test1" class="active indigo white-text">BUSCAR PACIENTES</a>
          </li>
          <li class="tab col s4">
            <a href="#test2" class='indigo white-text'>CONSULTAR REGISTROS</a>
          </li>
           <li class="tab col s4">
            <a href="#test3" class="indigo white-text">ACTUALIZAR DATOS</a>
          </li>
        </ul>
      </div>

      <div id="test1" class="col s12">
        <Dfilter />
      </div>

      <div id="test2" class="col s12">
      <Dwriter/>
      </div>

      <div id="test3" class="col s12">
      <Dupdate/>
      </div>

    </div>
  </div>

  <Footer />
</template>
