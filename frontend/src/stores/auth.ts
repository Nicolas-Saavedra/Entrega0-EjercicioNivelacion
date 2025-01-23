import { writable, type Writable } from 'svelte/store';

type AuthTokenStore = {
        access_token: string,
        refresh_token: string
}

export const currentAuthTokens: Writable<AuthTokenStore | null> = writable(null);
