import axios from 'axios';
import { currentAuthTokens } from '../stores/auth';
import { PUBLIC_API_URL } from '$env/static/public';

let accessToken: string | undefined;
let refreshToken: string | undefined;

currentAuthTokens.subscribe(tokens => {
  accessToken = tokens?.access_token;
  refreshToken = tokens?.refresh_token;
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

// Function to refresh the access token
const refreshAccessToken = async () => {
  const response = await axios.post(`${PUBLIC_API_URL}/usuarios/refrescar-token`, {
    refresh_token: refreshToken, // Assuming the refresh token is stored
  });

  const newAccessToken = response.data.access_token;

  currentAuthTokens.set({
    access_token: newAccessToken,
    refresh_token: refreshToken!,
  });

  return newAccessToken;
};


api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    // TODO: This error code should be changed whenever token expires are
    // handled different from invalid tokens
    if (error.response?.status === 403 && accessToken && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const newAccessToken = await refreshAccessToken();
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

        return api(originalRequest);
      } catch (refreshError) {
        currentAuthTokens.set(null);
        return Promise.reject(refreshError);
      }
    }

    // If the error is not a 403 or there's no token, reject the error
    return Promise.reject(error);
  }
);


export default api;
