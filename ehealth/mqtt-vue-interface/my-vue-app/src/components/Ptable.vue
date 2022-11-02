<script>

import { reactive, computed } from "vue";

export default {
  props: ['cc'],
  
  data() {
    return {
      nothing: {}
      
    };
  },

  methods: {
    get: async function(){
      console.log(this.cc)
      const ans = await fetch(
        "http://localhost:8000/apiV1/vitals/" + this.cc
      );
      
      const con = await ans.json();
      
      this.nothing = con;     
      
      console.log(con)
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
            
            <DataTable :value="vitals" :scrollable="true" scrollHeight="400px" :loading="loading">
                <Column field="name" header="Numero" style="min-width:200px"></Column>
                <Column field="country.name" header="Temperatura" style="min-width:200px"></Column>
                <Column field="representative.name" header="F.Cardiaca" style="min-width:200px"></Column>
                <Column field="status" header="F.Respiratoria" style="min-width:200px"></Column>
                
                <Column field="country.name" header="Oxigeno" style="min-width:200px"></Column>
                <Column field="representative.name" header="Peso" style="min-width:200px"></Column>
                <Column field="status" header="Altura" style="min-width:200px"></Column>
                
                <Column field="country.name" header="Anio" style="min-width:200px"></Column>
                <Column field="representative.name" header="Mes" style="min-width:200px"></Column>
                <Column field="status" header="Dia" style="min-width:200px"></Column>
                <Column field="status" header="Hora" style="min-width:200px"></Column>
                
                
            </DataTable>
        </div>
  

  
</template>