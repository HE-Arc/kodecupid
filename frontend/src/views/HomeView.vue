<script setup>
import PeopleCard from '@/components/PeopleCard.vue';
</script>

<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <PeopleCard />
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-container class="d-flex justify-space-between">
                    <v-btn class="bg-like"><v-icon>mdi-thumb-up</v-icon></v-btn>
                    <v-btn class="bg-dislike"><v-icon>mdi-thumb-down</v-icon></v-btn>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>
