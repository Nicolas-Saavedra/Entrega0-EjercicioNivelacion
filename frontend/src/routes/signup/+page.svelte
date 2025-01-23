<script lang="ts">
	import api from '$lib/api';
	import Signup from '$lib/components/auth/signup.svelte';
	import { currentAuthTokens } from '../../stores/auth';
	import { currentUser } from '../../stores/currentUser';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { goto } from '$app/navigation';

	async function onsubmit(name: string, password: string) {
		const formData = {
			username: name,
			password: password
		};
		const signupData = {
			nombre_usuario: name,
			contrasenia: password
		};
		const signupResponse = await api.post(`${PUBLIC_API_URL}/usuarios/`, signupData, {
			validateStatus: (status) => status >= 200 && status <= 300
		});
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
		currentUser.set({
			id: signupResponse.data.id,
			nombre_usuario: signupResponse.data.nombre_usuario,
			imagen_perfil: signupResponse.data.imagen_perfil
		});
		goto('/', { replaceState: true });
	}
</script>

<div class="mt-48 flex justify-center">
	<Signup {onsubmit}></Signup>
</div>
