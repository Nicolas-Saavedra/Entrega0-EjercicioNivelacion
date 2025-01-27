<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import PresetCalendar from '$lib/components/ui/preset-calendar/presetCalendar.svelte';
	import PresetHour from '$lib/components/ui/preset-hour/presetHour.svelte';
	import { Button } from '$lib/components/ui/button';
	import * as Select from '$lib/components/ui/select';
	import api from '$lib/api';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { userTasks } from '../../../../stores/userTasks';
	import { goto } from '$app/navigation';
	import { taskCategories } from '../../../../stores/taskCategories';
	import Textarea from '$lib/components/ui/textarea/textarea.svelte';

	let categoryName: string | null = $state(null);
	let categoryDescription: string | null = $state(null);

	async function createCategory() {
		if (categoryName && categoryDescription) {
			const createTaskResponse = await api.post(
				`${PUBLIC_API_URL}/categorias`,
				{
					nombre: categoryName,
					descripcion: categoryDescription
				},
				{
					validateStatus: (status) => status >= 200 && status <= 300
				}
			);
			userTasks.update((current) => (current ? [...current, createTaskResponse.data] : null));
			goto('/tasks');
		}
	}
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>Crear nueva categoria</Card.Title>
		<Card.Description>Clasifica tus tareas por medio de tags a continuacion</Card.Description>
	</Card.Header>
	<Card.Content>
		<div class="grid gap-6">
			<div class="grid gap-3">
				<Label for="name">Nombre de la categoria</Label>
				<Input id="name" type="text" class="w-full" bind:value={categoryName} />
			</div>
			<div class="grid gap-3">
				<Label for="name">Descripcion de la categoria</Label>
				<Textarea id="description" class="w-full" bind:value={categoryName} />
			</div>
			<Button class="mt-2 w-48">Crear nueva categoria</Button>
		</div>
	</Card.Content>
</Card.Root>
