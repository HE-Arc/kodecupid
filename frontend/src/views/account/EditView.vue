<template v-if="config">
    <v-form id="edit-form" ref="form" v-model="valid" @submit.prevent="handleSubmit">
        <v-card v-model="user" class="rounded-xl">
            <v-container>
                <v-row>
                    <v-col>
                        <div class="image-upload-container">
                            <v-img class="rounded-circle border border-secondary border-lg mr-3" :aspect-ratio="1"
                                min-width="50" max-width="200" :src="imagePreview || user.pfp_src">
                                <template v-slot:placeholder>
                                    <v-row class="fill-height ma-0" align="center" justify="center">
                                        <v-icon color="grey lighten-1" size="56">mdi-account-circle</v-icon>
                                    </v-row>
                                </template>
                            </v-img>
                            <v-file-input class="file-input-overlay" @change="previewImage"
                                @click:clear="imagePreview = null" accept="image/png, image/jpeg" label="Change Avatar"
                                prepend-icon="mdi-camera"
                                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0;">
                            </v-file-input>
                        </div>
                    </v-col>

                    <v-col>
                        <v-btn :disabled="!valid" form="edit-form" type="submit" color="primary"
                            class="mr-4">Enregistrer</v-btn>
                        <v-btn v-if="uninitialized" :to="{ name: 'account-show' }"><v-icon> mdi-cancel</v-icon></v-btn>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field v-model="user.username" label="Nom d'utilisateur" type="username"
                            :value="user.username" :rules="usernameRules" required />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-textarea v-model="user.bio" label="Bio" type="bio" :rules="bioRules" :value="user.bio"
                            required></v-textarea>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <!-- Radio buttons for sex -->
                        <v-row>
                            <v-col cols="6">
                                <v-label>Sexe</v-label>
                                <v-radio-group v-model="user.sex" row>
                                    <v-radio label="Homme" :value=true></v-radio>
                                    <v-radio label="Femme" :value=false></v-radio>
                                </v-radio-group>
                            </v-col>
                            <v-col cols="6" class="d-flex justify-center align-center">
                                <v-img :src="sexImage" height="100px" class="rounded-circle shadow" />
                            </v-col>
                        </v-row>

                        <!-- Radio buttons for looking_for -->
                        <v-row>
                            <v-col cols="6">
                                <v-label>Recherche</v-label>
                                <v-radio-group v-model="user.looking_for" row>
                                    <v-radio label="Homme" :value=true></v-radio>
                                    <v-radio label="Femme" :value=false></v-radio>
                                </v-radio-group>
                            </v-col>
                            <v-col cols="6" class="d-flex justify-center align-center">
                                <v-img :src="lookingForImage" height="100px" class="rounded-circle shadow" />
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>

                <v-divider class="my-4"></v-divider>

                <v-row>
                    <v-col>
                        <v-label>Tags:</v-label>
                        <v-chip-group column>
                            <v-chip @click.close="" v-for="tag in user.tags">{{ tag.name }}<template #close>
                                    <v-icon icon="mdi-close-circle" @click.stop="deleteTag(tag)" />
                                </template>
                            </v-chip>
                            <v-chip @click="openTagList"><v-icon>mdi-plus</v-icon></v-chip>

                            <v-list v-if="showTagList" class="tag-list">
                                <v-text-field v-model="search" label="Rechercher" outlined dense
                                    hide-details></v-text-field>
                                <v-list-item v-for="tag in filteredTags()" :key="tag" @click="addTag(tag)">
                                    <v-list-item-title>{{ tag.name }}</v-list-item-title>
                                </v-list-item>
                            </v-list>
                        </v-chip-group>
                    </v-col>
                </v-row>

                <v-divider class="my-4"></v-divider>

                <v-row>
                    <v-col>
                        <v-label>Images:</v-label>
                        <v-file-input @change="addPicture" accept="image/png, image/jpeg" label="Image"
                            prepend-icon="mdi-camera">
                        </v-file-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col v-if="user.pictures && user.pictures.length">
                        <v-carousel class="rounded-lg" show-arrows="hover">
                            <v-carousel-item v-for="picture in user.pictures" :key="picture.id" :src=picture.image_data>
                                <v-btn class="text-red" icon="mdi-delete" variant="text"
                                    @click="deletePicture(picture)">
                                </v-btn>
                            </v-carousel-item>
                        </v-carousel>
                    </v-col>
                    <v-col v-else>
                        <p>Aucune image</p>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </v-form>
</template>

<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import { computed } from 'vue';
import { ApiClient } from '@/clients/apiClient.js';
import { watch } from 'vue';
import router from '@/router';

const user = ref({});

const imagePreview = ref(null);
const selectedFile = ref(null);

