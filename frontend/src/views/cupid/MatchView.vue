<template>
    <v-container>
        <v-row v-if="match.length > 0" class="d-flex flex-row">
            <v-col cols="6" v-for="user in match">
                <PeopleCard :user=user />
            </v-col>
        </v-row>
        <v-row v-else>
            <v-col>
                <v-container class="d-flex flex-column align-center">
                    <v-label>Aucune connexion n'a encore été trouvée</v-label>
                    <v-icon color="red" class="my-4 text-h1">mdi-heart-broken</v-icon>
                    <v-label>Mais ne vous découragez pas !</v-label>
                    <v-label>Vous finirez par trouver cette connection spéciale ;)</v-label>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import PeopleCard from '@/components/PeopleCard.vue';

import { store } from '@/store';
import { setError } from '@/store';
import axios from 'axios';

const match = ref([]);

const fetchUserMatch = async () => {
    // TODO not implemented yet -> will be done in the future
    // axios.get(store.routes['USER_MATCH'], {}).catch((error) => {
    //     console.error(error.response.data);
    //     store.error.value = error.response.data;
    //     return error
    // })
    //     .then(response => {
    //         match.value = response.data;
    //     });
};

onMounted(() => {
    fetchUserMatch();
});

</script>