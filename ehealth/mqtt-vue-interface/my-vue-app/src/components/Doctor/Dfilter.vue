<script>

import { reactive, computed } from "vue";

export default {
  props: ['cc'],
  
  data() {
    return {
      patients: {}
      
    };
  },

  methods: {
    get: async function(){
      const ans = await fetch("http://localhost:8000/apiV1/patients/");
      
      const con = await ans.json();
      
      this.patients = con.persons;     

      console.log(con.persons)
      
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
            <h5 class='indigo white-text center'>LISTADO DE PACIENTES</h5>
            
            <DataTable :value="patients" :scrollable="true" scrollHeight="400px" :loading="false">
                <Column field="person_id" header="Cedula" style="min-width:200px"></Column>
                <Column field="name" header="Nombre" style="min-width:200px"></Column>
                <Column field="second_name" header="S. Nombre" style="min-width:200px"></Column>
                <Column field="lastname" header="Apellido" style="min-width:200px"></Column>
                <Column field="second_lastname" header="S. Apellido" style="min-width:200px"></Column>
                <Column field="age" header="F. Nacimiento" style="min-width:200px"></Column>

                
            </DataTable>
        </div>
  
</template>
