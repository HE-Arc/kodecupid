<template>
    <v-container>
        <v-banner sticky class="d-inline-flex align-center mb-4" style="z-index: 1;">
            <v-img cover class="rounded-circle border border-secondary border-lg mr-2" width="50" height="50"
                :src=user_target.pfp_src>
            </v-img>
            <p> {{ user_target.username }}</p>
        </v-banner>
        <v-row class="mb-4">
            <v-container class="mx-4">
                <v-row v-if="conversation.length > 0" v-for="message in conversation">
                    <v-col class="d-flex flex-row-reverse" v-if="message.source_user == user.id">
                        <v-card class="w-75 bg-blue" elevation="4">
                            <v-card-text>{{ message.content }}</v-card-text>
                            <v-card-text class="text-right">{{ message.sent }}</v-card-text>
                        </v-card>
                    </v-col>
                    <v-col class="d-flex flex-row" v-else>
                        <v-card class="w-75 bg-blue-lighten-5" elevation="4">
                            <v-card-text>{{ message.content }}</v-card-text>
                            <v-card-text class="text-right">{{ message.sent }}</v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-row>
        <v-row>
            <v-form @submit.prevent="sendMessage" @keyup.native.enter class="d-inline-flex w-100 align-center">
                <v-text-field variant="solo" class="mr-2 flex-grow-1" v-model="message" label="Message" type="text" />
                <v-btn type="submit" class="bg-primary ">Envoyer</v-btn>
            </v-form>
        </v-row>
    </v-container>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import { ApiClient } from '@/clients/apiClient.js';

import router from '@/router';

const conversation = ref([]);
const user_target = ref({});
const user = ref({});

const message = ref('');


onMounted(() => {
    fetchConversation();

    setInterval(() => {
        fetchConversation();
    }, 5000);
});

const sendMessage = async () => {

    const target_user = router.currentRoute.value.params.id;
    if (target_user) {

        const jsonForm = JSON.stringify({
            source_user: user.value.id,
            target_user: target_user,
            content: message.value
        });
        const response = await ApiClient.addMessage(jsonForm);

        if (response) {
            message.value = '';
            fetchConversation();
        }
    }
}

const fetchConversation = async () => {

    const fetchedUser = await ApiClient.getUser();
    user.value = fetchedUser;

    const target_user = router.currentRoute.value.params.id;
    if (target_user) {
        const fetchedUser = await ApiClient.getUserById(target_user);

        const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);

        if (fetchedUserPfp) {
            user_target.value.pfp_src = fetchedUserPfp;
        }

        user_target.value.id = fetchedUser.id;
        user_target.value.username = fetchedUser.username;
        const fetchedConversation = await ApiClient.getConversation(target_user);

        if (fetchedConversation) {
            fetchedConversation.forEach((message) => {
                const date = new Date(message.sent);
                message.sent = date.toLocaleString();
            });
            conversation.value = fetchedConversation;
        }
    }
};
</script>