<template>
<!--INDEX NAVBAR WITH NORMAL OPTIONS FOR MAIN PAGE-->

  <nav class="container">
    <div class="nav-wrapper indigo darken-3">
      <a href="#!" class="brand-logo"
        ><i class="material-icons">spa</i>Ehealth</a
      >
      <ul class="right hide-on-med-and-down">
        <li><i class="material-icons">home</i></li>
        <li>
          <a href="#"><router-link to="/">Inicio</router-link> </a>
        </li>
        <li><i class="material-icons">app_registration</i></li>

        <li>
          <a href="#"><router-link to="/register">Registro</router-link> </a>
        </li>
        <li><i class="material-icons">login</i></li>

        <li>
          <a href="#"><router-link to="/login">Ingreso</router-link> </a>
        </li>
      </ul>
    </div>
  </nav>
</template>
