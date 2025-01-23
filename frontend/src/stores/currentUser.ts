import { writable, type Writable } from 'svelte/store';
import type { User } from '../types/user';

const CURRENT_USER_STORE_KEY = "currentUserStore"

export const currentUser: Writable<User | null> = writable(
        JSON.parse(localStorage.getItem(CURRENT_USER_STORE_KEY) || "null")
);

currentUser.subscribe(user => {
        localStorage.setItem(CURRENT_USER_STORE_KEY, JSON.stringify(user))
})

