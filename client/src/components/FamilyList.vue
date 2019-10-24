<template>
  <v-container class="grey lighten-5">
   <h3 style="text-align: center"> Family Members </h3>
    <br/>
    <AddMember/>
    <div class="margins">
        <h5>Family</h5>
        <v-list>
            <v-list-item two-line v-for="person in allMembers" :key="person.id">
                <v-list-item-content>
                    <v-list-item-title>{{person.first_name}} {{person.last_name}}</v-list-item-title>
                    <v-list-item-subtitle>{{person.email}}</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                    <v-btn icon>
                        <v-icon  v-on:click="view(person)" color="grey lighten-1">mdi-chevron-right</v-icon>
                    </v-btn>
                </v-list-item-action>
            </v-list-item>
        </v-list>
    </div>
  </v-container>
</template>

<script>
import AddMember from './AddMember';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'FamilyList',
  components: {
    AddMember
  },
  data: () => ({
  }),
  methods: {
      ...mapActions(['getMembers']),
      view(person){
          this.$emit('view', person)
      }
  },
  created(){
      this.getMembers();
  },
  computed: mapGetters(['allMembers'])

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .margins {
        margin-top: 5%;
    }
</style>
