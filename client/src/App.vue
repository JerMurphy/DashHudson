<template>
  <v-app>
    <Header/>
    <v-content class="margins">
        <v-row>
          <v-col cols="12" sm="4">
            <v-card class="pa-2" outlined tile>
              <FamilyList v-on:view="view"/>
            </v-card>
          </v-col>
          <v-col cols="12" sm="8">
            <v-card class="pa-2" outlined tile>
             <FamilyMember v-if="currentPerson.first_name" v-bind:person="currentPerson"/>
             <div v-if="!currentPerson.first_name">
               <p>Click on a person to the side to view more details</p>
             </div>
            </v-card>
          </v-col>
        </v-row>
    </v-content>
  </v-app>
</template>

<script>
import Header from './components/Header';
import FamilyList from './components/FamilyList';
import FamilyMember from './components/FamilyMember';

export default {
  name: 'App',
  components: {
    Header,
    FamilyList,
    FamilyMember
  },
  data: () => ({
    //
    currentPerson: {}
  }),
  methods:{
    view(person){
      this.currentPerson = person;
    }
  }
};
</script>

<style scoped>
  .margins{
    margin-left: 1%;
    margin-right: 1%
  }
</style>
