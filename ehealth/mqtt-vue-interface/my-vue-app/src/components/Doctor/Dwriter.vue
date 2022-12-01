<script>
import { reactive, computed, ref } from "vue";
import { useStore } from "vuex";
import { useVuelidate } from "@vuelidate/core";
import { useRouter, useRoute } from "vue-router";

import {
  required,
  minLength,
  maxLength,
  sameAs,
  numeric,
  alpha,
  alphaNum,
} from "@vuelidate/validators";
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      route: useRoute(),
      store: useStore(),
      v$: useVuelidate(),
      cc: "",
      vitals: [],
    };
  },
  setup() {
    const route = useRoute();

    const store = useStore();

    //let vector = computed(() => store.getters.patient);

    return { route, store };
  },
  methods: {
   
    get: async function (id) {
      this.v$.$validate(); // checks all inputs

      if (!this.v$.$error) {
        const ans = await fetch("http://192.168.100.231:8000/apiV1/vitals/" + id);

        const con = await ans.json();

        this.vitals = con.vitals;
        
        } else {
        M.toast({ html: "RELLLENE LOS DATOS CORRECTAMENTE", classes: "red" });
      }
    },
  },

  computed: {
    ...mapGetters({
      vector: "patients",
    }),
  },

  validations() {
    return {
      cc: {
        required,
        minLength: minLength(1),
        maxLength: maxLength(15),
        numeric,
      },
    };
  },
  mounted() {
    M.AutoInit();
  },
};
</script>


<template>

 <div class="center align-items center ">
    <div class="col s12">
      <div class="card purple darken-4">
        <div class="card-content white-text">
          <span class="card-title">Búsqueda de pacientes</span>
          <p>Porfavor ingrese la cédula del paciente a buscar</p>
         </div>
      </div>
    </div>
  </div>

  <div class="row">
    <form class="col s12">
      <div class="row">

      <div class="input-field col s8 row offset-s2">
          <input id="last_name" type="text" class="validate" v-model="cc"
>
          <label for="last_name">CEDULA PACIENTE</label>
        </div>
     
      <div class="input-field col s1 row">
           <a class='btn indigo' @click='get(this.cc)' >Buscar</a>
      </div>
      </div>    
    
    </form>
  </div>
        



  <div class="">
    <h5 class="indigo white-text center">REGISTROS DEL PACIENTE</h5>

    <DataTable
      :value="vitals"
      :scrollable="true"
      scrollHeight="400px"
      :loading="false"
    >
      <Column
        field="register_number"
        header="Numero de Registro"
        style="min-width: 200px"
      ></Column>
      <Column
        field="temperature"
        header="Temperatura(C)"
        style="min-width: 200px"
      ></Column>
      <Column
        field="heart_rate"
        header="F.Cardiaca(BPM)"
        style="min-width: 200px"
      ></Column>
      <Column
        field="resp_rate"
        header="F.Respiratoria(RPM)"
        style="min-width: 200px"
      ></Column>

      <Column
        field="oxigen"
        header="Oxigeno(%)"
        style="min-width: 200px"
      ></Column>
      <Column
        field="weight"
        header="Peso(Kg)"
        style="min-width: 200px"
      ></Column>
      <Column
        field="height"
        header="Altura(cm)"
        style="min-width: 200px"
      ></Column>

      <Column
        field="year_taken"
        header="Anio"
        style="min-width: 200px"
      ></Column>
      <Column
        field="month_taken"
        header="Mes"
        style="min-width: 200px"
      ></Column>
      <Column field="day_taken" header="Dia" style="min-width: 200px"></Column>
      <Column
        field="hour_taken"
        header="Hora"
        style="min-width: 200px"
      ></Column>
    </DataTable>
  </div>
</template>
