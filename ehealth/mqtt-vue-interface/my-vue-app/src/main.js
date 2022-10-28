import { createApp } from 'vue'
import './style.css'

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

import Carousel from 'primevue/carousel';

import Galleria from 'primevue/galleria';


createApp(App).use(router).use(store).use(PrimeVue)
  .component("Knob", Knob)
  .component("Menubar", Menubar)
  .component("InputText", InputText)
  .component("Button", Button)
  .component("Galleria", Galleria)

  .mount('#app')
