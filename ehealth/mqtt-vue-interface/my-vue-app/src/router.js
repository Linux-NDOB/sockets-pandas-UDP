import { createRouter, createWebHistory } from "vue-router";

import Home from "./components/Home.vue";
import About from "./components/About.vue";
import Login from "./components/Login.vue";
import User from "./components/User.vue";
import Doctor from "./components/Home.vue";
import Metrics from "./components/About.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/user", component: User },
  { path: "/doctor", component: Doctor },
  { path: "/login", component: Login },
  { path: "/metrics", component: Metrics },



];

const history = createWebHistory();

const router = createRouter({
  history,
  routes,
});

export default router;