const all_tags = [];
const list_tags = ref([]);

const showTagList = ref(false);
const search = ref('');
const uninitialized = ref(localStorage.getItem('uninitialized'));

const valid = ref(false);
const form = ref(null);

const usernameRules = [
    v => !!v || 'Le nom d\'utilisateur est obligatoire',
    v => v.length >= 3 || 'Le nom d\'utilisateur doit contenir min. 3 caractères'
];

const bioRules = [
    v => !!v || 'La description (bio) est obligatoire',
    v => v.length < 256 || 'Bio trop longue !'
];

const handleSubmit = async () => {

    if (!form.value.validate()) {
        return;
    }

    user.value.tags = user.value.tags?.map(tag => tag.id);
    if (selectedFile.value) {
        const formdata = new FormData();
        formdata.append('image', selectedFile.value);
        if (user.value.pfp) {
            await ApiClient.deletePicture(user.value.pfp);
        }
        user.value.pfp = await ApiClient.addPicture(formdata);
    }

    const response = await ApiClient.updateUser(JSON.stringify(user.value), user.value.id);

    if (response) {
        router.push({ name: 'account-show', replace: true, force: true });
    }
};

const previewImage = async (event) => {
    selectedFile.value = event.target.files[0];
    if (selectedFile) {
        imagePreview.value = URL.createObjectURL(selectedFile.value);
    }
}

const addPicture = async (event) => {
    const selectimage = event.target.files[0];
    if (selectimage) {
        const formdata = new FormData();
        formdata.append('image', selectimage);

        const response = await ApiClient.addPicture(formdata);
        if (response) {
            const fetchedpicture = await ApiClient.getPicture(response);
            user.value.pictures.push(JSON.parse('{"id": ' + response + ',"image_data": "' + fetchedpicture + '"}'));

        }
    }
}

const deletePicture = async (picture) => {
    await ApiClient.deletePicture(picture.id);
    const index = user.value.pictures.indexOf(picture);
    user.value.pictures.splice(index, 1);
};

const fetchUser = async () => {
    const fetchedUser = await ApiClient.getUser();
    const fetchedTags = await ApiClient.getUserTags(fetchedUser.id);
    if (fetchedUser.pfp) {
        const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);
        if (fetchedUserPfp) {
            user.value.pfp_src = fetchedUserPfp;
        }
    }

    const fetchedPictures = await ApiClient.getPictures();

    if (fetchedPictures) {
        user.value.pictures = fetchedPictures;
    } else {
        user.value.pictures = [];
    }

    user.value.id = fetchedUser.id;
    user.value.username = fetchedUser.username;
    user.value.bio = fetchedUser.bio;
    user.value.looking_for = fetchedUser.looking_for;
    user.value.sex = fetchedUser.sex;
    user.value.pfp = fetchedUser.pfp;
    user.value.tags = fetchedTags;
};

const fetchTags = async () => {
    const fetchedTags = await ApiClient.getTags();
    all_tags.push(...fetchedTags);
};

onMounted(() => {
    fetchUser();
    fetchTags();
});

computed(() => {
    filteredTags();
});

watch(search, () => {
    // Reset scroll position when search changes
    const list = document.querySelector('.tag-list .v-list');
    if (list) {
        list.scrollTop = 0;
    }
});


const lookingForImage = computed(() => {
    return user.value.looking_for ? '/giga_chad.jpg' : '/giga_female.jpg';
});

const sexImage = computed(() => {
    return user.value.sex ? '/giga_chad.jpg' : '/giga_female.jpg';
});

const filteredTags = () => {
    const all_tags_ids = all_tags.map((tag) => tag.id);
    const user_tags_ids = user.value.tags.map((tag) => tag.id);
    const all_tags_not_in_user = all_tags_ids.filter((tag) => !user_tags_ids.includes(tag));
    const filtered_tags = all_tags.filter((tag) => all_tags_not_in_user.includes(tag.id));
    return filtered_tags.filter(tag =>
        tag.name.toLowerCase().includes(search.value.toLowerCase())
    );
}

const openTagList = () => {
    showTagList.value = true;
};

const addTag = async (tag) => {
    const jsonTag = JSON.stringify(tag);
    const response = await ApiClient.addUserTag(jsonTag);
    if (response) {
        user.value.tags.push(tag);
        showTagList.value = false;
        search.value = '';
    }
}

const deleteTag = async (tag) => {
    const jsonTag = JSON.stringify(tag);
    const response = await ApiClient.deleteUserTag(jsonTag);
    if (response) {
        user.value.tags = user.value.tags.filter((t) => t.id !== tag.id);
        list_tags.value = all_tags.filter((tag) => !user.value.tags.includes(tag))
    }
}
</script>