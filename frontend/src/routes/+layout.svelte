<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import '../app.css';
	import { currentUser } from '../stores/currentUser';

	let { children } = $props();

	const publicRoutes = ['/login', '/signup'];
	const isLoggedInPrivateRoute = $currentUser || publicRoutes.includes(page.url.pathname);
	const isLoggedInPublicRoute = $currentUser && publicRoutes.includes(page.url.pathname);

	if (!isLoggedInPrivateRoute) {
		goto('/login');
	}
	if (isLoggedInPublicRoute) {
		goto('/tasks');
	}
</script>

{#if isLoggedInPrivateRoute || !isLoggedInPublicRoute}
	{@render children()}
{/if}
