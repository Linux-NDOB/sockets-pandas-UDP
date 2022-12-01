//import Vue from 'vue'
//import Router from 'vue-router'
import store from './store';

import { createRouter, createWebHistory } from "vue-router";

import Index from "./components/Index/Index.vue";

import Register from "./components/Registers/Register.vue";

import Login from "./components/Logins/Login.vue";

import User from "./components/User/User.vue";

import Doctor from "./components/Doctor/Mdoctor.vue";

import Ptable from "./components/User/Ptable.vue";



const routes = [
  { path: "/", component: Index },

  { path: "/login", name: "Login", component: Login },

  { path: "/register", component: Register },

  { path: "/user", component: User },

  {
    path: "/user:id",
    name: 'user',
    meta: {
    requiresAuth: true
    },
    component: User
  },

  {
    path: "/doctor:id",
    name: 'doctor',
    meta: {
    requiresAuth: true
    },
    component: Doctor
  },

  { path: "/doctor", component: Doctor },


  { path: "/ptable", component: Ptable },

];


const history = createWebHistory();

const router = createRouter({
  history,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.state.logged == true) {
      next();
    } else {
      next({ name: "Login"});
    }
  } else {
    next();
  }
});


export default router;

