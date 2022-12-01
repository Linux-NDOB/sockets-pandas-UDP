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
      name: "",
      sname: "",
      lname: "",
      slname: "",
      bdate: "",
      title: ""
    };
  },
  setup() {
    const route = useRoute();

    const store = useStore();

    //let vector = computed(() => store.getters.patient);

    return { route, store };
  },
  methods: {
    asg: async function () {
      const res = await fetch(
        "http://192.168.100.231:8000/apiV1/persons/" + this.route.params.id
      );
      const patient = await res.json();
      console.log(patient);
      this.cc = patient.person.person_id;
      this.name = patient.person.name;
      this.sname = patient.person.second_name;
      this.lname = patient.person.lastname;
      this.slname = patient.person.second_lastname;
     
    },

    update: async function () {
      this.v$.$validate(); // checks all inputs

      if (!this.v$.$error) {
        let obj = {
          person_id: this.cc,
          name: this.name,
          second_name: this.sname,
          lastname: this.lname,
          second_lastname: this.slname,
          age: this.bdate,
        };

        console.log(obj.person_id);

        // STORE MUTATION

        this.$store.dispatch("EDIT_PATIENT", obj);
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
      name: {
        required,
        minLength: minLength(1),
        maxLength: maxLength(15),
        alpha,
      },
      sname: {
        required,
        minLength: minLength(1),
        maxLength: maxLength(15),
        alpha,
      },
      lname: {
        required,
        minLength: minLength(1),
        maxLength: maxLength(15),
        alpha,
      },
      slname: {
        required,
        minLength: minLength(1),
        maxLength: maxLength(15),
        alpha,
      },
      bdate: { required, minLength: minLength(1), maxLength: maxLength(15) },
    };
  },
  mounted() {
    M.AutoInit();
    this.store.dispatch("GET_DOCTOR", this.route.params.id);
    this.asg();
  },
};
</script>

<template>
  <div class="center align-items center container">
    <div class="col s12">
      <div class="card pink darken-1">
        <div class="card-content white-text">
          <span class="card-title">Actualizacion de datos</span>
          <p>
            En este apartado podra actualizar sus datos a excepcion de su
            cedula.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="container align-items center">
      <div class="container">
        <div class="col s12 container">
          <div class="card row">
            <div class="col s12">
              <h5 class="indigo-text">ACTUALIZAR DATOS</h5>
            </div>
            <div class="col s12">
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">person</i>
                  <input
                    disabled
                    id="cedula"
                    type="text"
                    class="validate"
                    v-model="cc"
                  />
                  <h6 class="indigo white-text" v-if="v$.cc.$error">
                    {{ v$.cc.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">face</i>
                  <input
                    id="ru_name"
                    type="text"
                    class="validate"
                    v-model="name"
                  />
                  <h6 class="indigo white-text" v-if="v$.name.$error">
                    {{ v$.name.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">account_circle</i>
                  <input
                    id="ru_sname"
                    type="text"
                    class="validate"
                    v-model="sname"
                  />
                  <h6 class="indigo white-text" v-if="v$.sname.$error">
                    {{ v$.sname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">group</i>
                  <input
                    id="ru_lastname"
                    type="text"
                    class="validate"
                    v-model="lname"
                  />
                  <h6 class="indigo white-text" v-if="v$.lname.$error">
                    {{ v$.lname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">account_circle</i>
                  <input
                    id="ru_slastname"
                    type="text"
                    class="validate"
                    v-model="slname"
                  />
                  <h6 class="indigo white-text" v-if="v$.slname.$error">
                    {{ v$.slname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">date_range</i>
                  <input
                    placehholder="borndate"
                    type="date"
                    class="validate"
                    v-model="bdate"
                  />
                  <label for="first_name">Fecha de nacimiento</label>
                  <h6 class="indigo white-text" v-if="v$.bdate.$error">
                    {{ v$.bdate.$errors[0].$message }}
                  </h6>
                </div>

                <div class="center">
                  <button
                    class="btn purple darken-4"
                    type="submit"
                    @click="update"
                  >
                    ACTUALIZAR DATOS
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

