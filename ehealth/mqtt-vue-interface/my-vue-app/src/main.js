import { createApp } from 'vue'
//import './style.css'
import 'materialize-css/dist/css/materialize.min.css'
//import 'material-design-icons/iconfont/material-icons.css'

import router from "./router";
import store from "./store";

import App from './App.vue'

import PrimeVue from "primevue/config";
import InputText from "primevue/inputtext";
import 'primevue/resources/primevue.min.css'
import 'primevue/resources/themes/bootstrap4-light-blue/theme.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css';
// elements
import Knob from 'primevue/knob';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';     //optional for column grouping
import Row from 'primevue/row';    
import Chart from 'primevue/chart';
import Calendar from 'primevue/calendar';
import Checkbox from 'primevue/checkbox';
import Password from 'primevue/password';


createApp(App).use(router).use(store).use(PrimeVue)
  .component("Knob", Knob)
  .component("Menubar", Menubar)
  .component("InputText", InputText)
  .component("Button", Button)
  .component("DataTable", DataTable)
  .component("Column", Column)
  .component("ColumnGroup", ColumnGroup)
  .component("Row", Row)
  .component("Chart", Chart)
  .component("Calendar", Calendar)
  .component("Checkbox", Checkbox)
  .component("Password", Password)
  .mount('#app')
