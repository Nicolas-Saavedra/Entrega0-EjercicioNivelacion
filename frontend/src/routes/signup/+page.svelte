<script lang="ts">
	import api from '$lib/api';
	import Signup from '$lib/components/auth/signup.svelte';
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
		const signupData = {
			nombre_usuario: name,
			contrasenia: password
		};
		let signupResponse: AxiosResponse<User>;
		try {
			signupResponse = await api.post(`${PUBLIC_API_URL}/usuarios/`, signupData, {
				validateStatus: (status) => status >= 200 && status <= 300
			});
		} catch (e) {
			toast.error(
				'There is a problem establishing a connection to the database, please try again later'
			);
			return;
		}
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
				"There was an error trying to access the logged in user's data, please try again later"
			);
			return;
		}
		currentAuthTokens.set({
			access_token: loginResponse.data.access_token,
			refresh_token: loginResponse.data.refresh_token
		});
		currentUser.set({
			id: signupResponse.data.id,
			nombre_usuario: signupResponse.data.nombre_usuario,
			imagen_perfil: signupResponse.data.imagen_perfil
		});
		goto('/tasks', { replaceState: true });
	}
</script>

<div class="mt-48 flex justify-center">
	<Signup {onsubmit}></Signup>
</div>
