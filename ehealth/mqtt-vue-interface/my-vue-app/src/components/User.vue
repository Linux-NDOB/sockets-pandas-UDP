<script>
import Ubar from "/src/components/Bars/Ubar.vue";
import { useRouter, useRoute } from 'vue-router'
import HelloWorld from "/src/components/HelloWorld.vue";
import Footer from "/src/components/Bars/Footer.vue";


export default {
  components: {
    Ubar,
    Footer,
    HelloWorld,
  },
  data(){
    return {
      data : {
        name : ''
      }     
    };
  },
  setup(){
    
    const router = useRouter();
    const route = useRoute(); 
       
  },
  methods: {
    get : async function (){
    const res = await fetch(
      "http://localhost:8000/apiV1/persons/" + this.$route.params.id
    );

    const us = await res.json();
  
    this.data.name = us.person.name;
},
    
  },
  mounted(){
    M.AutoInit();
    
    this.get();
    
    
},
  
};
</script>

<template>

    <Ubar/>
                 
      <div class="section white">
        <div class="row container">
          <h2 class="header">Hola {{data.name}}</h2>
          <p class="grey-text text-darken-3 lighten-3">Esta es la interfaz principal de la aplicacion, en ella solo desde deslizarte entre ellas dando click a las secciones que quieras consultar.</p>
        </div>
      </div>
      
      <HelloWorld/>

    <Footer/>
</template>