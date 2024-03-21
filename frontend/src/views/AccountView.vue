<template>
    <v-card v-model="user" class="rounded-xl">
        <v-container>
            <v-row>
                <v-col v-if="user.avatar">
                    <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                        :src="user.avatar">
                    </v-img>
                </v-col>

                <v-col>
                    <v-card-title>{{ store.user.name }}</v-card-title>
                    <v-card-subtitle>{{ store.user.email }}</v-card-subtitle>
                    <v-card-subtitle>{{ store.user.bio }}</v-card-subtitle>
                </v-col>

                <v-col>
                    <v-btn color="primary">modifier mon profil</v-btn>
                </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>

            <v-row>
                <v-col>
                    <v-label>Tags:</v-label>
                    <v-chip-group column>
                        <v-chip v-for="tag in user.tags">{{ tag }}</v-chip>
                    </v-chip-group>
                </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>
            <v-row><v-label>Photos:</v-label></v-row>
            <v-row>
                <template v-for="(image, imgIdx) in imageLayout" :key="imgIdx">
                    <v-col :cols="image.cols">
                        <v-img :src="`https://picsum.photos/500/300?image=${image.cols * 20}`" height="100%"
                            cover></v-img>
                    </v-col>

                    <v-col v-if="image.children" class="d-flex flex-column" cols="6">
                        <v-row>
                            <v-col v-for="(children, childIdx) in image.children" :key="childIdx" :cols="children.cols">
                                <v-img :src="`https://picsum.photos/500/300?image=${children.cols + childIdx}`"
                                    height="100%" cover></v-img>
                            </v-col>
                        </v-row>
                    </v-col>
                </template>
            </v-row>
        </v-container>
    </v-card>
</template>

<script setup>
import { store } from '@/store';
import { getCurrentInstance } from 'vue';

const { appContext } = getCurrentInstance();
const axios = appContext.config.globalProperties.$axios;

const fetchUser =async ()=> {
    const response = await axios.get(store.routes['USER']);
    store.user.value = response.data;
};

import { onMounted } from 'vue';

onMounted(() => {
    fetchUser();
});

const imageLayout = [
    { cols: 4 },
    {
        cols: 8,
        children: [{ cols: 12 }, { cols: 12 }],
    },
    { cols: 6 },
    { cols: 3 },
    { cols: 9 },
    { cols: 4 },
    { cols: 8 },
]
</script>