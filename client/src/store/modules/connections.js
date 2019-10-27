import axios from 'axios';

const state = {
    connections: {}
};

const getters = {
    allConnections: (state) => state.connections
};

const actions = {
    async getConnections({ commit }){
        const response = await axios.get('http://localhost:5000/connections');
        const obj = {};

        //puts them into a object sorted by personID to easily display in front end
        response.data.forEach(element => {
            if(obj[element.from_person_id]){
                obj[element.from_person_id].push(element)
            }else{
                obj[element.from_person_id] = []
                obj[element.from_person_id].push(element)
            }
        });
        commit('setConnections', obj);
    },
    async addConnection({ commit }, obj){
        const response = await axios.post('http://localhost:5000/connections', obj);
        commit('newConnection', response.data)
    }
};

const mutations = {
    setConnections: (state,connections) => (state.connections = connections),
    newConnection(state,connection){
        if(state.connections[connection.from_person_id]){
            state.connections[connection.from_person_id].push(connection)
        }else{
            state.connections[connection.from_person_id] = []
            state.connections[connection.from_person_id].push(connection)
        }
    } 
};

export default {
    state,
    getters,
    actions,
    mutations
}