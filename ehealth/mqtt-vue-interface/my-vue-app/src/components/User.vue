<script setup>
import Ubar from "/src/components/Ubar.vue";

import { onMounted } from "@vue/runtime-core";

import Ibar from "/src/components/Ibar.vue";
import Footer from "/src/components/Footer.vue";

onMounted(()=>{
    M.AutoInit();
    
  });

</script>

<template>

    <Ubar/>
    <div class="container">
        <ul id="slide-out" class="sidenav">
          <li><div class="user-view">
            <div class="background">
              <img src="https://images.pexels.com/photos/1502286/pexels-photo-1502286.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">
            </div>
            <a href="#user"><img class="circle" src="https://images.pexels.com/photos/5490142/pexels-photo-5490142.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"></a>
            <a href="#name"><span class="white-text name"></span></a>
            <a href="#email"><span class="white-text email"></span></a>
          </div></li>
          <li><a class="subheader">Pacientes</a></li>
          <li><a href="/actualizar_paciente/{{ data.person.person_id }}"><i class="material-icons">sync_alt</i>Actualizar datos</a></li> 
          <li><a href="/login/"><i class="material-icons">logout</i>Cerrar sesion</a></li>  
        </ul>
      
      
      
      </div>
            
      
      
      
      <div class="section white">
        <div class="row container">
          <h2 class="header">Hola  </h2>
          <p class="grey-text text-darken-3 lighten-3">Parallax is an effect where the background content or image in this case, is moved at a different speed than the foreground content while scrolling.</p>
        </div>
      </div>
      
      
      
      
      <div class="container">
        <ul id="tabs-swipe-demo" class="tabs">
          <li class="tab col s3 "><a class="active blue white-text" href="#test-swipe-1">Datos de Paciente</a></li>
          <li class="tab col s3"><a class="purple white-text" href="#test-swipe-2">Registros de paciente</a></li>
          <li class="tab col s3"><a class="cyan white-text" href="#test-swipe-3">Datos de Registros</a></li>
          <li class="tab col s3"><a class="teal white-text" href="#test-swipe-4">Diagnosticos</a></li>
        </ul>
        <div id="test-swipe-1" class="col s12 blue">
      
          <h4 class="indigo center white-text">Datos de Paciente</h4>
        <ul class="collection">
      
          <li class="collection-item avatar">
            <i class="material-icons circle indigo">person</i>
            <span class="title">Datos</span>
            <p> <br>
                CC:  <br>
               Fecha de nacimiento: 
            </p>
            
          </li>
      
        </ul>
      </div>
        </div>
      
      
        <div id="test-swipe-2" class="col s12 white">
      
          <h4 class="purple center white-text container">Registros de Paciente</h4>
      
      
      <div class="container striped">
        <table class="table">
            <thead>
                <tr>
                    <th>#Registro</th>
                    <th>Oxigeno</th>
                    <th>Pulso</th>
                    <th>Temperatura</th>
                    <th>Respiracion</th>
                    <th>Peso</th>
                    <th>Altura</th>
                </tr>
            </thead>
      
      
            <tbody>
                
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td> kg</td>
                <td> cm</td>
                <tr/>
                
            </tbody>
        </table>
      </div>
      
        </div>
        <div id="test-swipe-3" class="col s12 white">
          <h4 class="blue center white-text container">Datos de Registros</h4>
      
      
      <div class="container striped">
        <table class="table">
            <thead>
                <tr>
                    <th>#Registro</th>
                    <th>Año</th>
                    <th>Mes</th>
                    <th>Dia</th>
                    <th>Hora</th>
                </tr>
            </thead>
      
      
            <tbody>
                
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
      
                <tr/>
                
            </tbody>
        </table>
      </div>
        </div>
      
      
      <div id="test-swipe-4" class="col s12 white">
      
        <h4 class="teal center white-text container">Diagnosticos del Paciente</h4>
      
      <div class="container striped">
        <table class="table">
            <thead>
                <tr>
                    <th>Numero Diagnostico</th>
                    <th>Cedula Doctor</th>
                    <th>Cedula Paciente</th>
                    <th>Diagnostico</th>
                </tr>
            </thead>
      
      
            <tbody>
                
                <td></td>
                <td></td>
                <td></td>
                <td></td>
      
                <tr/>
               
            </tbody>
        </table>
      </div>
      
      </div>
      
      <div class="fixed-action-btn floating-action-btn">
        <a class="btn-floating btn-large red btn-large pulse indigo sidenav-trigger" data-target="slide-out">
          <i class="large material-icons">menu</i>
        </a>
      </div>

    <Footer/>
</template>