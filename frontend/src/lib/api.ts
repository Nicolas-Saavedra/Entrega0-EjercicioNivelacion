import axios from 'axios';
import { currentAuthTokens } from '../stores/auth';
import { PUBLIC_API_URL } from '$env/static/public';

let accessToken: string | undefined;

currentAuthTokens.subscribe(tokens => {
  accessToken = tokens?.access_token;
});

const api = axios.create({
  baseURL: PUBLIC_API_URL,
});

api.interceptors.request.use(
  config => {
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`; // Attach the access token
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default api;
