<template v-if="config">
    <v-card class="rounded-xl">
        <v-container>
            <v-row>
                <v-col>
                    <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                        :src=user.pfp_src>
                    </v-img>
                </v-col>

                <v-col>
                    <v-card-title>{{ user.username }}</v-card-title>
                    <v-card-subtitle>{{ user.sex ? 'Homme' : 'Femme' }}</v-card-subtitle>
                </v-col>

                <v-col>
                    <v-btn :to="{ name: 'account-edit' }" color="primary">Modifier mon profil</v-btn>
                </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>

            <v-row>
                <v-col>
                    <v-label>Bio:</v-label>
                    <br>
                    {{ user.bio }}
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

            <v-divider class="my-4"></v-divider>

            <v-row>
                <v-col v-if="user.pictures && user.pictures.length">
                    <v-carousel class="rounded-lg" show-arrows="hover">
                        <v-carousel-item v-for="picture in user.pictures" :key="picture.id" :src=picture.image_data></v-carousel-item>
                    </v-carousel>
                </v-col>

                <v-col v-else>
                    <p>Aucune image</p>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script setup>

import { ref } from 'vue';
import { onMounted } from 'vue';
import { ApiClient } from '@/clients/apiClient.js';

const user = ref({});

const fetchUser = async () => {
    const fetchedUser = await ApiClient.getUser();
    const fetchedTags = await ApiClient.getUserTags(fetchedUser.id);
    const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);

    if (fetchedUserPfp) {
        user.value.pfp_src = fetchedUserPfp;
    }

    const fetchedPictures = await ApiClient.getPictures();

    if (fetchedPictures) {
        user.value.pictures = fetchedPictures;
    }

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