<script>

import { reactive, computed } from "vue";

export default {
  props: ['cc'],
  
  data() {
    return {
      vitals: {}
      
    };
  },

  methods: {
    get: async function(){
      console.log(this.cc)
      const ans = await fetch(
        "http://localhost:8000/apiV1/vitals/" + this.cc
      );
      
      const con = await ans.json();
      
      this.vitals = con.vitals;     
      
      console.log(this.vitals)
    }
  },

  mounted() {
    M.AutoInit();
    this.get();   
  },
};
</script>

<template>
  
<div class="card">
            <h5 class='indigo white-text center'>REGISTROS DEL PACIENTE</h5>
            
            <DataTable :value="vitals" :scrollable="true" scrollHeight="400px" :loading="false">
                <Column field="register_number" header="Numero de Registro" style="min-width:200px"></Column>
                <Column field="temperature" header="Temperatura(C)" style="min-width:200px"></Column>
                <Column field="heart_rate" header="F.Cardiaca(BPM)" style="min-width:200px"></Column>
                <Column field="resp_rate" header="F.Respiratoria(RPM)" style="min-width:200px"></Column>
                
                <Column field="oxigen" header="Oxigeno(%)" style="min-width:200px"></Column>
                <Column field="weight" header="Peso(Kg)" style="min-width:200px"></Column>
                <Column field="height" header="Altura(cm)" style="min-width:200px"></Column>
                
                <Column field="year_taken" header="Anio" style="min-width:200px"></Column>
                <Column field="month_taken" header="Mes" style="min-width:200px"></Column>
                <Column field="day_taken" header="Dia" style="min-width:200px"></Column>
                <Column field="hour_taken" header="Hora" style="min-width:200px"></Column>
                       
            </DataTable>
        </div>
  
</template>