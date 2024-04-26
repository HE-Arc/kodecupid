<template v-if="config">
    <v-form id="edit-form" @submit.prevent="handleSubmit">
        <v-card v-model="user" class="rounded-xl">
            <v-container>
                <v-row>
                    <v-col>
                        <v-img cover class="rounded-circle border border-secondary border-lg mr-3" width="100"
                            height="100" :src="pfp">
                            <v-img cover v-if="imagePreview" :src="imagePreview" width="100" height="100"></v-img>
                        </v-img>
                        <v-file-input :rules="pfprules" @change="previewImage" @click:clear="imagePreview = null"
                            accept="image/png, image/jpeg" label="Avatar" prepend-icon="mdi-camera">
                        </v-file-input>
                    </v-col>

                    <v-col>
                        <v-btn form="edit-form" type="submit" color="primary" class="mr-4">Enregistrer</v-btn>
                        <v-btn v-if="uninitialized" :to="{ name: 'account-show' }"><v-icon> mdi-cancel</v-icon></v-btn>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-title>
                            <v-text-field v-model="user.username" label="Nom d'utilisateur" type="username"
                                :value="user.username" :rules="usernameRules" required />
                        </v-card-title>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-subtitle>
                            <v-text-field v-model="user.bio" label="Bio" type="bio" :rules="bioRules" :value="user.bio"
                                required />
                        </v-card-subtitle>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-subtitle>
                            <v-text-field v-model="user.looking_for" :rules="looking_forRules"
                                label="Préférences de recherche" type="looking_for" :value="user.looking_for"
                                required />
                        </v-card-subtitle>
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
// import ImageUploader from '@/components/ImageUploader.vue';

const user = ref({});
const pfp = ref({});

const imagePreview = ref(null);
const selectedFile = ref(null);

const all_tags = [];
const list_tags = ref([]);

const showTagList = ref(false);
const search = ref('');
const uninitialized = ref(localStorage.getItem('uninitialized'));


const pfprules = ref([
    v => !v,
    v => !v.length,
    v => v[0].size < 200000 || 'Avatar size should be less than 2 MB!'
])

const usernameRules = [
    v => !!v || 'Le nom d\'utilisateur est obligatoire',
    v => v.length >= 3 || 'Le nom d\'utilisateur doit contenir min. 3 caractères'
];

const bioRules = [
    v => !!v || 'La description (bio) est obligatoire',
];

const looking_forRules = [
    v => !!v || 'Vos préférences de recherche sont obligatoires',
    v => v.length >= 3 || 'Vos préférences de recherche doivent contenir min. 3 caractères'
];

const handleSubmit = async () => {
    user.value.tags = user.value.tags?.map(tag => tag.id);
    if (selectedFile.value) {
        const formdata = new FormData();
        formdata.append('image', selectedFile.value);
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

const fetchUser = async () => {
    const fetchedUser = await ApiClient.getUser();
    const fetchedTags = await ApiClient.getUserTags(fetchedUser.id);
    if (fetchedUser.pfp) {
        const fetchedUserPfp = await ApiClient.getPicture(fetchedUser.pfp);
        if (fetchedUserPfp) {
            pfp.value = fetchedUserPfp;
        }
    }

    user.value.id = fetchedUser.id;
    user.value.username = fetchedUser.username;
    user.value.bio = fetchedUser.bio;
    user.value.looking_for = fetchedUser.looking_for;
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