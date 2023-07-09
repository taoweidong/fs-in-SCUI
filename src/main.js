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
import d2CrudX from 'd2-crud-x'

const app = createApp(App);
app.use(d2CrudX, { name: 'd2-crud-x' }) //修改d2CrudX的标签名称
app.use(VXETable)
app.use(store);
app.use(router);
app.use(ElementPlus);
app.use(i18n);
app.use(scui);

//挂载app
app.mount('#app');
