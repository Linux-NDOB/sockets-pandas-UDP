<template>
  <div>
      <table class="centered striped" id="datatable">
      <thead>
        <tr>
          <th>C.C</th>
          <th>Nombre</th>
          <th>S.Nombre</th>
          <th>Apellido</th>
          <th>S.Apellido</th>
          <th>F.Nacimiento</th>      
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in products" :key="item.person_id">
          <td>{{ item.person_id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.second_name }}</td>
          <td>{{ item.lastname }}</td>
          <td>{{ item.second_lastname }}</td>
          <td>{{ item.age }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import axios from "axios";
import $ from "jquery";
export default {
  mounted() {
    axios.get("http://192.168.100.231:8000/apiV1/patients/" ).then((response) => {
      this.products = response.data.persons;
      $("#datatable").DataTable();
      console.log(response.data);
    });
  },
  data: function () {
    return {
      products: [],
    };
  },
  watch: {
  products(val) {
    $('#datatable').DataTable().destroy();
    this.$nextTick(()=> {
      $('#datatable').DataTable()
    });
   }
  }
};
</script>
