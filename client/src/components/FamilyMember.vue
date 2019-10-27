<template>
  <v-container class="grey lighten-5 margin">
    <p class="display-3">{{person.first_name}} {{person.last_name}}</p>
    <span class="subtitle-3 left"> {{person.email}}</span>
    <v-container class="grey lighten-5">
        <p class="headline"> Connections </p>
        <v-row no-gutters>
            <v-col v-for="connection in allConnections[person.id]" :key="connection.id"  cols="12" sm="4">
                <v-list-item two-line class="spacing">
                <v-list-item-content>
                    <v-list-item-title>{{connection.first_name}} {{connection.last_name}} </v-list-item-title>
                    <v-list-item-subtitle>{{connection.connection_type}}</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
            </v-col>
        </v-row>
    </v-container>
    <v-container class="grey lighten-5">
        <p class="subtitle-1"> Add a connection </p>
        <v-row no-gutters>
            <v-col cols="12" sm="4" class="select">
                <v-select :items="allMembers" item-text="first_name" item-value="id" v-model="connect_to" label="To"></v-select>
            </v-col>
            <v-col cols="12" sm="4">
                <v-select :items="types" v-model="connect_type" label="Type"></v-select>
            </v-col>
            <v-col cols="12" sm="3" class="button">
                <v-btn color="#9bcc71" block v-on:click="connect()"> <span class="btntext">Connect</span></v-btn>
            </v-col>
        </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'FamilyMember',
  props: {
      person: {}
  },
  methods: {
    ...mapActions(['getConnections', 'getMembers', 'addConnection']),
    connect(){
        var obj = {
            connection_type: this.connect_type,
            from_person_id: this.person.id,
            to_person_id: this.connect_to
        };
        this.addConnection(obj);
        this.resetFields()
    },
    resetFields(){
        this.connect_to = {};
        this.connect_type = '';
    }
  },
  created(){
    //BUG, NOT LOADING NEW CONNECTIONS ON FIRST TIME
    this.getConnections();
  },
  computed: mapGetters(['allConnections', 'allMembers']),
  data: () => ({
      types: ['wife', 'husband', 'mother', 'father', "brother", 'sister', 'son', 'daughter', 'friend', 'coworker'],
      connect_to: {},
      connect_type: ''
  })
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .left {
        margin-left: 1%;
    }
    .spacing {
        background-color: white;
        margin-top: 1%;
        margin-right: 1%;
    }
     .select {
        margin-right: 1%;
    }
    .button {
        margin-left:5%;
    }
    .btntext{   
          color: #8C623A
    }
</style>
