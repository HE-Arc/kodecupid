<template>
    <v-row>
        <v-col>
            <v-label for="imageUpload">Profile Picture:</v-label>
            <input type="file" id="imageUpload" @change="previewImage" accept="image/*">
            <v-img v-if="imagePreview" :src="imagePreview" class="rounded-circle border border-secondary" width="100" height="100"></v-img>
            <v-btn @click="handleSubmit" class="bg-like"><v-icon>mdi-thumb-up</v-icon></v-btn>
        </v-col>
    </v-row>
</template>

<script>

import { store } from '@/store';
import axios from 'axios';

export default {
    data() {
        return {
            // Existing data properties
            imagePreview: null, // For displaying the selected image preview
            selectedFile: null, // To hold the selected file
            // Other existing data properties
        };
    },
    methods: {
        previewImage(event) {
            // Method to preview image before uploading
            this.selectedFile = event.target.files[0];
            if (this.selectedFile) {
                this.imagePreview = URL.createObjectURL(this.selectedFile);
            }
        },
        handleSubmit() {
            const formData = new FormData();

            // Append the selected file if there is one
            if (this.selectedFile) {
                formData.append('image', this.selectedFile);
            }

            // Perform the API call with formData
            axios.post(store.routes['USER_PICTURE'], formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                // Handle success
                console.log('Profile updated successfully.', response.data);
            }).catch(error => {
                // Handle error
                console.error('Error updating profile:', error);
            });
        },
        // Other methods...
    },
    // Other options...
}

</script>