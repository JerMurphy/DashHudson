import Vuex from 'vuex';
import Vue from 'vue';
import members from './modules/members.js';
import connections from './modules/connections';

//Load Vuex
Vue.use(Vuex);

//Create store
export default new Vuex.Store({
    modules: {
        members,
        connections
    }
})