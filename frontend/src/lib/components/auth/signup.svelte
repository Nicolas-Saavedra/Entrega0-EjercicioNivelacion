<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	let name = $state('');
	let password = $state('');

	type SubmitProps = {
		onsubmit: (name: string, password: string) => void;
	};

	let { onsubmit }: SubmitProps = $props();
</script>

<Card.Root class="w-full max-w-sm">
	<Card.Header>
		<Card.Title class="text-2xl">Registrar</Card.Title>
		<Card.Description
			>Para crear una cuenta, por favor diligencie los campos a continuacion</Card.Description
		>
	</Card.Header>
	<Card.Content class="grid gap-4">
		<div class="grid gap-2">
			<Label for="email">Nombre de usuario</Label>
			<Input id="email" type="email" placeholder="John Doe" bind:value={name} required />
		</div>
		<div class="grid gap-2">
			<Label for="password">Contraseña</Label>
			<Input
				id="password"
				type="password"
				placeholder="************"
				bind:value={password}
				required
			/>
		</div>
		<a class="text-center text-sm" href="/login">Ya tengo una cuenta</a>
	</Card.Content>
	<Card.Footer>
		<Button class="w-full" onclick={() => onsubmit(name, password)}>Crear cuenta</Button>
	</Card.Footer>
</Card.Root>
