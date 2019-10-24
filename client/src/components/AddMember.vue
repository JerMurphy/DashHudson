<template>
    <div>
    <h5> Add to  your family</h5>
   <v-row>
       <v-col cols=12 sm=6>
           <v-text-field
            v-model="firstname"
            label="First name"
            required
          ></v-text-field>
       </v-col>
       <v-col cols=12 sm=6>
           <v-text-field
            v-model="lastname"
            label="Last name"
            required
          ></v-text-field>
       </v-col>
   </v-row>
   <v-row>
       <v-col cols=12 sm=12>
           <v-text-field
            v-model="email"
            label="Email"
            required
          ></v-text-field>
       </v-col>
   </v-row>
   <v-row>
       <v-btn v-on:click="submit()" small color="#9bcc71" block><span class="submit">Add Member</span></v-btn>
   </v-row>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'AddMember',
  props: {
  },
  methods: {
    ...mapActions(['addMember']),
    submit(){
        if(this.firstname && this.lastname && this.email){
            //validate all fields are there
            var obj = {
                'first_name': this.firstname,
                'last_name': this.lastname,
                'email': this.email
            };
            this.addMember(obj)
            this.resetFields();
        }else{
            alert("Please fill in all fields before submitting.")
        }
    },
    resetFields(){
        this.firstname = '';
        this.lastname = '';
        this.email = '';
    }

  },
  data: () => ({
    //
    firstname: '',
    lastname: '',
    email: ''
  }),
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .margin {
      margin-left: 0px;
  }
  .submit {
      color: #8C623A
  }
</style>
