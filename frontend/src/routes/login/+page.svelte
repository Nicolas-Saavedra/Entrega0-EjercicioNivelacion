<script lang="ts">
	import api from '$lib/api';
	import Login from '$lib/components/auth/login.svelte';
	import { currentAuthTokens } from '../../stores/auth';
	import { currentUser } from '../../stores/currentUser';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { goto } from '$app/navigation';
	import { toast } from 'svelte-sonner';
	import type { AxiosResponse } from 'axios';
	import type { User } from '../../types/user';

	type JWTLogin = {
		access_token: string;
		refresh_token: string;
	};

	async function onsubmit(name: string, password: string) {
		const formData = {
			username: name,
			password: password
		};
		let loginResponse: AxiosResponse<JWTLogin>;
		try {
			loginResponse = await api.postForm<JWTLogin>(
				`${PUBLIC_API_URL}/usuarios/iniciar-sesion`,
				formData,
				{
					validateStatus: (status) => status >= 200 && status <= 300
				}
			);
		} catch (e) {
			toast.error(
				'Could not log into the application with the current credentials, please try again'
			);
			return;
		}
		currentAuthTokens.set({
			access_token: loginResponse.data.access_token,
			refresh_token: loginResponse.data.refresh_token
		});
		let infoResponse: AxiosResponse<User>;
		try {
			infoResponse = await api.get<User>(`${PUBLIC_API_URL}/usuarios/me`, {
				validateStatus: (status) => status >= 200 && status <= 300
			});
		} catch (e) {
			toast.error(
				"There was an error trying to access the logged in user's data, please try again later"
			);
			return;
		}
		currentUser.set({
			id: infoResponse.data.id,
			nombre_usuario: infoResponse.data.nombre_usuario,
			imagen_perfil: infoResponse.data.imagen_perfil
		});
		goto('/tasks', { replaceState: true });
	}
</script>

<div class="mt-48 flex justify-center">
	<Login {onsubmit}></Login>
</div>
