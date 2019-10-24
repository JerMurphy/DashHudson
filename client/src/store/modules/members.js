import axios from 'axios';

const state = {
    members: []
};

const getters = {
    allMembers: (state) => state.members
};

const actions = {
    async getMembers({ commit }){
        const response = await axios.get('http://localhost:5000/people');
        commit('setMembers', response.data);
    },
    async addMember({ commit }, obj){
        const response = await axios.post('http://localhost:5000/people', obj);

        commit('newMember', response.data)
    }
};

const mutations = {
    setMembers: (state,members) => (state.members = members),
    newMember: (state,member) => (state.members.push(member))
};

export default {
    state,
    getters,
    actions,
    mutations
}