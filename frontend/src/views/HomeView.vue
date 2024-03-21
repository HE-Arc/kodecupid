<template>
    <v-container >
        <v-row>
            <v-col>
                <v-img cover class="rounded" src="/logo1024.png"></v-img>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-chip> > [SUCCESS] New connection established ! </v-chip>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <p>Bienvenue sur KodeCupid: la plateforme de rencontres dédiée aux ingénieurs informatiques et
                    passionnés de la tech !
                </p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <p>
                    Faites la rencontre de personnes qui partagent votre amour pour la tech et le coding sur KodeCupid. Qui sait, vous pourriez bien trouver votre binôme de code idéal... ou pas ! Mais bon, ça vaut le coup d'essayer.
                </p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-img cover class="rounded-lg" src="/jdg-joueur-du-grenier.gif"></v-img>
            </v-col>
        </v-row>
        <v-row>
            <v-col class="d-flex justify-center">
                <v-btn color="primary" :to="{ name: 'signin' }">Connecte toi</v-btn>
            </v-col>
            <v-col class="d-flex justify-center">
                <v-btn color="primary" :to="{ name: 'signup' }">crée un compte</v-btn>
            </v-col>
        </v-row>
        <v-divider class="my-4"></v-divider>
        <v-row>
            <v-col>
                <h1><v-icon color="blue">mdi-shield-crown</v-icon>L'équipe</h1>
                <v-list>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon> Lucas Gosteli</p>
                    </v-list-item>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon>Danien Tschan</p>
                    </v-list-item>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon>Bruno Tomas</p>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>
    </v-container>

</template>

<script setup>
import { onMounted, ref } from 'vue';
import PeopleCard from '@/components/PeopleCard.vue';

import { store } from '@/store';
import axios from 'axios';

const user = ref({});

const like = async () => {
    axios.put(store.routes['LIKE'], { user_id: store.user.id });
};

const dislike = async () => {
    axios.put(store.routes['DISLIKE'], { user_id: store.user.id });
};

const fetchUser = async () => {
    try {
        user.value = await axios.get(store.routes['USER_SEARCH'], {});
    }
    catch (e) {
        user.value = {
            id: -1,
            name: 'User not found',
            bio: 'User not found',
            avatar: 'https://picsum.photos/170'
        };
    }
};

onMounted(() => {
    fetchUser();
});

</script>