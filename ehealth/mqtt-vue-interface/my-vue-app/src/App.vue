<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import { ref, onMounted } from 'vue';
import M from 'materialize-css';
import Login from './components/Login.vue';

onMounted(() => {
  M.AutoInit() // <div>
});

</script>

<template>
  <router-view></router-view>
  
</template>


