<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import api from '$lib/api';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { goto } from '$app/navigation';
	import Textarea from '$lib/components/ui/textarea/textarea.svelte';
	import type { Category } from '../../../../types/category';
	import { taskCategories } from '../../../../stores/taskCategories';
	import { Undo2 } from 'lucide-svelte';

	let categoryName: string | null = $state(null);
	let categoryDescription: string | null = $state(null);

	async function createCategory() {
		if (categoryName && categoryDescription) {
			const createCategoryResponse = await api.post<Category>(
				`${PUBLIC_API_URL}/categorias`,
				{
					nombre: categoryName,
					descripcion: categoryDescription
				},
				{
					validateStatus: (status) => status >= 200 && status <= 300
				}
			);
			taskCategories.update((current) =>
				current ? [...current, createCategoryResponse.data] : null
			);
			goto('/tasks/categories');
		}
	}
</script>

<Card.Root>
	<Card.Header class="flex flex-row items-center">
		<div class="grid gap-2">
			<Card.Title>Crear nueva categoria</Card.Title>
			<Card.Description>Clasifica tus tareas por medio de tags a continuacion</Card.Description>
		</div>
		<div class="ml-auto gap-1">
			<Button onclick={() => goto('/tasks/categories')} size="sm" class="ml-auto gap-1">
				Volver
				<Undo2 class="h-4 w-4" />
			</Button>
		</div>
	</Card.Header>
	<Card.Content>
		<div class="grid gap-6">
			<div class="grid gap-3">
				<Label for="name">Nombre de la categoria</Label>
				<Input id="name" type="text" class="w-full" bind:value={categoryName} />
			</div>
			<div class="grid gap-3">
				<Label for="name">Descripcion de la categoria</Label>
				<Textarea id="description" class="w-full" bind:value={categoryDescription} />
			</div>
			<Button class="mt-2 w-48" onclick={createCategory}>Crear nueva categoria</Button>
		</div>
	</Card.Content>
</Card.Root>
