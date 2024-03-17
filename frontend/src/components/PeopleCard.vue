<script setup></script>
<template>
    <v-card class="rounded-xl">
        <v-card-item>
            <v-img cover class=" rounded-lg" src="https://picsum.photos/160">
            </v-img>
        </v-card-item>
        <v-card-item>
            <v-container>
            <v-row>
                <v-col>
                    <v-img cover  class="rounded-circle border border-secondary border-lg" width="100"
                    height="100" src="https://picsum.photos/170">
                    </v-img>
                </v-col>
                <v-col>
                    <v-card-title>John Doe</v-card-title>
                    <v-card-text>Card subtitle</v-card-text>
                </v-col>
            </v-row>
            </v-container>
        </v-card-item>
    </v-card>
</template>

<script>
export default {
    name: 'PeopleCard',
}
</script>