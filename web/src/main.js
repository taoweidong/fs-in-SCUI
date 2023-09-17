import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/display.css'
import scui from './scui'
import i18n from './locales'
import router from './router'
import store from './store'
import App from './App.vue'
import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'
import FastCrud from './fast-crud/index.js';
import 'view-ui-plus/dist/styles/viewuiplus.css'
import ViewUIPlus from 'view-ui-plus'

const app = createApp(App);
app.use(FastCrud)
app.use(VXETable)
app.use(store);
app.use(router);
app.use(ElementPlus);
app.use(i18n);
app.use(scui);
app.use(ViewUIPlus)

//挂载app
app.mount('#app');
