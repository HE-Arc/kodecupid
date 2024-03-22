<template v-if="config">
    <v-card v-model="user" class="rounded-xl">
        <v-container>
            <v-row>
                <v-col>
                    <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                        :src="user.pfp">
                    </v-img>
                </v-col>

                <v-col>
                    <v-card-title>{{ user.username }}</v-card-title>
                    <v-card-subtitle>{{ user.bio }}</v-card-subtitle>
                    <v-card-subtitle>{{ user.looking_for }}</v-card-subtitle>
                </v-col>

                <v-col>
                    <v-btn :to="{ name: 'account-edit' }" color="primary">Modifier mon profil</v-btn>
                </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>

            <v-row>
                <v-col>
                    <v-label>Tags:</v-label>
                    <v-chip-group column>
                        <v-chip v-if="user.tags && user.tags.length" v-for="tag in user.tags">{{ tag.name }}</v-chip>
                        <v-chip v-else>aucun</v-chip>
                    </v-chip-group>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script setup>
import { store } from '@/store';
import { ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';

const user = ref({
    username: ref(''),
    bio: ref(''),
    looking_for: ref(''),
    pfp: ref('https://picsum.photos/170'),
    tags: ref([])
});


const fetchUser = async ()=> {
    const response = await axios.get(store.routes['USER_DETAIL']).catch((error) => {
        console.error(error.response.data);
        return error
    }).then(response => {
        console.log(response.data);
        user.value = response.data;
    });
};

onMounted(() => {
    fetchUser();
});
</script>