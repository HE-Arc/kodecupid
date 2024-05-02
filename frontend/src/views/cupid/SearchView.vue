<template>
    <v-container v-if="userx">
        <v-row justify="center">
            <v-col class="d-inline-flex align-center">
                <v-btn @click="like" class="h-100 mr-2 bg-like"><v-icon>mdi-thumb-up</v-icon></v-btn>
                <PeopleCard elevation="4" class="flex-grow-1" :user=user :details=true />
                <v-btn @click="dislike" class="h-100 ml-2 bg-dislike"><v-icon>mdi-thumb-down</v-icon></v-btn>
            </v-col>
        </v-row>
    </v-container>
    <v-container v-else>
        <v-row>
            <v-col>
                <p>Hé, tu le croirais ça ? Plus un seul profil à liker sur KodeCupid 😱 !
                    C'est comme si t'avais vidé tout le stock de jus de Mynthos et qu'il ne reste plus qu'un verre vide.
                </p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <p>
                    T'as tout cliqué, tout swipé, et là, c'est le désert digital.
                    Mais bon, au moins tu continues de faire connaissance avec ton clavier, c'est pas si mal, non ?</p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-img cover class="rounded-lg" src="/jdg-joueur-du-grenier.gif"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>

import { onMounted, ref } from 'vue';
import PeopleCard from '@/components/PeopleCard.vue';

import { ApiClient } from '@/clients/apiClient.js';

const user = ref({});
const userx = ref(false);

const like = async () => {
    const liked = await ApiClient.likeUser(user.value.id);
    if (liked) {
        fetchUser();
    }
};

const dislike = async () => {
    fetchUser();
};


const fetchUser = async () => {
    const fetchedUser = await ApiClient.getUserRandom();
    userx.value = fetchedUser;
    if (!fetchedUser) {
        return;
    }

    const fetchedTags = await ApiClient.getUserTags(fetchedUser.id);

    if (fetchedUser.pfp) {
        const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);
        if (fetchedUserPfp) {
            user.value.pfp_src = fetchedUserPfp;
        }
    }

    const fetchedPictures = await ApiClient.getPicturesByUser(fetchedUser.id);

    if (fetchedPictures) {
        user.value.pictures = fetchedPictures;
    }

    user.value.id = fetchedUser.id;
    user.value.username = fetchedUser.username;
    user.value.bio = fetchedUser.bio;
    user.value.sex = fetchedUser.sex;
    user.value.pfp = fetchedUser.pfp;
    user.value.tags = fetchedTags;
}


onMounted(() => {
    fetchUser();
});

</script>