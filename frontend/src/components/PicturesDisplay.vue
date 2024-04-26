<template>
    <div class="user-images">
      <v-container>
        <v-row>
          <v-col cols="12" sm="6" md="4" lg="3" v-for="image in images" :key="image.id">
            <v-img :src="image.url" class="mb-4" aspect-ratio="1"></v-img>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserImages',
    props: {
      userId: Number,
    },
    data() {
      return {
        images: [],
      };
    },
    created() {
      this.fetchImages();
    },
    methods: {
      async fetchImages() {
        try {
          const response = await this.axios.get(`/api/pictures/`, {
            params: {
              user: this.userId,
            },
          });
          this.images = response.data;
        } catch (error) {
          console.error('Error fetching images:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .user-images {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }
  </style>
  