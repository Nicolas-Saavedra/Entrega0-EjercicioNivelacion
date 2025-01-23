<script lang="ts">
	import { redirect } from '@sveltejs/kit';
	import { currentUser } from '../stores/currentUser';
	import { get } from 'svelte/store';

	const user = get(currentUser)!;
</script>

<h1>Welcome {user.nombre_usuario}</h1>
<img src={user.imagen_perfil} alt="Imagen perfil usuario" />
