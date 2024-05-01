<template slot="user">
    <v-card class="rounded-xl">
        <v-card-item>
            <v-container>
                <v-row>
                    <v-col>
                        <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                            :src=user.pfp_src>
                        </v-img>
                    </v-col>
                    <v-col>
                        <v-card-title>{{ user.username }}</v-card-title>
                        <v-card-text>{{ user.bio }}</v-card-text>
                    </v-col>
                    <v-col>
                        <v-label>Tags:</v-label>
                        <v-chip-group column>
                            <v-chip v-if="user.tags && user.tags.length" v-for="tag in user.tags">{{ tag.name
                                }}</v-chip>
                            <v-chip v-else>aucun</v-chip>
                        </v-chip-group>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-item>
        <v-card-item v-if="user.pictures && user.pictures.length">
            <v-carousel class="rounded-lg" show-arrows="hover">
                <v-carousel-item v-for="picture in user.pictures" :key="picture.id">
                    <v-img cover class="rounded-lg" :src=picture.image_data></v-img>
                </v-carousel-item>
            </v-carousel>
        </v-card-item>
    </v-card>
</template>

<script setup>

const { user, pfp } = defineProps({
    user: {
        type: Object,
        required: true
    }
});

// Component name
const name = 'PeopleCard';


</script>