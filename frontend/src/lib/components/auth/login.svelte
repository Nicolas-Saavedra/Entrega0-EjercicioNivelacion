<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
</script>

<Card.Root class="w-full max-w-sm">
	<Card.Header>
		<Card.Title class="text-2xl">Login</Card.Title>
		<Card.Description
			>Ingrese por favor su nombre de usuario y contraseña para ingresar</Card.Description
		>
	</Card.Header>
	<Card.Content class="grid gap-4">
		<div class="grid gap-2">
			<Label for="email">Nombre de usuario</Label>
			<Input id="email" type="email" placeholder="John Doe" required />
		</div>
		<div class="grid gap-2">
			<Label for="password">Contraseña</Label>
			<Input id="password" type="password" placeholder="************" required />
		</div>
		<a class="text-center text-sm" href="/signup">Aun no tengo una cuenta</a>
	</Card.Content>
	<Card.Footer>
		<Button class="w-full">Ingresar</Button>
	</Card.Footer>
</Card.Root>
