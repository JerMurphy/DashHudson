import axios from 'axios';

const state = {
    connections: []
};

const getters = {
    allConnections: (state) => state.connections
};

const actions = {
    async getConnections({ commit }){
        const response = await axios.get('http://localhost:5000/connections');
        commit('setConnections', response.data);
    },
    async addConnection({ commit }, obj){
        const response = await axios.post('http://localhost:5000/connections', obj);
        commit('newConnection', response.data)
    }
};

const mutations = {
    setConnections: (state,connections) => (state.connections = connections),
    newConnection: (state,connection) => (state.connections.push(connection))
};

export default {
    state,
    getters,
    actions,
    mutations
}