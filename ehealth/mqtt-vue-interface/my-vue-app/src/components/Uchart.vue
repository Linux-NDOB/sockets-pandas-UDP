<script setup>
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const id = route.params.id;

let temp = [];
let ox = [];
let fc = [];
let fr = [];
let tit = [];

async function getAll() {
  const res = await fetch("http://localhost:8000/apiV1/vitals/" + route.params.id);
  const patients = await res.json();

  const vitals = patients.vitals;

  let i = 0;

  for( i = 0; i < vitals.length; i++){
	temp.push(vitals[i].temperature);
	ox.push(vitals[i].oxigen);
	fc.push(vitals[i].heart_rate);
	fr.push(vitals[i].resp_rate);
	tit.push(vitals[i].register_number);

  }
};

let basicData = {
  labels: tit,
  datasets: [
    {
      label: "Temperatura",
      backgroundColor: "#42A5F5",
      data: temp,
    },
	{
      label: "Oxigeno",
      backgroundColor: "#f44336",
      data: ox,
    },
	{
      label: "R.Cardiaca",
      backgroundColor: "#e91e63",
      data: fc,
    },
	{
      label: "F.Respiratoria",
      backgroundColor: "#9c27b0",
      data: fr,
    },
    
  ],
};

onMounted(()=>{
	getAll();
})
</script>

<template>

  

  <Chart type="line" :data="basicData" />
</template>