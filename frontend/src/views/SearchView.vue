<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <PeopleCard :user=user />
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