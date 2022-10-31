<script>
import Ibar from "/src/components/Ibar.vue";
import Footer from "/src/components/Footer.vue";

import { reactive, computed } from "vue";
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import { required, minLength, maxLength, sameAs, numeric, alpha, alphaNum } from "@vuelidate/validators";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    Footer,
    Ibar,
  },
  data() {
    return {
      v$: useVuelidate(),
    };
  },
  setup() {
    const store = useStore();
    let vector = computed(() => store.getters.patients);
    const state = reactive({
      cc: "",
      name: "",
      sname: "",
      lname: "",
      slname: "",
      bdate: "",
    });

    const rules = computed(() => {
      return {
        cc: { required, minLength: minLength(1), maxLength: maxLength(15), numeric },
        name: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        sname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        lname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        slname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        bdate: { required, minLength: minLength(1), maxLength: maxLength(15), alphaNum },
      };
    });

    const v$ = useVuelidate(rules, state);

    return { state, v$, vector };
  },
  methods: {
    ...mapActions({
      get: "GET_PATIENTS",
    }),
    send() {
      console.log(this.state);

      this.v$.$validate(); // checks all inputs
      if (!this.v$.$error) {
        // if ANY fail validation
        alert("Form successfully submitted.");
      } else {
        alert("Form failed validation");
      }
    },
  },

  computed: {
    ...mapGetters({
      vector: "patients",
    }),
  },
  mounted() {
    M.AutoInit();
    this.get();
  },

  validations() {
    return {
      email: { required },
      password: { required },
    };
  },
};
</script>

<template>
  <Ibar />
  <br />

  <div class="container">
    <div class="container align-items center">
      
      <div id="test-swipe-1" class="col s12 white row">
        <div>
          <br />

          <div class="container">
            <div class="col s12 container">
              <div class="row">

                <div class="col s12">
                  <h4 class="white-text indigo ">
                    Formulario de Registro
                  </h4>
                </div>

                <div class="col s12">
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        placeholder="Cedula del paciente"
                        id="cedula"
                        type="text"
                        class="validate"
                        v-model="state.cc"
                      />
                      <h6 class="red white-text" v-if="v$.cc.$error">
                        {{ v$.cc.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Nombre"
                        id="ru_name"
                        type="text"
                        class="validate"
                        v-model="state.name"
                      />
                      <h6 class="red white-text" v-if="v$.name.$error">
                        {{ v$.name.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo nombre"
                        id="ru_sname"
                        type="text"
                        class="validate"
                        v-model="state.sname"
                      />
                      <h6 class="red white-text" v-if="v$.sname.$error">
                        {{ v$.sname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Apellido"
                        id="ru_lastname"
                        type="text"
                        class="validate"
                        v-model="state.lname"
                      />
                      <h6 class="red white-text" v-if="v$.lname.$error">
                        {{ v$.lname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo apellido"
                        id="ru_slastname"
                        type="text"
                        class="validate"
                        v-model="state.slname"
                      />
                      <h6 class="red white-text" v-if="v$.slname.$error">
                        {{ v$.slname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Fecha de nacimiento"
                        id="ru_bdate"
                        type="date"
                        class="validate"
                        v-model="state.bdate"
                      />
                      <label for="first_name">Fecha de nacimiento</label>
                      <h6 class="red white-text" v-if="v$.bdate.$error">
                        {{ v$.bdate.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="center">
                      <button
                        onclick="register_user()"
                        class="btn purple darken-4"
                        name="doctor"
                        type="submit"
                        @click="send"
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

   
    </div>
  </div>

  <Footer />
</template>