import { createApp } from 'vue'
import App from './App.vue'
import naive from "naive-ui";
import axios from 'axios'
import VueAxios from 'vue-axios'



//createApp(App).use(naive).mount('#app')

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend

const app = createApp(App)
app.use(naive)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)
app.mount('#app')
