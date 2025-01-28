<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import '../app.css';
	import { currentUser } from '../stores/currentUser';
	import { Toaster } from '$lib/components/ui/sonner';

	let { children } = $props();

	const publicRoutes = ['/login', '/signup'];
	const isLoggedInPrivateRoute = $currentUser || publicRoutes.includes(page.url.pathname);
	const isLoggedInPublicRoute = $currentUser && publicRoutes.includes(page.url.pathname);

	if (page.url.pathname === '/') {
		goto($currentUser ? '/tasks' : '/login');
	}

	if (!isLoggedInPrivateRoute) {
		goto('/login');
	}
	if (isLoggedInPublicRoute) {
		goto('/tasks');
	}
</script>

<Toaster />
{#if isLoggedInPrivateRoute || !isLoggedInPublicRoute}
	{@render children()}
{/if}
