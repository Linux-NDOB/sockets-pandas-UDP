import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router'
import store from './store'



// PrimeVue
import PrimeVue from 'primevue/config';

// Themes and more
import 'primevue/resources/themes/md-light-indigo/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'
import '/node_modules/primeflex/primeflex.css'
// Components
import Menubar from 'primevue/menubar';


createApp(App).use(store).use(router).use(PrimeVue).component('Menubar', Menubar).mount('#app')
