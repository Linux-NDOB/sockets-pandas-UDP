<script>
import Ubar from "/src/components/Bars/Ubar.vue";
import { useRouter, useRoute } from "vue-router";
import Ucontent from "/src/components/User/Ucontent.vue";
import Footer from "/src/components/Bars/Footer.vue";

export default {
  components: {
    Ubar,
    Footer,
    Ucontent,
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
      <h2 class="header">Hola {{ data.name }}!</h2>
      <p class="grey-text text-darken-3 lighten-3">
        Esta es la interfaz principal de la aplicacion, solo debes deslizarte
        entre ellas dando click a las secciones que quieras consultar.
      </p>
    </div>
  </div>

  <Ucontent />

  <Footer />
</template>
