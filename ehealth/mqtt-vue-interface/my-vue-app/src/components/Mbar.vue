<script setup>


</script>

<template>
    <div class="container">

        <nav>
            <div class="nav-wrapper indigo" >
              <a href="#!" class="brand-logo"><i class="material-icons">spa</i>Ehealth</a>
              <ul class="right hide-on-med-and-down">
                <li><a href="#"><i class="material-icons">person</i></a></li>
                <li><a href="#"><i class="material-icons">keyboard_backspace</i></a></li>
                
              </ul>
            </div>
          </nav>

          <ul id="slide-out" class="sidenav">
            <li><div class="user-view">
              <div class="background">
                <img src="images/office.jpg">
              </div>
              <a href="#user"><img class="circle" src="images/yuna.jpg"></a>
              <a href="#name"><span class="white-text name">John Doe</span></a>
              <a href="#email"><span class="white-text email">jdandturk@gmail.com</span></a>
            </div></li>
            <li><a href="#!"><i class="material-icons">cloud</i>First Link With Icon</a></li>
            <li><a href="#!">Second Link</a></li>
            <li><div class="divider"></div></li>
            <li><a class="subheader">Subheader</a></li>
            <li><a class="waves-effect" href="#!">Third Link With Waves</a></li>
          </ul>

          <div class="fixed-action-btn">
            <a data-target="slide-out" class="btn-floating btn-large indigo sidenav-trigger">
              <i class="large material-icons">dashboard</i>
            </a>
          </div>
          <br>
          <br>
          
    </div>
</template>