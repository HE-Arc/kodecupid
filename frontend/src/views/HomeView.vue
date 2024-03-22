<template>
    <v-container >
        <v-row>
            <v-col>
                <v-img cover class="rounded" src="/logo1024.png"></v-img>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-chip> > [SUCCESS] New connection established ! </v-chip>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <p>Bienvenue sur KodeCupid: la plateforme de rencontres dédiée aux ingénieurs informatiques et
                    passionnés de la tech !
                </p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <p>
                    Faites la rencontre de personnes qui partagent votre amour pour la tech et le coding sur KodeCupid. Qui sait, vous pourriez bien trouver votre binôme de code idéal... ou pas ! Mais bon, ça vaut le coup d'essayer.
                </p>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-img cover class="rounded-lg" src="/jdg-joueur-du-grenier.gif"></v-img>
            </v-col>
        </v-row>
        <v-row>
            <v-col class="d-flex justify-center">
                <v-btn color="primary" :to="{ name: 'signin' }">Connecte-toi</v-btn>
            </v-col>
            <v-col class="d-flex justify-center">
                <v-btn color="primary" :to="{ name: 'signup' }">Crée un compte</v-btn>
            </v-col>
        </v-row>
        <v-divider class="my-4"></v-divider>
        <v-row>
            <v-col>
                <h1><v-icon color="blue">mdi-shield-crown</v-icon>L'équipe</h1>
                <v-list>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon>Lucas Gosteli</p>
                    </v-list-item>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon>Damien Tschan</p>
                    </v-list-item>
                    <v-list-item>
                        <p><v-icon color="blue">mdi-shield-sword</v-icon>Bruno Thomas</p>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>
    </v-container>

</template>