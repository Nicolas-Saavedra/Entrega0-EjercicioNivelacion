import { writable, type Writable } from 'svelte/store';

type AuthTokenStore = {
        access_token: string,
        refresh_token: string
}

const AUTH_TOKEN_STORE_KEY = "authTokenStore"

export const currentAuthTokens: Writable<AuthTokenStore | null> = writable(
        JSON.parse(localStorage.getItem(AUTH_TOKEN_STORE_KEY) || "null")
);

currentAuthTokens.subscribe(authTokens => {
        localStorage.setItem(AUTH_TOKEN_STORE_KEY, JSON.stringify(authTokens))
})

