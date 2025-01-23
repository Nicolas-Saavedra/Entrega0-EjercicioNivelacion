<script lang="ts">
	import api from '$lib/api';
	import Login from '$lib/components/auth/login.svelte';
	import { redirect } from '@sveltejs/kit';
	import { currentAuthTokens } from '../../stores/auth';
	import { currentUser } from '../../stores/currentUser';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { goto } from '$app/navigation';

	async function onsubmit(name: string, password: string) {
		const formData = {
			username: name,
			password: password
		};
		const loginResponse = await api.postForm(
			`${PUBLIC_API_URL}/usuarios/iniciar-sesion`,
			formData,
			{
				validateStatus: (status) => status >= 200 && status <= 300
			}
		);
		currentAuthTokens.set({
			access_token: loginResponse.data.access_token,
			refresh_token: loginResponse.data.refresh_token
		});
		const infoResponse = await api.get(`${PUBLIC_API_URL}/usuarios/me`, {
			validateStatus: (status) => status >= 200 && status <= 300
		});
		currentUser.set({
			id: infoResponse.data.id,
			nombre_usuario: infoResponse.data.nombre_usuario,
			imagen_perfil: infoResponse.data.imagen_perfil
		});
		goto('/', { replaceState: true });
	}
</script>

<div class="mt-48 flex justify-center">
	<Login {onsubmit}></Login>
</div>
