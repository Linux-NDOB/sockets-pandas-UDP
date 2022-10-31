import { createRouter, createWebHistory } from "vue-router";

import Index from "./components/Index.vue";

import Register from "./components/Register.vue";

import Home from "./components/Home.vue";

import Login from "./components/Login.vue";

import User from "./components/User.vue";

import Doctor from "./components/Doctor.vue";



const routes = [
  { path: "/", component: Index },
  
  { path: "/login", component: Login },

  { path: "/register", component: Register },

  { path: "/home", component: Home },

  { path: "/user", component: User },

  { path: "/doctor", component: Doctor },
  
];

const history = createWebHistory();

const router = createRouter({
  history,
  routes,
});

export default router;

