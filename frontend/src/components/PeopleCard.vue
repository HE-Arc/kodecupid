<template slot="user">
    <v-card class="rounded-xl">
        <v-card-item v-if=details>
            <v-container>
                <v-row>
                    <v-col class="flex-grow-0 mr-4">
                        <v-img cover class="rounded-circle border border-secondary border-lg" width="200" height="200"
                            :src=user.pfp_src>
                        </v-img>
                    </v-col>

                    <v-col class="align-center d-flex">
                        <v-row>
                            <v-col>
                                <v-card-title>{{ user.username }}</v-card-title>
                                <v-card-subtitle>{{ user.sex ? 'Homme' : 'Femme' }}</v-card-subtitle>
                            </v-col>
                        </v-row>
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
                            <v-chip v-if="user.tags && user.tags.length" v-for="tag in user.tags">
                                {{ tag.name }}
                            </v-chip>
                            <v-chip v-else>aucun</v-chip>
                        </v-chip-group>
                    </v-col>
                </v-row>

                <v-divider class="my-4"></v-divider>

                <v-row>
                    <v-col v-if="user.pictures && user.pictures.length">
                        <v-carousel class="rounded-lg" show-arrows="hover">
                            <v-carousel-item v-for="picture in user.pictures" :key="picture.id"
                                :src=picture.image_data></v-carousel-item>
                        </v-carousel>
                    </v-col>

                    <v-col v-else>
                        <p>Aucune image</p>
                    </v-col>
                </v-row>

            </v-container>
        </v-card-item>
        <v-card-item v-if=!details>
            <v-container>
                <v-row>
                    <v-col cols="flex-grow-0 mr-4">
                        <v-img cover class="rounded-circle border border-secondary border-lg" width="200" height="200"
                            :src=user.pfp_src>
                        </v-img>
                    </v-col>

                    <v-col class="align-center d-flex">
                        <v-row>
                            <v-col>
                                <v-card-title>{{ user.username }}</v-card-title>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-item>
    </v-card>
</template>

<script setup>

const { user, details } = defineProps({
    user: {
        type: Object,
        required: true
    },
    details: {
        type: Boolean,
        required: false
    }
});

// Component name
const name = 'PeopleCard';


</script>