<template v-if="config">
    <v-form id="edit-form" @submit.prevent="handleSubmit">
        <v-card v-model="user" class="rounded-xl">
            <v-container>
                <v-row>
                    <v-col>
                        <v-img cover class="rounded-circle border border-secondary border-lg" width="100" height="100"
                            :src="user.pfp">
                        </v-img>
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
                            <v-text-field v-model="user.bio" label="Bio" type="bio" :rules="bioRules" :value="user.bio" required />
                        </v-card-subtitle>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-subtitle>
                            <v-text-field v-model="user.looking_for" :rules="looking_forRules" label="Préférences de recherche" type="looking_for"
                                :value="user.looking_for" required />
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
import { store } from '@/store';
import { setError } from '@/store';
import { ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';
import { computed } from 'vue';

const user = ref({
    username: ref(''),
    bio: ref(''),
    looking_for: ref(''),
    pfp: ref('https://picsum.photos/170'),
    tags: ref([])
});

const all_tags = [];
const list_tags = ref([]);

const showTagList = ref(false);
const search = ref('');
const uninitialized = ref(localStorage.getItem('uninitialized'));

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

    const jsonForm = JSON.stringify(user.value);

    axios.patch(store.routes['USER_DETAIL'], jsonForm, {
        headers: {
            'Content-Type': 'application/json'
        }
    }, { withCredentials: true }).catch((error) => {
        console.error(error.response.data);
        setError(error.response.data,'error');
        return error
    }).then(response => {
        uninitialized.value = false;
        setError({message:'L\'utilisateur a été mis à jour'},'success');
        localStorage.setItem('uninitialized', false);
        router.push({ name: 'account-show', replace: true, force: true });
    });
};

const fetchUser = async () => {
    axios.get(store.routes['USER_DETAIL']).catch((error) => {
        console.error(error.response.data);
        setError(error.response.data,'error');
        return error
    }).then(response => {
        user.value = response.data;
    });
};

const fetchTags = async () => {
    axios.get(store.routes['TAG_LIST']).catch((error) => {
        console.error(error.response.data);
        setError(error.response.data,'error');
        return error
    }).then(response => {
        all_tags.push(...response.data);
    });
};

const fetchUserTags = async () => {
    axios.get(store.routes['USER_TAGS']).catch((error) => {
        console.error(error.response.data);
        setError(error.response.data,'error');
        return error
    }).then(response => {
        user.value.tags = response.data;
    });
};

onMounted(() => {
    fetchUser();
    fetchTags();
    fetchUserTags();
});

computed(() => {
    filteredTags();
});

import { watch } from 'vue';
import router from '@/router';

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
    showTagList.value = true; // Show the tag list
};

const addTag = (tag) => {
    axios.post(store.routes['USER_TAG_ADD'], JSON.stringify(tag))
        .catch((error) => {
            console.error(error.response.data);
            setError(error.response.data,'error');
            return error
        }).then(response => {
            user.value.tags.push(tag);
            list_tags.value = all_tags.filter((tag) => !user.value.tags.includes(tag))
        });

    showTagList.value = false;
    search.value = '';
}

const deleteTag = (tag) => {
    user.value.tags = user.value.tags.filter((t) => t.id !== tag.id);
    axios.delete(store.routes['USER_TAG_REMOVE'], { data: JSON.stringify(tag) })
        .catch((error) => {
            console.error(error.response.data);
            setError(error.response.data,'error');
            return error
        }).then(response => {
            list_tags.value = all_tags.filter((tag) => !user.value.tags.includes(tag))
        });
}
</script>