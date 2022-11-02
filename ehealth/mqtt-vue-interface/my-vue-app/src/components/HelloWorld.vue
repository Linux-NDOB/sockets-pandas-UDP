<script setup>
import { ref, onMounted } from "vue";
import Ibar from "/src/components/Ibar.vue";
import Footer from "/src/components/Footer.vue";
import Ptable from "/src/components/Ptable.vue";
import { useRouter, useRoute } from 'vue-router'

// VARS
const router = useRouter()
const route = useRoute()
const id = route.params.id;
const client = new Paho.MQTT.Client("172.19.0.1", 9001, "futon");

// SENSORS
let jhrate = ref(0);
let jrrate = ref(0);
let joxigen = ref(0);
let jtemp = ref(0);
//let temp = ref(0);
//let temp = ref(0);

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({ onSuccess: onConnect });

// called when the client connects
function onConnect() {
  
  // Once a connection has been made, make a subscription and send a message.
  console.log("Connected");
  client.subscribe("ehealth");
  //const message = new Paho.MQTT.Message(`{"client": "futon", "state": "connected"}`);
  //const message = new Paho.MQTT.Message(`
  //{
  // "temperature": 30,
  // "oxigen": 95,
  //"hearth_rate": 150
  //}`);

  //message.destinationName = "ehealth";
  //client.send(message);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:" + responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  let payload = message.payloadString;
  let json = JSON.parse(payload);

  let { hrate, rrate, oxigen, temp } = json;

  jhrate.value = hrate;
  jrrate.value = rrate;
  joxigen.value = oxigen;
  jtemp.value = temp;

};

onMounted(()=>{
    M.AutoInit();
  });

</script>

<template>
  
   <div class="row container">
    <div class="col s12">
      
      <ul class="tabs">
        <li class="tab col s3"><a href="#test1" class='indigo white-text active'>Toma de datos</a></li>
        <li class="tab col s3"><a href="#test2" class='indigo white-text'>tabla de datos</a></li>
        <li class="tab col s3"><a href="#test3" class='indigo white-text'>grafico de datos</a></li>
        <li class="tab col s3"><a href="#test4" class='indigo white-text'>Datos de paciente</a></li>
      </ul>
    </div>
    <div id="test1" class="col s12">
    <div class="row align-items center">
      <br>
      <h5 class='indigo container white-text container'>TOMA DE DATOS</h5>
      <br>
      <br>
      
      <div class='col s3'>
      <Knob class="" readonly v-model="jtemp" :min="0" :max="100 " />
      <a class='white-text btn indigo pulse'>Temperatura</a>
      </div>
      
      <div class='col s3'>
      <Knob class="" readonly v-model="jhrate" :min="0" :max="200" />
      <a class='white-text btn indigo pulse'>Frecuencia Cardiaca</a>
      </div>
      
      <div class='col s3'>
      <Knob class="" readonly v-model="jrrate" :min="0" :max="200" />
      <a class='white-text btn indigo pulse'>Fre. Respiratoria</a>
      </div>
      
      <div class='col s3'>
      <Knob class="" readonly v-model="joxigen" :min="0" :max="150" />
      <a class='white-text btn indigo pulse'>Oxigeno</a>
      </div>   
      
      <div class='col s12'>
      <br>
      <a class='btn indigo darken-4' >Guardado</a>
      </div>
         
    </div>
    </div>
    
    <div id="test2" class="col s12">
    <Ptable cc = 'id'/>
    </div>
    
    <div id="test3" class="col s12">Test 3</div>
    
    <div id="test4" class="col s12">Test 4</div>
    
  </div>
  
</template>
