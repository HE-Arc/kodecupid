<template>
    <v-bottom-navigation v-model="value" :bg-color="color()" mode="shift" grow>
        <v-btn :to="{ name: 'home' }">
            <v-icon aria-hidden="false">
                mdi-home
            </v-icon>
            <span>Home</span>
        </v-btn>

        <v-btn :to="{ name: 'search' }">
            <v-icon aria-hidden="false">
                mdi-magnify
            </v-icon>
            <span>Search</span>
        </v-btn>

        <v-btn :to="{ name: 'match' }">
            <v-icon aria-hidden="false">
                mdi-robot-love
            </v-icon>
            <span>Match</span>
        </v-btn>

        <v-btn :to="{ name: 'account' }">
            <v-icon aria-hidden="false">
                mdi-account
            </v-icon>
            <span>Account</span>
        </v-btn>

        <v-btn :to="{ name: 'signin' }">
            <v-icon aria-hidden="false">
                mdi-account
            </v-icon>
            <span>Signin</span>
        </v-btn>

        <v-btn :to="{ name: 'about' }">
            <v-icon aria-hidden="false">mdi-information</v-icon>
            <span>About</span>
        </v-btn>
    </v-bottom-navigation>

</template>

<script>
export default {
    name: 'Navbar',
    data() {
        return {
            value: 0
        }
    },
    methods: {
        color() {
            switch (this.value) {
                case 0: return 'blue-grey'
                case 1: return 'teal'
                case 2: return 'brown'
                case 3: return 'indigo'
                case 4: return 'orange'
                default: return 'blue-grey'
            }
        }
    }
};
</script>