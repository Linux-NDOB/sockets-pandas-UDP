<script setup>
import Dbar from "/src/components/Dbar.vue";

import { onMounted } from "@vue/runtime-core";


import Footer from "/src/components/Footer.vue";

onMounted(()=>{
    M.AutoInit();   
  });

</script>

<template>
    <Dbar/>

    <div class="container">

        <ul id="slide-out" class="sidenav">
          <li><div class="user-view">
            <div class="background">
              <img src="https://images.pexels.com/photos/1502286/pexels-photo-1502286.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">
            </div>
            <a href="#user"><img class="circle" src="https://images.pexels.com/photos/5490142/pexels-photo-5490142.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"></a>
            <a href="#name"><span class="white-text name">x</span></a>
            <a href="#email"><span class="white-text email">x</span></a>
          </div></li>
          <li><a class="subheader">Pacientes</a></li>
          <li><a href="/listado_pacientes/{{ data.person.person_id }}"><i class="material-icons">person_search</i>Listado de pacientes</a></li>
      
         
          <li><div class="divider"></div></li>
          <li><a class="subheader">Doctor</a></li>
          <li><a href="/actualizar_doctor/{{data.person.person_id}}"><i class="material-icons">sync_alt</i>Actualizar datos</a></li>  
          <li><a href="/login/"><i class="material-icons">logout</i>Cerrar sesion</a></li>
        </ul>
            
      </div>
            
         
      <div class="section white">
        <div class="row container">
          <h2 class="header">Hola  Dr(a) </h2>
          <p class="grey-text text-darken-3 lighten-3">Parallax is an effect where the background content or image in this case, is moved at a different speed than the foreground content while scrolling.</p>
        </div>
      </div>
      
           
      <div class="fixed-action-btn floating-action-btn">
        <a class="btn-floating btn-large red btn-large pulse indigo sidenav-trigger" data-target="slide-out">
          <i class="large material-icons">menu</i>
        </a>
      </div>

    <Footer/>

    </template>