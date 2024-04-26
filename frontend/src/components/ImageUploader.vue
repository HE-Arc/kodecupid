<template slot="pfp">
    <v-row>
        <v-col>
            <v-label for="imageUpload">Profile Picture:</v-label>
            <v-file-input :rules="rules" @change="previewImage" accept="image/png, image/jpeg, image/bmp" label="Avatar"
                placeholder="Pick an avatar" prepend-icon="mdi-camera"></v-file-input>
            <v-img v-if="imagePreview" :src="pfp" class="rounded-circle border border-secondary" width="100"
                height="100"></v-img>
            <v-btn @click="handleSubmit" class="bg-like"><v-icon>mdi-thumb-up</v-icon></v-btn>
        </v-col>
    </v-row>
</template>

<script setup>
import { ApiClient } from '@/clients/apiClient.js';
import { ref } from 'vue';

const imagePreview = ref(null);
const selectedFile = ref(null);

const rules = ref([
    v => !v,
    v => !v.length,
    v => v[0].size < 200000 || 'Avatar size should be less than 2 MB!'
])

const previewImage = async (event) => {
    // Method to preview image before uploading
    selectedFile.value = event.target.files[0];
    if (selectedFile) {
        imagePreview.value = URL.createObjectURL(selectedFile.value);
    }
}

const handleSubmit = async () => {
    const formData = new FormData();

    if (selectedFile.value) {
        formData.append('image', selectedFile.value);
    }

    // await ApiClient.addPicture(formData);
    // await ApiClient.addProfilePicture(selectedFile.value);
}

</script>