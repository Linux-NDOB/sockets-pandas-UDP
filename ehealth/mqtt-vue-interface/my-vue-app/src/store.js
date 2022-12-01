"use strict";
import { createStore } from 'vuex'; 

export default createStore({

    state: {
        patients: [],
        doctors: [],
        vitals: [],
        patient: [],
        doctor: [],
        logged : 'false',
    },

    getters: {
        patients: (state) => state.patients,
        doctors: (state) => state.doctors,
        vitals: (state) => state.vitals,
        patient: (state) => state.patient,
        doctor: (state) => state.doctor,
        logged: (state) => state.logged,
    },

    actions: {

        login: function ({ commit }) {
            commit('SET_LOGGED', true);
        },
        logout: function ({ commit }) {
            commit('SET_LOGGED', false);
            
        },    
        GET_PATIENTS: async function ({ commit }) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/patients/");
            const patients = await res.json();
            commit("SET_PATIENTS", patients);
        },

        GET_PATIENT: async function ({ commit }, id) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/patients/" + id);
            const patient = await res.json();
            commit("SET_PATIENT", patient);
        },

        ADD_PATIENT: async function ({ commit }, array) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/patients/", {
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

        EDIT_PATIENT: async function ({ commit }, object) {
            console.log('hi', object)
            fetch("http://192.168.100.231:8000/apiV1/persons/" + object.person_id, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({

                    person_id: object.person_id,

                    name: object.name,

                    second_name: object.second_name,

                    lastname: object.lastname,

                    second_lastname: object.second_lastname,

                    age: object.age,

                }),
            });

            M.toast({ html: "DATOS ACTUALIZADOS CORRECTAMENTE", classes: "rounded green" });

        },


        GET_DOCTORS: async function ({ commit }) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/doctors/");

            const doctors = await res.json();

            commit("SET_DOCTORS", doctors);

            console.log(doctors.persons);
        },

        GET_DOCTOR: async function ({ commit }, id) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/persons/" + id);
            const doc = await res.json();
            commit("SET_DOCTOR", doc);
        },

        ADD_DOCTOR: async function ({ commit }, array) {
            const res = await fetch("http://192.168.100.231:8000/apiV1/doctors/", {
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

        EDIT_DOCTOR: async function ({ commit }, array) {
            console.log(array.person_id)
            fetch("http://192.168.100.231:8000/persons/" + array.person_id, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({

                    person_id: array.person_id,

                    name: array.name,

                    second_name: array.second_name,

                    lastname: array.lastname,

                    second_lastname: array.second_lastname,

                    age: array.age,

                }),
            });

            const res = await fetch("http://192.168.100.231:3000/persons/" + array.cc);

            const doctor = await res.json();

            commit("SET_DOCTOR", doctor);
        },
    },

    mutations: {
        SET_PATIENTS: function (state, patients) {
            state.patients = patients;
        },
        SET_DOCTORS: function (state, doctors) {
            state.doctors = doctors;
        },
        SET_PATIENT: function (state, patient) {
            state.patient = patient;
        },
        SET_DOCTOR: function (state, doctor) {
            state.doctor = doctor;
        },
        SET_LOGGED: function (state, logged) {
            state.logged = logged;
        },
    },
})



