<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import '../app.css';
	import { currentUser } from '../stores/currentUser';
	import { get } from 'svelte/store';

	let { children } = $props();

	const maybeUser = get(currentUser);
	const publicRoutes = ['/login', '/signup'];
	const isLoggedInPrivateRoute = maybeUser || publicRoutes.includes(page.url.pathname);
	const isLoggedInPublicRoute = maybeUser && publicRoutes.includes(page.url.pathname);

	if (!isLoggedInPrivateRoute) {
		goto('/login');
	}
	if (isLoggedInPublicRoute) {
		goto('/');
	}
</script>

{#if isLoggedInPrivateRoute || !isLoggedInPublicRoute}
	{@render children()}
{/if}
