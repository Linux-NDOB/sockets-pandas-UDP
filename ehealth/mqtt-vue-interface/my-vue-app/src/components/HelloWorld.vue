<script setup>
import { ref, onMounted } from "vue";
import Ptable from "/src/components/Ptable.vue";
import Uchart from "/src/components/Uchart.vue";
import { useRouter, useRoute } from "vue-router";
import Chart from "primevue/chart";

// VARS
const router = useRouter();
const route = useRoute();
const id = route.params.id;
const client = new Paho.MQTT.Client("172.19.0.1", 9001, "futon");

// SENSORS
let jhrate = ref(0);
let jrrate = ref(0);
let joxigen = ref(0);
let jtemp = ref(0);
//let weight = ref(0);
//let height = ref(0);
let weight = 90;
let height = 175;

// DATE
let day = new Date().getDate(); // Get the day as a number (1-31)
//let day = new Date().getDay() + 1           // Get the weekday as a number (0-6)
let year = new Date().getFullYear(); // Get the four digit year (yyyy)
let hour = new Date().getHours(); // Get the hour (0-23)
//new Date().getMilliseconds()  // Get the milliseconds (0-999)
//new Date().getMinutes()       // Get the minutes (0-59)
let month = new Date().getMonth(); // Get the month (0-11)
//new Date().getSeconds()       // Get the seconds (0-59)
//new Date().getTime()          // Get the time (milliseconds since January 1, 1970)

// GENERAL CHART

const primeChart = ref();

let limit = 0;

function getRandomInt(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min) + min)
}

const addData = () => {
  const chart = primeChart.value.chart;
  chart.data.labels.push((limit += 1));
  chart.data.datasets[0].data.push(jtemp.value);
  chart.data.datasets[1].data.push(joxigen.value);
  chart.data.datasets[2].data.push(jhrate.value);
  chart.data.datasets[3].data.push(jrrate.value);
  chart.update();
};

let basicData = {
  labels: [],
  datasets: [
    {
      label: "Temperatura",
      backgroundColor: "#42A5F5",
      data: [],
    },
    {
      label: "Oxigeno",
      backgroundColor: "#f44336",
      data: [],
    },
    {
      label: "R.Cardiaca",
      backgroundColor: "#e91e63",
      data: [],
    },
    {
      label: "F.Respiratoria",
      backgroundColor: "#9c27b0",
      data: [],
    },
  ],
};

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
}

async function send() {
  if (
    jhrate.value > 1 &&
    jrrate.value > 1 &&
    joxigen.value > 1 &&
    jtemp.value > 1
  ) {
    const res = await fetch("http://localhost:8000/apiV1/vitals/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        patient: id,

        oxigen: joxigen.value,

        heart_rate: jhrate.value,

        temperature: jtemp.value,

        resp_rate: jrrate.value,

        weight: weight,

        height: height,

        day_taken: day,

        year_taken: year,

        month_taken: month,

        hour_taken: hour,
      }),
    });
    const sded = await res.json();

    console.log(sded);

    M.toast({ html: "DATOS REGISTRADOS", classes: "rounded green" });
  } else {
    M.toast({ html: "DATOS INVALIDOS", classes: "rounded red" });
  }
}

let timer;

function startTimer() {
  timer = setInterval(function () {
    addData();
  }, 5000);
}

onMounted(() => {
  M.AutoInit();
  startTimer();
});
</script>

<template>
  <div class="row container">
    <div class="col s12">
      <ul class="tabs">
        <li class="tab col s3">
          <a href="#test1" class="indigo white-text active">Toma de datos</a>
        </li>
        <li class="tab col s3">
          <a href="#test2" class="indigo white-text">tabla de datos</a>
        </li>
        <li class="tab col s3">
          <a href="#test3" class="indigo white-text">grafico de datos</a>
        </li>
        <li class="tab col s3">
          <a href="#test4" class="indigo white-text">Datos de paciente</a>
        </li>
      </ul>
    </div>
    <div id="test1" class="col s12">
      <div class="row align-items center">
        <br />
        <h5 class="indigo container white-text container">TOMA DE DATOS</h5>
        <br />
        <br />

        <div class="col s3">
          <Knob class="" readonly v-model="jtemp" :min="0" :max="100" />
          <a class="white-text btn indigo pulse">Temperatura</a>
        </div>

        <div class="col s3">
          <Knob class="" readonly v-model="jhrate" :min="0" :max="200" />
          <a class="white-text btn indigo pulse">Frecuencia Cardiaca</a>
        </div>

        <div class="col s3">
          <Knob class="" readonly v-model="jrrate" :min="0" :max="200" />
          <a class="white-text btn indigo pulse">Fre. Respiratoria</a>
        </div>

        <div class="col s3">
          <Knob class="" readonly v-model="joxigen" :min="0" :max="150" />
          <a class="white-text btn indigo pulse">Oxigeno</a>
        </div>

        <div class="col s12">
          <br />
          <br />
          <a class="btn green" @click="addData">ACTUALIZANDO</a>
        </div>
      </div>

      <Chart ref="primeChart" type="line" :data="basicData" />
    </div>

    <div id="test2" class="col s12">
      <Ptable :cc="id" />
    </div>

    <div id="test3" class="col s12">
      <Uchart />
    </div>

    <div id="test4" class="col s12">Test 4</div>
  </div>
</template>
