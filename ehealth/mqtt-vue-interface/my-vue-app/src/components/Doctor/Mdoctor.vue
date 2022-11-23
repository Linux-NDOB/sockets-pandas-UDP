<script>
import Ubar from "/src/components/Bars/Ubar.vue";
import { onMounted } from "@vue/runtime-core";
import { useRouter, useRoute } from "vue-router";
import { reactive, computed, ref } from "vue";
import HelloWorld from "/src/components/HelloWorld.vue";
import Footer from "/src/components/Bars/Footer.vue";

import Dfilter from "/src/components/Doctor/Dfilter.vue";

export default {
  components: {
    Ubar,
    Footer,
    HelloWorld,
    Dfilter,
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
    get: async function () {
      const res = await fetch(
        "http://localhost:8000/apiV1/persons/" + this.$route.params.id
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
        Parallax is an effect where the background content or image in this
        case, is moved at a different speed than the foreground content while
        scrolling.
      </p>
    </div>
  </div>

  <div class="container">
    <div class="row">
      <div class="col s12">
        <ul class="tabs">
          <li class="tab col s6">
            <a href="#test1" class='active'>REVISAR PACIENTES</a>
          </li>
          <li class="tab col s6">
            <a href="#test2">REALIZAR OBSERVACIONES</a>
          </li>
        </ul>
      </div>
      <div id="test1" class="col s12">
        <Dfilter />
      </div>
      <div id="test2" class="col s12">Test 2</div>
    </div>
  </div>

  <Footer />
</template>
