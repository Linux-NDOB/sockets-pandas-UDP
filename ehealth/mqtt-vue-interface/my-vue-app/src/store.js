"use strict";
import router from "./router";
import { createStore } from 'vuex';

export default createStore({

  state: {
    patients:[],
    doctors: []

  },

  getters: {
    patients: (state) => state.patients,
    doctors: (state) => state.doctors,
  },

  actions: {

    GET_PATIENTS: async function ({ commit }) {
      const res = await fetch("http://localhost:8000/apiV1/patients/");

      const patients = await res.json();
      
      console.log(patients);

      commit("SET_PATIENTS", patients);
    },

    ADD_PATIENT: async function ({ commit }, array) {
      const res = await fetch("http://localhost:8000/apiV1/patients/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(array),
      });
      const user = await res.json();

      console.log(user);

      M.toast({ html: "REGISTERED", classes: "rounded" });

      commit("SET_PATIENTS", user);
    },

    EDIT_PATIENT: async function ({ commit }, object) {
      fetch("http://localhost:3000/users/" + object.id, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: object.id,
          username: object.username,
          email: object.email,
          password: object.password,
        }),
      });

      const res = await fetch("http://localhost:3000/users");

      const cart = await res.json();

      commit("SET_USERS", cart);

      this.$router.push("/admin");
    },


    GET_DOCTORS: async function ({ commit }) {
      const res = await fetch("http://localhost:8000/apiV1/patients/");

      const patients = await res.json();

      commit("SET_PATIENTS", patients);
    },

    ADD_DOCTOR: async function ({ commit }, array) {
      const res = await fetch("http://localhost:8000/apiV1/patients/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(array),
      });
      const user = await res.json();

      console.log(user);

      M.toast({ html: "REGISTERED", classes: "rounded" });

      commit("SET_PATIENTS", user);
    },

    EDIT_DOCTOR: async function ({ commit }, object) {
      fetch("http://localhost:3000/users/" + object.id, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: object.id,
          username: object.username,
          email: object.email,
          password: object.password,
        }),
      });

      const res = await fetch("http://localhost:3000/users");

      const cart = await res.json();

      commit("SET_USERS", cart);

      this.$router.push("/admin");
    },
    
  },

  mutations: {
    SET_PATIENTS: function (state, patients) {
      state.patients = patients;
    },
    SET_DOCTORS: function (state, doctors) {
      state.doctors = doctors;
    },
  },
  
  
})

