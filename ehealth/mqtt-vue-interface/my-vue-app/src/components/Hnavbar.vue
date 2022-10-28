<script setup>

</script>


<template>

<div  class="grid">

    <Menubar
    class="fixed top-0 left-0 px-2 py-2 w-full font-bold bg-indigo-700 border-0"
  >
    <template #start>
      <img
        alt="logo"
        src="https://cdn-icons-png.flaticon.com/512/2438/2438018.png"
        height="40"
        class="mr-2 ml-4"
      />
      <Button
        label="EHEALTH"
        class="p-button-text text-white text-xl font-bold"
      />
    </template>
    <template #end>
      <Button
        icon="pi pi-home"
        label="Inicio"
        class="p-button-text text-white text-xl font-medium"
      />
      <Button
        icon="pi pi-sign-out"
        label="Sobre Nosotros"
        class="p-button-text text-white text-xl font-medium"
      />
      <Button
        icon="pi pi-user-plus"
        label="Iniciar sesion"
        class="p-button-text text-white text-xl font-medium"
      />
    </template>
  </Menubar>

</div>
</template>

<style lang="scss" scoped>
    Button{
        font-family: 'Lato', sans-serif;
    }

    label{
        font-style: bold;
    }
    </style>
