<script lang="ts">
	import { currentUser } from '../stores/currentUser';
</script>

<h1>Welcome {$currentUser!.nombre_usuario}</h1>
<img src={$currentUser!.imagen_perfil} alt="Imagen perfil usuario" />
