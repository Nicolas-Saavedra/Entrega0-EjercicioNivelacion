import { redirect, type LoadEvent } from '@sveltejs/kit';
import { currentUser } from '../stores/currentUser';
import { get } from 'svelte/store';

export async function load(event: LoadEvent) {

        const isLoginRoute = event.url.pathname === '/login' || event.url.pathname === '/signup';

        if (!get(currentUser) && !isLoginRoute) {
                redirect(302, '/login');
        }

        return {};
}
