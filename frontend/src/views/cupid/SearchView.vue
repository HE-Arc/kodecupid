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
import { setError } from '@/store';
import axios from 'axios';

const user = ref({});

const like = async () => {
    axios.post(store.routes['USER_LIKE'], { target_user_id: user.value.id }).catch((error) => {
        setError(error.response.data,'error');
        fetchUser();
    })
    .then(response => {
        fetchUser();
    });
};

const dislike = async () => {
    fetchUser();
};

const fetchUser = async () => {
    axios.get(store.routes['USER_SEARCH'], {params : {id : "random"}}).catch((error) => {
        console.error(error.response.data);
        setError(error.response.data,'error');
        return error
    }).then(response => {
        user.value = response.data;
    });
};

onMounted(() => {
    fetchUser();
});

</script>