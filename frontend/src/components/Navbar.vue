<script setup>
</script>

<template>
    <v-bottom-navigation v-model="value" :bg-color="color" mode="shift" grow>
        <v-btn :to="{name: 'home'}">
            <v-icon aria-hidden="false">
                mdi-home
            </v-icon>
            <span>Home</span>
        </v-btn>

        <v-btn :to="{name: 'account'}">
            <v-icon aria-hidden="false">
                mdi-account
            </v-icon>
            <span>Account</span>
        </v-btn>

        <v-btn :to="{name: 'signin'}">
            <v-icon aria-hidden="false">
                mdi-account
            </v-icon>
            <span>Signin</span>
        </v-btn>

        <v-btn :to="{name: 'about'}">
            <v-icon>mdi-information</v-icon>
            <span>About</span>
        </v-btn>
    </v-bottom-navigation>

</template>

<script>
export default {
  data: () => ({ value: 1 }),

  computed: {
    color() {
      switch (this.value) {
        case 0: return 'blue-grey'
        case 1: return 'teal'
        default: return 'blue-grey'
      }
    },
  },

  name: 'Navbar',
}
</script>