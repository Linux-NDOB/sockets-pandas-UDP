<script>
import { reactive, computed, ref } from "vue";
import { useStore } from "vuex";
import { useVuelidate } from "@vuelidate/core";
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
      v$: useVuelidate(),
    };
  },
  setup() {
    let modal2 = ref("blank");

    let cedula = ref('');

    let contrasenia = ref('');

    let mostrar = false;

    const store = useStore();

    let vector = computed(() => store.getters.doctors);

    const state = reactive({
      cc: "",
      name: "",
      sname: "",
      lname: "",
      slname: "",
      bdate: "",
      uname: "",
      email: "",
      password: "",
      title: "",
    });

    const rules = computed(() => {
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
        title: {
          required,
          minLength: minLength(1),
          maxLength: maxLength(50),
          alpha,
        },
      };
    });

    const v$ = useVuelidate(rules, state);

    return { state, v$, vector, modal2, cedula, contrasenia, mostrar };
  },
  methods: {
    ...mapActions({
      get: "GET_DOCTORS",
    }),

    cleanFields() {
      this.state.cc = "";

      this.state.name = "";

      this.state.sname = "";

      this.state.lname = "";

      this.state.slname = "";

      this.state.bdate = "";

      this.state.title = "";
    },

    isEmpty: async function () {
      const res = await fetch(
        "http://localhost:8000/apiV1/doctors/" + this.state.cc
      );
      const us = await res.json();

      let empty = false;

      us.hasOwnProperty("msg") ? (empty = true) : (empty = false);

      //console.log("MSG ? :" + empty);

      return empty;
    },

    isRegistered: async function () {
      this.isEmpty();

      const isEmpty = await this.isEmpty();

      //console.log(": " + isEmpty);

      let registered = false;

      if (isEmpty == true) {
        registered = false;

        console.log("is empty");
      } else if (isEmpty == false) {
        console.log("is not empty");

        const res = await fetch(
          "http://localhost:8000/apiV1/doctors/" + this.state.cc
        );
        const us = await res.json();

        us.hasOwnProperty("msg") ? (registered = false) : (registered = true);
      }

      return registered;
    },
    send2: async function () {
      let isRegistered = await this.isRegistered();

      this.v$.$validate(); // checks all inputs

      if (!this.v$.$error && !isRegistered) {
        let name = this.state.name;

        let username = name.substring(0, 3) + this.state.lname.substring(0, 3);

        this.state.uname = username;

        this.state.email =
          this.state.name.substring(0, 3) +
          this.state.lname.substring(0, 3) +
          "@gmail.com";

        this.state.password =
          this.state.name.substring(0, 3) + this.state.cc.substring(0, 3);

        //console.log(this.state.uname, this.state.email, this.state.password);

        // STORE MUTATION

        this.$store.dispatch("ADD_DOCTOR", this.state);

        // CHANGING BUTTON CLASS

        this.modal2 = "modal-trigger";

        this.cedula = this.state.cc;

        this.contrasenia = this.state.password;

        this.mostrar = true;

        this.cleanFields();

      } else {
        M.toast({ html: "USUARIO REGISTRADO O DATOS INCORRECTOS", classes: "red" });
      }
    },
  },

  computed: {
    ...mapGetters({
      vector: "doctors",
    }),
  },
  mounted() {
    M.AutoInit();
    this.get();
  },
};
</script>

<template>

  <div v-if="mostrar" class=" center align-items center container ">
    <div class="col s12 ">
      <div class="card red darken-4">
        <div class="card-content white-text">
          <span class="card-title">REGISTRADO CON EXITO!</span>
          <p>Porfavor utilice estas credenciales para iniciar sesion.</p>
          <p>CEDULA: {{cedula}}</p>
          <p>CONTRASENIA: {{contrasenia}}</p>
        </div>
      </div>
    </div>
  </div>

  <div v-else class=" center align-items center container ">
    <div class="col s12 ">
      <div class="card indigo darken-1">
        <div class="card-content white-text">
          <span class="card-title">Datos de inicio de sesion</span>
          <p>Una vez complete satisfactoriamente el registro apareceran las credenciales de inicio de sesion en este apartado.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="container align-items center">
      <div class="container">
        <div class="col s12 container">
          <div class="row card">
            <div class="col s12">
              <h5 class="indigo-text ">REGISTRO DE DOCTORES</h5>
            </div>
            <div class="col s12">
              <div class="row">
                <div class="input-field col s12">
                  <i class="material-icons prefix">list_alt</i>
                  <input
                    placeholder="Titulos"
                    id="cedula"
                    type="text"
                    class="validate"
                    v-model="state.title"
                  />
                  <h6 class="indigo white-text" v-if="v$.title.$error">
                    {{ v$.title.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons  prefix">person</i>
                  <input
                    placeholder="Cedula del doctor"
                    id="cedula"
                    type="text"
                    class="validate"
                    v-model="state.cc"
                  />
                  <h6 class="indigo white-text" v-if="v$.cc.$error">
                    {{ v$.cc.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">face</i>

                  <input
                    placeholder="Nombre"
                    id="ru_name"
                    type="text"
                    class="validate"
                    v-model="state.name"
                  />
                  <h6 class="indigo white-text" v-if="v$.name.$error">
                    {{ v$.name.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">person</i>

                  <input
                    placeholder="Segundo nombre"
                    id="ru_sname"
                    type="text"
                    class="validate"
                    v-model="state.sname"
                  />
                  <h6 class="indigo white-text" v-if="v$.sname.$error">
                    {{ v$.sname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">group</i>

                  <input
                    placeholder="Apellido"
                    id="ru_lastname"
                    type="text"
                    class="validate"
                    v-model="state.lname"
                  />
                  <h6 class="indigo white-text" v-if="v$.lname.$error">
                    {{ v$.lname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">person</i>

                  <input
                    placeholder="Segundo apellido"
                    id="ru_slastname"
                    type="text"
                    class="validate"
                    v-model="state.slname"
                  />
                  <h6 class="indigo white-text" v-if="v$.slname.$error">
                    {{ v$.slname.$errors[0].$message }}
                  </h6>
                </div>

                <div class="input-field col s12">
                  <i class="material-icons prefix">date_range</i>

                  <input
                    placeholder="Fecha de nacimiento"
                    id="ru_bdate"
                    type="date"
                    class="validate"
                    v-model="state.bdate"
                  />
                  <label for="first_name">Fecha de nacimiento</label>
                  <h6 class="indigo white-text" v-if="v$.bdate.$error">
                    {{ v$.bdate.$errors[0].$message }}
                  </h6>
                </div>

                <div class="center">
                  <button
                    class="btn purple darken-4"
                    :class="modal2"
                    href="#modal2"
                    name="doctor"
                    type="submit"
                    @click="send2"
                  >
                    Registrarse
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

