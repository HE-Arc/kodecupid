<template>
    <v-bottom-navigation v-model="value" :bg-color="color()" mode="shift" grow>

        <v-btn :to="{ name: 'search' }">
            <v-icon aria-hidden="false">
                mdi-magnify
            </v-icon>
            <span>Recherche</span>
        </v-btn>

        <v-btn :to="{ name: 'match' }">
            <v-icon aria-hidden="false">
                mdi-robot-love
            </v-icon>
            <span>Matchs</span>
        </v-btn>

        <v-btn :to="{ name: 'account-show' }">
            <v-icon aria-hidden="false">
                mdi-account
            </v-icon>
            <span>Ton compte</span>
        </v-btn>
        
        <v-btn @click="logout()" v-if="checkAuth()">
            <v-icon aria-hidden="false">
                mdi-logout
            </v-icon>
            <span>Déconnexion</span>
        </v-btn>
        <v-btn v-else :to="{ name: 'signin' }">
            <v-icon aria-hidden="false">
                mdi-login
            </v-icon>
            <span>Connexion</span>
        </v-btn>
    </v-bottom-navigation>

</template>

<script>
import router from '@/router';
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
        },
        logout() {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            router.push({ name: 'signin', replace: true, force: true });
        },
        checkAuth() {
            return localStorage.getItem('accessToken') !== null;
        }

    }
};
</script>