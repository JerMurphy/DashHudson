<template>
  <div class="hello">
    <v-app-bar app>
      <v-toolbar-side-icon>
        <v-img src="../assets/tree_logo.jpeg" height="60" width="50"/>
      </v-toolbar-side-icon> 
      <v-toolbar-title class="headline">Family Tree</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .headline {
    margin-left: 10px;
  }
</style>
