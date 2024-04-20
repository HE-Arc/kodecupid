<template slot="user">
    <v-card class="rounded-xl">
        <v-card-item>
            <template slot="pfp">

                <v-img cover class=" rounded-lg" :src=pfp>
                </v-img>
            </template>
        </v-card-item>
        <v-card-item>
            <v-container>
                <v-row>
                    <v-col>
                        <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                            src="https://picsum.photos/160">
                        </v-img>
                    </v-col>
                    <v-col>
                        <v-card-title>{{ user.username }}</v-card-title>
                        <v-card-text>{{ user.bio }}</v-card-text>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-item>
    </v-card>
</template>

<script>
export default {
    props: {
        user: {
            type: Object,
            required: true
        }
    },
    name: 'PeopleCard',
}
</script>