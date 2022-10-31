<script>
import Ibar from "/src/components/Ibar.vue";

import Footer from "/src/components/Footer.vue";

import {reactive, computed} from 'vue';
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import {
  required,
  minLength,
  maxLength,
  sameAs,
} from "@vuelidate/validators";
import { mapActions, mapGetters } from "vuex";

export default{
    components: {
    Footer,
    Ibar,
  },
  data() {    
    return {  
        v$: useVuelidate(),    
        email: '',      
        password: ''
    }  
},
    setup(){
        let vector = computed(() => store.getters.patients);
        const state = reactive({      
            cc: '',      
            
            password: '',          
        });    
        
        const rules = computed(() => {  
            return {    
                cc: { required, minLength: minLength(1), maxLength: maxLength(15), },    
                password: { required, minLength: minLength(1), maxLength: maxLength(15), },      
   
            }});
         
        
        const v$ = useVuelidate(rules, state)    
        
        return { state, v$, vector }
    },
    methods: {    
        send() {      
            this.v$.$validate() // checks all inputs      
            if (!this.v$.$error) {        // if ANY fail validation        
                alert('Form successfully submitted.')      } 
                else {        
                    alert('Form failed validation')      
                }    
            },  
        },   
    
    computed: {
      ...mapGetters({
        vector: "patients",
      })
    },

    validations() {    
        return {      
            email: { required },      
            password: { required },       
        }  
    },
}

</script>

<template>
    <Ibar />
  
      <br />
      <div class="divider"></div>
      <br />
      
      <div class="container">
        <div class="row container align-items center">
          <div class="col s12">
            <h4 class="white-text indigo container">
              Formulario de Inicio de Sesion
            </h4>
          </div>
          <div class="divider"></div>
    
          <div class="col s12 m4 l2"><p></p></div>
          <div class="col s12 m4 l8">
            <input id="last_name" type="text" v-model="state.cc" />
            <label for="last_name">Cedula</label>
            <h6 class="red white-text" v-if="v$.cc.$error">
              {{ v$.cc.$errors[0].$message }}
            </h6>
          </div>
          <div class="col s12 m4 l2"><p></p></div>
    
          <div class="col s12"></div>
          <br />
    
          <div class="col s12 m4 l2"><p></p></div>
          <div class="col s12 m4 l8">
            <input type="password" v-model="state.password" />
            <label for="password">Contrasenia</label>
            <h6 class="red white-text" v-if="v$.password.$error">
              {{ v$.password.$errors[0].$message }}
            </h6>
          </div>
          <div class="col s12 m4 l2"><p></p></div>
        </div>
  
        <div class="col s12 align-items center ">
          <a class="red-text"
            >Pulse aqui si ha olvidado su contrasenia</a
          >
        </div>
    
        <div class="col s12 align-items center">
          <a class="waves-effect waves-light btn indigo white-text" @click="send"
            >Entrar</a
          >
        </div>
      </div>

      
  
      <div class="divider"></div>
  
      <br />
    
    <Footer />

    
  </template>