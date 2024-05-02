import {setError} from '@/store';
import axios from 'axios';

import {RouteEnum, routes_api} from '../configs/constants';

const API_SERVER_URL = import.meta.env.VITE_API_URL;

export class ApiClient {
  // users
  static async signupUser(data) {
    try {
      const response =
          await axios.post(handleRoute(RouteEnum.USER_LIST), data, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'anonymous'
            }
          });

      if (response.status === 201) {
        localStorage.setItem('uninitialized', true);
        setError({message: 'Votre compte a été bien enregistre'}, 'success');
        return true
      }
    } catch (error) {
      setError(error.response.data, 'error');
      return false;
    }
  }
  static async signinUser(data) {
    try {
      const response =
          await axios.post(handleRoute(RouteEnum.TOKEN_OBTAIN_PAIR), data, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'anonymous'
            }
          });
      if (response.status === 200) {
        localStorage.setItem('accessToken', response.data.access);
        axios.defaults.headers.common['Authorization'] =
            `Bearer ${localStorage.getItem('accessToken')}`;
        localStorage.setItem('refreshToken', response.data.refresh);
        return true;
      }
    } catch (error) {
      console.error(error);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async getUserRandom() {
    try {
      const response =
          await axios.get(handleRoute(RouteEnum.SWIPE_RANDOM_USER));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async getUserMatches() {
    try {
      const response = await axios.get(handleRoute(RouteEnum.SWIPE_MATCHES));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async likeUser(id) {
    try {
      const reponse =await axios.post(handleRoute(RouteEnum.LIKE_LIST), {target_user_id: id});
      if (reponse.status === 201 && reponse.data?.match) {
          setError({message: 'Vous avez un match !!!'}, 'success');
      }
      return true;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async getUser() {
    try {
      const response = await axios.get(handleRoute(RouteEnum.USER_CURRENT));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return error;
    }
  };

  static async getUserById(id) {
    try {
      const response = await axios.get(handleRoute(RouteEnum.USER_DETAIL, id));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return error;
    }
  };

  static async getUserTags(id) {
    try {
      const response =
          await axios.get(handleRoute(RouteEnum.USER_TAGS_LIST, id));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return error;
    }
  };

  static async updateUser(user, id) {
    try {
      await axios.patch(handleRoute(RouteEnum.USER_DETAIL, id), user, {
        headers: {'Content-Type': 'application/json'},
        withCredentials: true
      });

      setError({message: 'L\'utilisateur a été mis à jour'}, 'success');
      localStorage.setItem('uninitialized', false);
      return true;
    } catch (error) {
      console.error(error);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async addUserTag(tag) {
    try {
      const response =
          await axios.post(handleRoute(RouteEnum.USER_ADD_TAG), tag);
      setError(response.data, 'success');
      return true;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  };

  static async deleteUserTag(tag) {
    try {
      const response = await axios.delete(
          handleRoute(RouteEnum.USER_REMOVE_TAG), {data: tag});
      setError(response.data, 'success');
      return true;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  };

  // tags

  static async getTags() {
    try {
      const response = await axios.get(handleRoute(RouteEnum.TAG_LIST));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return error;
    }
  };

  // token

  static async refreshToken() {
    const refreshToken = localStorage.getItem('refreshToken');
    localStorage.removeItem('accessToken');
    try {
      const response = await axios.post(
          handleRoute(RouteEnum.TOKEN_REFRESH), {'refresh': refreshToken},
          {withCredentials: true});
      if (response.status === 200) {
        localStorage.setItem('accessToken', response.data.access);
        axios.defaults.headers.common['Authorization'] =
            `Bearer ${localStorage.getItem('accessToken')}`;
        return true;
      } else {
        return false;
      }
    } catch (error) {
      return false;
    }
  }

  // images

  static async getPictures() {
    try {
      const response = await axios.get(handleRoute(RouteEnum.PICTURE_LIST));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async getPicturesByUser(id) {
    try {
      const response =
          await axios.get(handleRoute(RouteEnum.USER_PICTURES_LIST, id));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async getPicture(id) {
    const arrayBufferToBase64 = buffer => {
      let binary = '';
      const bytes = new Uint8Array(buffer);
      const len = bytes.byteLength;
      for (let i = 0; i < len; i++) {
          binary += String.fromCharCode(bytes[i]);
      }
      return btoa(binary);
    };

    try {
      const response = await axios.get(
          handleRoute(RouteEnum.PICTURE_DETAIL, id),
          {responseType: 'arraybuffer'});

      return `data:image/jpeg;base64,${arrayBufferToBase64(response.data)}`;
    } catch (error) {
      console.error(error);
      setError(error.response?.data, 'error');
      return error;
    }
  }

  static async addPicture(image) {
    try {
      const response =
          await axios.post(handleRoute(RouteEnum.PICTURE_LIST), image, {
            headers: {'Content-Type': 'multipart/form-data'},
            withCredentials: true
          });

      return response.data.id;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async deletePicture(id) {
    try {
      await axios.delete(handleRoute(RouteEnum.PICTURE_DETAIL, id));
      return true;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  // conversations
  static async getConversation(id) {
    try {
      const response =
          await axios.get(handleRoute(RouteEnum.MESSAGE_CONVERSATION, id));
      return response.data;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }

  static async addMessage(message) {
    try {
      await axios.post(
          handleRoute(RouteEnum.MESSAGE_LIST), message, {withCredentials: true});
      return true;
    } catch (error) {
      console.error(error.response?.data);
      setError(error.response?.data, 'error');
      return false;
    }
  }
}



// utils

const handleRoute = (function() {
  function handleRoute(routeName, id) {
    const route = routes_api[routeName];
    if (!route) {
      throw new Error(`Route with name '${routeName}' not found`);
    }

    let routeUrl = route;
    if (id !== undefined) {
      routeUrl = routeUrl.replace('{id}', id);
    }
    return API_SERVER_URL + routeUrl;
  }
  return handleRoute;
})();