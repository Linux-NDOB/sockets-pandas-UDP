"use strict";
import router from "./router";
import { createStore } from 'vuex';

export default createStore({

    state: {
        patients: [],
        doctors: [],
        vitals: [],
        patient: [],
        doctor: [],
    },

    getters: {
        patients: (state) => state.patients,
        doctors: (state) => state.doctors,
        vitals: (state) => state.vitals,
        patient: (state) => state.patient,
        doctor: (state) => state.doctor,

    },

    actions: {

        GET_PATIENTS: async function({ commit }) {
            const res = await fetch("http://localhost:8000/apiV1/patients/");
            const patients = await res.json();
            commit("SET_PATIENTS", patients);
        },

        GET_PATIENT: async function({ commit }, id) {
            const res = await fetch("http://localhost:8000/apiV1/patients/" + id);
            const patient = await res.json();
            commit("SET_PATIENT", patient);
        },

        ADD_PATIENT: async function({ commit }, array) {
            const res = await fetch("http://localhost:8000/apiV1/patients/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({

                    person_id: array.cc,

                    name: array.name,

                    second_name: array.sname,

                    lastname: array.lname,

                    second_lastname: array.slname,

                    age: array.bdate,

                    username: array.uname,

                    email: array.email,

                    password: array.password,
                }),
            });
            const user = await res.json();

            console.log(user);

            M.toast({ html: "REGISTRADO CORRECTAMENTE", classes: "rounded indigo" });

            commit("SET_PATIENTS", user);
        },

        EDIT_PATIENT: async function({ commit }, object) {
            fetch("http://localhost:3000/patients/" + object.id, {
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


        GET_DOCTORS: async function({ commit }) {
            const res = await fetch("http://localhost:8000/apiV1/doctors/");

            const doctors = await res.json();

            commit("SET_DOCTORS", doctors);
            
            console.log(doctors.persons);
        },

        ADD_DOCTOR: async function({ commit }, array) {
            const res = await fetch("http://localhost:8000/apiV1/doctors/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({

                        person_id: array.cc,

                        name: array.name,

                        second_name: array.sname,

                        lastname: array.lname,

                        second_lastname: array.slname,

                        age: array.bdate,

                        title: array.title,

                        username: array.uname,

                        email: array.email,

                        password: array.password
                    }),
            });
            const user = await res.json();

            M.toast({ html: "REGISTRADO CON EXITO", classes: "rounded indigo" });

            commit("SET_DOCTORS", user);
        },

        EDIT_DOCTOR: async function({ commit }, object) {
            fetch("http://localhost:3000//" + object.id, {
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

            const doctors = await res.json();

            commit("SET_DOCTORS", doctors);

            
        },

    },

    mutations: {
        SET_PATIENTS: function(state, patients) {
            state.patients = patients;
        },
        SET_DOCTORS: function(state, doctors) {
            state.doctors = doctors;
        },
        SET_PATIENT: function(state, patient) {
            state.patient = patient;
        },
        SET_DOCTOR: function(state, doctor) {
            state.doctor = doctor;
        },
    },


})

