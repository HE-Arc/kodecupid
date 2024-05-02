<template>
    <v-container>
        <v-row v-if="match.length > 0">
            <v-col v-for="user in match">
                <PeopleCard @click="showConversation(user.id)" :user=user min-width="250"/>
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
import { onMounted, ref} from 'vue';
import { ApiClient } from '@/clients/apiClient.js';
import PeopleCard from '@/components/PeopleCard.vue';

import router from '@/router';

const match = ref([]);

const fetchUserMatch = async () => {
    match.value = await ApiClient.getUserMatches();

    if (!match.value) {
        return;
    }

    match.value.forEach(async (user) => {

        if (user.pfp) {
            const fetchedUserPfp = await ApiClient.getPicture(user.pfp);
            if (fetchedUserPfp) {
                user.pfp_src = fetchedUserPfp;
            }
        }

        const fetchedTags = ApiClient.getUserTags(user.id);
        if (fetchedTags) {
            user.tags = fetchedTags;
        }

    });
};

onMounted(() => {
    fetchUserMatch();
});


const showConversation = (id) => {
    router.push({ name: 'conversation', params: { id: id } , replace: true, force: true });
}

</script>