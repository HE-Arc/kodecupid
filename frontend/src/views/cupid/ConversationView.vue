<template>
    <v-container fullscreen>
        <v-row>
            <v-col class="d-flex align-center">
                <v-img :src="user_target.pfp_src" :aspect-ratio="1" min-width="50" max-width="100"
                    class="rounded-circle border border-secondary border-lg mr-4 flex-grow-1">
                </v-img>
                <p>{{ user_target.username }}</p>
            </v-col>
        </v-row>

        <v-divider class="my-4"></v-divider>

        <v-row class="mb-4">
            <v-container ref="scrollContainer" class="mx-4 scrollable-container">
                <template v-if="conversation.length > 0">
                    <v-row v-for="message in conversation" :key="message.id">
                        <v-col
                            :class="{ 'd-flex flex-row-reverse': message.source_user === user.id, 'd-flex flex-row': message.source_user !== user.id }">
                            <v-card
                                :class="{ 'bg-blue': message.source_user === user.id, 'bg-blue-lighten-5': message.source_user !== user.id }"
                                elevation="4" class="flex-grow-1" max-width="65%">
                                <v-card-text>{{ message.content }}</v-card-text>
                                <v-card-text class="text-right">{{ message.sent }}</v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </template>
            </v-container>
        </v-row>

        <v-row>
            <v-form @submit.prevent="sendMessage" @keyup.native.enter class="d-inline-flex w-100">
                <v-text-field variant="solo" class="mr-2 flex-grow-1" v-model="message" label="Message" type="text"
                    append-inner-icon="mdi-send" @click:append-inner="sendMessage"/>
            </v-form>
        </v-row>
    </v-container>
</template>

<style scoped>
.scrollable-container {
    max-height: calc(100vh - 350px);
    /* Adjust the height as needed */
    overflow-y: auto;
    /* Enables vertical scrolling */
    scrollbar-width: none;
    /* For Firefox */
    -ms-overflow-style: none;
    /* For Internet Explorer and Edge */
}

.scrollable-container::-webkit-scrollbar {
    display: none;
    /* For Chrome, Safari, and Opera */
}
</style>

<script setup>
import { onMounted, ref, nextTick } from 'vue';
import { ApiClient } from '@/clients/apiClient.js';

import router from '@/router';

const conversation = ref([]);
const user_target = ref({});
const user = ref({});

const message = ref('');

const lastConversationLength = ref(0)

onMounted(() => {
    fetchConversation().then(() => {
        scrollToBottom();
    });

    setInterval(() => {
        fetchConversation();
    }, 5000);
});

const scrollToBottom = () => {
    nextTick(() => {
        const scrollElement = document.querySelector('.scrollable-container');
        if (!scrollElement) return;
        scrollElement.scrollTop = scrollElement.scrollHeight;
    });
}

const sendMessage = async () => {

    if(message.value.length == 0)
        return;

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
        if (fetchedUser.pfp) {
            const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);
            if (fetchedUserPfp) {
                user_target.value.pfp_src = fetchedUserPfp;
            }
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
            if (fetchedConversation.length > lastConversationLength.value) {
                scrollToBottom();
            }

            lastConversationLength.value = fetchedConversation.length;
        }
    }
};
</script>