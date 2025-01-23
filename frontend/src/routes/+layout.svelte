<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import '../app.css';
	import { currentUser } from '../stores/currentUser';
	import { get } from 'svelte/store';

	let { children } = $props();

	const maybeUser = get(currentUser);
	const publicRoutes = ['/login', '/signup'];
	const isLoggedIn = maybeUser || publicRoutes.includes(page.url.pathname);

	if (!isLoggedIn) {
		goto('/login');
	}
</script>

{#if isLoggedIn}
	{@render children()}
{/if}
