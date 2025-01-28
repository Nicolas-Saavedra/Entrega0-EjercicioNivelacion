<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table';
	import { BookmarkPlus, Trash, Undo2 } from 'lucide-svelte';
	import { taskCategories } from '../../../stores/taskCategories';
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import { PUBLIC_API_URL } from '$env/static/public';

	async function deleteCategory(id: number) {
		await api.delete(`${PUBLIC_API_URL}/categorias/${id}`, {
			validateStatus: (status) => status >= 200 && status <= 300
		});
		taskCategories.update((currentCategories) => {
			if (currentCategories) {
				return currentCategories.filter((category) => category.id !== Number(id));
			}
			return null;
		});
		goto('/tasks/categories');
	}
</script>

<Card.Root>
	<Card.Header class="flex flex-row items-center">
		<div class="grid gap-2">
			<Card.Title>Categorias</Card.Title>
			<Card.Description>En orden alfabetico</Card.Description>
		</div>
		<div class="ml-auto gap-1">
			<Button onclick={() => goto('/tasks/categories/create')} size="sm" class="ml-auto gap-1">
				Crear nueva categoria
				<BookmarkPlus class="h-4 w-4" />
			</Button>
			<Button onclick={() => goto('/tasks')} size="sm" class="ml-auto gap-1">
				Volver
				<Undo2 class="h-4 w-4" />
			</Button>
		</div>
	</Card.Header>
	<Card.Content>
		<Table.Root>
			<Table.Header>
				<Table.Row>
					<Table.Head class="w-32">Nombre</Table.Head>
					<Table.Head>Descripcion</Table.Head>
					<Table.Head class="w-4"></Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#if $taskCategories}
					{#each $taskCategories as category}
						<Table.Row>
							<Table.Cell class="font-medium">{category.nombre}</Table.Cell>
							<Table.Cell>{category.descripcion}</Table.Cell>
							<Table.Cell>
								<Button class="size-9 bg-red-400 p-2" onclick={() => deleteCategory(category.id)}>
									<Trash class="size-4" />
								</Button>
							</Table.Cell>
						</Table.Row>
					{/each}
				{/if}
			</Table.Body>
		</Table.Root>
	</Card.Content>
</Card.Root>
