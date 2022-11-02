<script>
import Ibar from "/src/components/Ibar.vue";
import Footer from "/src/components/Footer.vue";
import { reactive, computed, ref } from "vue";
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import { required, minLength, maxLength, sameAs, numeric, alpha, alphaNum } from "@vuelidate/validators";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    Footer,
    Ibar,
  },
  data() {
    return {
      v$: useVuelidate(),
    };
  },
  setup() {
       
    let modal = 'blank'; 
    
    const store = useStore();
    
    let vector = computed(() => store.getters.patients);
    
    const state = reactive({
      cc: "",
      name: "",
      sname: "",
      lname: "",
      slname: "",
      bdate: "",
      uname: '',
      email: '',
      password: '',
    });

    const rules = computed(() => {
      return {
        cc: { required, minLength: minLength(1), maxLength: maxLength(15), numeric },
        name: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        sname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        lname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        slname: { required, minLength: minLength(1), maxLength: maxLength(15), alpha },
        bdate: { required, minLength: minLength(1), maxLength: maxLength(15) },
      };
    });

    const v$ = useVuelidate(rules, state);

    return { state, v$, vector };
    
  },
  methods: {
    ...mapActions({
      
      get: "GET_PATIENTS",
      
    }),
    isRegistered(){ 
      
      let registered = false;
      
      let vector2 = this.vector.persons;
      
      vector2.forEach((el,i) => {
        
        console.log(el.person_id);
        console.log(this.state.cc);
        
        if (String(el.person_id) == this.state.cc){
          
          registered = true;   
          M.toast({html: 'Ya registrado', classes: 'indigo'});
          
        } else {
          
          registered = false;
          M.toast({html: 'Para registrar'});
          
        } 
      });
      
      return registered;  
      
    },
    send() {
      
      this.isRegistered(); 
      
      this.v$.$validate(); // checks all inputs
      
      if (!this.v$.$error && !this.isRegistered()) {
        
        let name = this.state.name;
        
         let username = name.substring(0, 3) + this.state.lname.substring(0, 3);
         
         this.state.uname = username;
         
         this.state.email = this.state.name.substring(0, 3) + this.state.lname.substring(0, 3) + '@gmail.com';
         this.state.password = this.state.name.substring(0, 3) + this.state.cc.substring(0, 3);
         
         console.log(this.state.uname, this.state.email, this.state.password);
         
         // STORE MUTATION
         
         this.$store.dispatch("ADD_PATIENT", this.state);
         
         // CHANGING BUTTON CLASS
         
         this.modal = 'modal-trigger';
         
         // CLEANING FIELDS
         
         this.state.cc = '';
         
         this.state.name = '';
         
         this.state.sname = '';
         
         this.state.lname = '';
         
         this.state.slname = '';
         
         this.state.bdate = '';
                
      } else {
        
         M.toast({html: 'Rellene el formulario correctamente', classes: 'red'});
         
      }
    },
  },

  computed: {
    ...mapGetters({
      
      vector: "patients",
      
    }),
  },
  mounted() {
    
    M.AutoInit();
    
    this.get();
    
  }, 
};
</script>

<template>
  <Ibar />
  <br />

  <div class="container">
    <div class="container align-items center">
      
        <!-- Modal Trigger -->
 

  <!-- Modal Structure -->
  <div id="modal1" class="modal modal-fixed-footer">
    <div class="modal-content">
      <h4>Datos de Inicio de Sesion</h4>
     
      <p>Porfavor anote los siguientes datos</p>
      
      <div class='container align-items center'>
      <p>CEDULA: {{ state.cc }} </p>
      <p>CONTRASENIA: {{ state.password }}</p>
      </div>
    </div>
    <div class="modal-footer">
      <a href="#!" class="modal-close waves-effect waves-green btn-flat">Aceptar</a>
    </div>
  </div>
                
      <div id="test-swipe-1" class="col s12 white row">
        <div>
          <br />

          <div class="container">
            <div class="col s12 container">
              <div class="row">

                <div class="col s12">
                  <h4 class="white-text indigo ">
                    Formulario de Registro
                  </h4>
                </div>

                <div class="col s12">
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        placeholder="Cedula del paciente"
                        id="cedula"
                        type="text"
                        class="validate"
                        v-model="state.cc"
                      />
                      <h6 class="red white-text" v-if="v$.cc.$error">
                        {{ v$.cc.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Nombre"
                        id="ru_name"
                        type="text"
                        class="validate"
                        v-model="state.name"
                      />
                      <h6 class="red white-text" v-if="v$.name.$error">
                        {{ v$.name.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo nombre"
                        id="ru_sname"
                        type="text"
                        class="validate"
                        v-model="state.sname"
                      />
                      <h6 class="red white-text" v-if="v$.sname.$error">
                        {{ v$.sname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Apellido"
                        id="ru_lastname"
                        type="text"
                        class="validate"
                        v-model="state.lname"
                      />
                      <h6 class="red white-text" v-if="v$.lname.$error">
                        {{ v$.lname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo apellido"
                        id="ru_slastname"
                        type="text"
                        class="validate"
                        v-model="state.slname"
                      />
                      <h6 class="red white-text" v-if="v$.slname.$error">
                        {{ v$.slname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Fecha de nacimiento"
                        id="ru_bdate"
                        type="date"
                        class="validate"
                        v-model="state.bdate"
                      />
                      <label for="first_name">Fecha de nacimiento</label>
                      <h6 class="red white-text" v-if="v$.bdate.$error">
                        {{ v$.bdate.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="center">
                      <button
                        class="btn purple darken-4"
                        :class='modal'
                        href="#modal1"
                        name="doctor"
                        type="submit"
                        @click="send"
                      >
                        Registrarse
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>   
    </div>
  </div>

  <Footer />
</template>