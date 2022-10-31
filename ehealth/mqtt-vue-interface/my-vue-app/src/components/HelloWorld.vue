<script setup>
import { ref } from "vue";

//defineProps({
//msg: String
//})

// <h1>{{ msg }}</h1>
// Create a client instance

const client = new Paho.MQTT.Client("172.19.0.1", 9001, "futon");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({ onSuccess: onConnect });

// called when the client connects
function onConnect() {
  //const data = {
  //temperature: "30",
  //oxigen: "95",
  //hearth_rate: "150",
  //};

  //const info = JSON.stringify(data);

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

let jhrate = ref(0);
let jrrate = ref(0);
let joxigen = ref(0);
let jtemp = ref(0);
//let temp = ref(0);
//let temp = ref(0);

// called when a message arrives
function onMessageArrived(message) {
  let payload = message.payloadString;
  let json = JSON.parse(payload);

  let { hrate, rrate, oxigen, temp } = json;

  jhrate.value = hrate;
  jrrate.value = rrate;
  joxigen.value = oxigen;
  jtemp.value = temp;

  //console.log("Message", hrate, rrate, oxigen, tempp);

  console.log(hrate, rrate, oxigen, temp);

  //return temperature;
}

//console.log(temp);

// Menubar items
</script>

<template>
  
  <div class="container">
    

    <div class="flex flex align-items-center justify-content-center ">
      <Knob class="mr-3" v-model="jtemp" :min="0" :max="100" />
      <Knob class="mr-3" v-model="jhrate" :min="0" :max="200" />
      <Knob class="mr-3" v-model="jrrate" :min="0" :max="200" />
      <Knob class="mr-3" v-model="joxigen" :min="0" :max="150" />
    </div>

    <div class="flex flex align-items-center justify-content-center">
      <div
        class="m-3 p-2 flex-initial flex align-items-center justify-content-center bg-blue-500 font-base text-white m-1 px-1 py-1 "
      >
        Temperatura
      </div>
      <div
        class=" m-3 flex-initial flex align-items-center justify-content-center bg-teal-500 font-base text-white m-1 px-1 py-1 "
      >
        F.Cardiaca
	</div>
      <div
        class="m-3 flex-initial flex align-items-center justify-content-center  bg-yellow-500 font-base text-white m-1 px-1 py-1 "
      >
       Respiracion
       </div>
      <div
        class="m-3 flex-initial flex align-items-center justify-content-center bg-red-500 font-base text-white m-2 px-1 py-1"

      >
       Oxigeno
       </div>
    </div>
  </div>

</template>
