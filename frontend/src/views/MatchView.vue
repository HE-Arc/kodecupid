<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <PeopleCard v-for ="user in match" :user=user />
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import PeopleCard from '@/components/PeopleCard.vue';

import { store } from '@/store';
import axios from 'axios';

const match = ref([]);

const fetchUserMatch = async () => {
    try {
        match.value = await axios.get(store.routes['USER_MATCH'], {});
    }
    catch (e) {
        match.value = [{
            id: -1,
            name: 'User not found',
            bio: 'User not found',
            avatar: 'https://picsum.photos/170'
        }];
    }
};

onMounted(() => {
    fetchUserMatch();
});

</script>