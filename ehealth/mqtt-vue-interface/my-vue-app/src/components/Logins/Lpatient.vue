<script>
import { reactive, computed } from "vue";
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import {
  required,
  minLength,
  maxLength,
  sameAs,
  numeric,
} from "@vuelidate/validators";
import { mapActions, mapGetters } from "vuex";

export default {
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
      password: "",
    });

    const rules = computed(() => {
      return {
        cc: {
          required,
          minLength: minLength(1),
          maxLength: maxLength(15),
          numeric,
        },
        password: {
          required,
          minLength: minLength(1),
          maxLength: maxLength(15),
        },
      };
    });

    const v$ = useVuelidate(rules, state);

    return { state, v$, vector, store};
  },

  methods: {
    ...mapActions({
      get: "GET_PATIENTS",
    }),

    exists: async function () {
      const res = await fetch(
        "http://192.168.100.231:8000/apiV1/user_accounts/" + this.state.cc
      );
      const us = await res.json();

      let ex = false;

      us.hasOwnProperty("msg") || this.state.cc == ""
        ? (ex = false)
        : (ex = true);

      console.log(this.state.cc);

      return ex;
    },

    valPass: async function () {
      let ex = await this.exists();

      let isValid = false;

      if (ex == true) {
        const res = await fetch(
          "http://192.168.100.231:8000/apiV1/user_accounts/" + this.state.cc
        );

        const us = await res.json();

        this.state.password == us.user_account.user_password
          ? (isValid = true)
          : (isValid = false);

        console.log("Valido: " + isValid);
      } else if (ex == false) {
        isValid = false;
        console.log("Se supone invalid");
      }

      console.log("valPass final:" + isValid);
      return isValid;
    },
    send: async function () {
      let valid = await this.valPass();

      console.log("valid: " + valid);

      this.v$.$validate();

      if (!this.v$.$error && valid == true) {
        let id = this.state.cc;

        // M.toast({ html: "LOGON", classes: "rounded" });

        this.$router.push({ name: "user", params: { id } });
        this.store.dispatch("login"); 
      } else if (valid == false || this.v$.error) {
        M.toast({ html: "DATOS INCORRECTOS", classes: "rounded red" });
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
};
</script>

<template>
  <div class="container align-items">
    <br />
    <div class="row align-items center card">
      <div class="col s12 container">
        <br />

        <h5 class="indigo-text container">CREDENCIALES DEL PACIENTE</h5>

        <br />
      </div>
      <div class="divider"></div>

      <div class="col s12 m4 l2"><p></p></div>

      <div class="input-field col s12 m4 l8">
        <i class="material-icons prefix">face</i>

        <input id="last_name" type="text" v-model="state.cc" />

        <label for="last_name">Cédula</label>
        <h6 class="red white-text" v-if="v$.cc.$error">
          {{ v$.cc.$errors[0].$message }}
        </h6>
      </div>
      <div class="col s12 m4 l2"><p></p></div>

      <div class="col s12"></div>
      <br />

      <div class="col s12 m4 l2"><p></p></div>

      <div class="input-field col s12 m4 l8">
        <i class="material-icons prefix">key</i>

        <input type="password" v-model="state.password" />
        <label for="password">Contraseña</label>
        <h6 class="red white-text" v-if="v$.password.$error">
          {{ v$.password.$errors[0].$message }}
        </h6>
      </div>

      <div class="col s12 m4 l2"><p></p></div>
    </div>

    <div class="col s12 align-items center">
      <a class="waves-effect waves-light btn indigo white-text" @click="send"
        >Entrar</a
      >
    </div>
  </div>
</template>
