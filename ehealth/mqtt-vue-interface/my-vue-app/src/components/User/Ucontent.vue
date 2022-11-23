<script setup>
import { ref, onMounted } from "vue";
import Ptable from "/src/components/User/Ptable.vue";
import Uchart from "/src/components/User/Uchart.vue";
import Update from "/src/components/User/Update.vue";
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
const primeT = ref();
const primeO = ref();
const primeFc = ref();
const primeFr = ref();

let limit = 0;
let limitT = 0;
let limitO = 0;
let limitFc = 0;
let limitFr = 0;

const addData = () => {
  joxigen.value = 95;
  jhrate.value = 120;
  jrrate.value = 100;
  jtemp.value = 30;

  const chart = primeChart.value.chart;
  const chartT = primeT.value.chart;
  const chartO = primeO.value.chart;
  const chartFc = primeFc.value.chart;
  const chartFr = primeFr.value.chart;

  chart.data.labels.push((limit += 1));
  chartT.data.labels.push((limitT += 1));
  chartO.data.labels.push((limitO += 1));
  chartFc.data.labels.push((limitFc += 1));
  chartFr.data.labels.push((limitFr += 1));

  chart.data.datasets[0].data.push(jtemp.value);
  chart.data.datasets[1].data.push(joxigen.value);
  chart.data.datasets[2].data.push(jhrate.value);
  chart.data.datasets[3].data.push(jrrate.value);

  chartT.data.datasets[0].data.push(jtemp.value);
  chartO.data.datasets[0].data.push(joxigen.value);
  chartFc.data.datasets[0].data.push(jhrate.value);
  chartFr.data.datasets[0].data.push(jrrate.value);

  chart.update();
  chartT.update();
  chartO.update();
  chartFc.update();
  chartFr.update();
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

let tempData = {
  labels: [],
  datasets: [
    {
      label: "Temperatura",
      backgroundColor: "#42A5F5",
      data: [],
    },
  ],
};

let oxData = {
  labels: [],
  datasets: [
    {
      label: "Oxigeno",
      backgroundColor: "#f44336",
      data: [],
    },
  ],
};

let fcData = {
  labels: [],
  datasets: [
    {
      label: "F.Cardiaca",
      backgroundColor: "#e91e63",
      data: [],
    },
  ],
};

let frData = {
  labels: [],
  datasets: [
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
          <a href="#test2" class="indigo darken-1 white-text">tabla de datos</a>
        </li>
        <li class="tab col s3">
          <a href="#test3" class="indigo darken-2 white-text"
            >grafico de datos</a
          >
        </li>
        <li class="tab col s3">
          <a href="#test4" class="indigo darken-3 white-text"
            >Datos de paciente</a
          >
        </li>
      </ul>
    </div>
    <div id="test1" class="col s12">
      <div class="row align-items center">
        <br />
        <div class="center align-items">
          <div class="col s12">
            <div class="card pink">
              <div class="card-content white-text">
                <i class="material-icons">save</i>

                <span class="card-title">SIGNOS VITALES EN TIEMPO REAL</span>
                <p>
                  Una vez son validados los signos vitales tomados por los
                  sensores el sistema procede a guardarlos para que pueda
                  revisarlos mas tarde, si quiere ver los datos actualizados en
                  la tabla porfavor recargue la pagina.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col s4">
            <Knob class="" readonly v-model="jtemp" :min="0" :max="100" />
            <a class="white-text btn indigo darken-1 pulse">Temperatura(Cº)</a>
          </div>

          <div class="col s4">
            <Knob class="" readonly v-model="jhrate" :min="0" :max="200" />
            <a class="white-text btn indigo darken-2 pulse"
              >Frecuencia Cardíaca(BPM)</a
            >
          </div>

          <div class="col s4">
            <Knob class="" readonly v-model="jrrate" :min="0" :max="200" />
            <a class="white-text btn indigo darken-3 pulse"
              >Fre. Respiratoria(RPM)</a
            >
          </div>
        </div>
        <br />

        <div class="col s4">
          <Knob class="" readonly v-model="joxigen" :min="0" :max="150" />
          <a class="white-text btn indigo darken-4 pulse">Oxígeno(%)</a>
        </div>

        <div class="col s4">
          <Knob class="" readonly v-model="jrrate" :min="0" :max="200" />
          <a class="white-text btn indigo darken-3 pulse">Peso(kg)</a>
        </div>

        <div class="col s4">
          <Knob class="" readonly v-model="joxigen" :min="0" :max="150" />
          <a class="white-text btn indigo darken-4 pulse">Altura(cm)</a>
        </div>

        <div class="col s12">
          <br />
          <br />
        </div>
      </div>

      <div class="center align-items center">
        <div class="col s12">
          <div class="card blue lighten-1">
            <div class="card-content white-text">
              <i class="material-icons">show_chart</i>

              <span class="card-title center"
                >GRAFICA EN TIEMPO REAL DE TODOS LOS SENSORES</span
              >
            </div>
          </div>
        </div>
      </div>

      <Chart ref="primeChart" type="line" :data="basicData" />

      <div class="center align-items center">
        <div class="col s12">
          <div class="card purple lighten-1">
            <div class="card-content white-text">
              <i class="material-icons">show_chart</i>

              <span class="card-title center">GRAFICA DE TEMPERATURA</span>
            </div>
          </div>
        </div>
      </div>

      <Chart ref="primeT" type="line" :data="tempData" />

      <div class="center align-items center">
        <div class="col s12">
          <div class="card red lighten-1">
            <div class="card-content white-text">
              <i class="material-icons">show_chart</i>

              <span class="card-title center">GRAFICA DE OXÍGENO</span>
            </div>
          </div>
        </div>
      </div>

      <Chart ref="primeO" type="line" :data="oxData" />

      <div class="center align-items center">
        <div class="col s12">
          <div class="card pink lighten-1">
            <div class="card-content white-text">
              <i class="material-icons">show_chart</i>

              <span class="card-title center">GRAFICA DE F.CARDIACA</span>
            </div>
          </div>
        </div>
      </div>

      <Chart ref="primeFc" type="line" :data="fcData" />

      <div class="center align-items center">
        <div class="col s12">
          <div class="card indigo lighten-1">
            <div class="card-content white-text">
              <i class="material-icons">show_chart</i>

              <span class="card-title center">GRAFICA DE F.RESPIRATORIA</span>
            </div>
          </div>
        </div>
      </div>

      <Chart ref="primeFr" type="line" :data="frData" />

      <div class="center align-items center">
        <div class="col s12">
          <div class="card purple lighten-1">
            <div class="card-content white-text">
              <span class="card-title center">COLORES DE LAS LINEAS</span>
              <p>
                Las líneas en la grafica corresponden a: <br />
                Azul: Temperatura. <br />
                Naranja: Oxigeno. <br />
                Rojo: F. Cardiaca. <br />
                Purpura: F.Respiratoria
              </p>
            </div>
          </div>
        </div>
      </div>

      <br />

      <div class="center align-items center container">
        <div class="col s12">
          <div class="card pink lighten-1">
            <div class="card-content white-text">
              <span class="card-title center">ALERTAS</span>
              <p>
                Una vez son validados los signos vitales tomados por el sensor
                el sistema procede a comparar sus signos vitales y verificar si
                se encuentran datos anomalos, de ser el caso aqui apareceran las
                recomendaciones a seguir en base a los documentos cientificos
                mas recientes.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="test2" class="col s12">
      <Ptable :cc="id" />
    </div>

    <div id="test3" class="col s12">
      <Uchart />
    </div>

    <div id="test4" class="col s12">
      <Update />
    </div>
  </div>
</template>
