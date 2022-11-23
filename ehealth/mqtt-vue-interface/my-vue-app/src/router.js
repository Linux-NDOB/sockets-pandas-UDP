import { createRouter, createWebHistory } from "vue-router";

import Index from "./components/Index/Index.vue";

import Register from "./components/User/Register.vue";

import Login from "./components/User/Login.vue";

import User from "./components/User.vue";

import Doctor from "./components/Doctor/Mdoctor.vue";

import Ptable from "./components/Ptable.vue";

const routes = [
  { path: "/", component: Index },

  { path: "/login", component: Login },

  { path: "/register", component: Register },

  { path: "/user", component: User },

  {
    path: "/user:id",
    name: 'user',
    component: User
  },

  {
    path: "/doctor:id",
    name: 'doctor',
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

export default router;

