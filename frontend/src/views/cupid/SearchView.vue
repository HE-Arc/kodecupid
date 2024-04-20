<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <PeopleCard :user=user :pfp=pfp />
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-container class="d-flex justify-space-between">
                    <v-btn @click="like" class="bg-like"><v-icon>mdi-thumb-up</v-icon></v-btn>
                    <v-btn @click="dislike" class="bg-dislike"><v-icon>mdi-thumb-down</v-icon></v-btn>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>

import { onMounted, ref } from 'vue';
import PeopleCard from '@/components/PeopleCard.vue';

import { ApiClient } from '@/clients/apiClient.js';

const user = ref({});
const pfp = ref({});

const like = async () => {
    console.log(user.value);
    const liked = await ApiClient.likeUser(user.value.id);
    if (liked) {
        fetchUser();
    }
};

const dislike = async () => {
    fetchUser();
};


const fetchUser = async () => {
    const fetchedUser = await ApiClient.getUser();
    const fetchedTags = await ApiClient.getUserTags(fetchedUser.id);
    const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);

    if (fetchedUserPfp) {
        pfp.value = fetchedUserPfp;
    }

    user.value.username = fetchedUser.username;
    user.value.bio = fetchedUser.bio;
    user.value.looking_for = fetchedUser.looking_for;
    user.value.pfp = fetchedUser.pfp;
    user.value.tags = fetchedTags;
}


onMounted(() => {
    fetchUser();
});

</script>