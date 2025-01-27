<script lang="ts">
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table';
	import { Bookmark, FilePlus, Pen } from 'lucide-svelte';
	import { goto } from '$app/navigation';
	import { userTasks } from '../../stores/userTasks';

	function toFormattedDate(rawDate: string) {
		const date = new Date(rawDate);
		return `${date.getDate().toString().padStart(2, '0')}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getFullYear().toString().substring(2)}
            ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
	}

	function toUppercaseFirst(text: string) {
		return text.charAt(0).toUpperCase() + text.slice(1);
	}
</script>

{#if $userTasks}
	<Card.Root class="xl:col-span-2">
		<Card.Header class="flex flex-row items-center">
			<div class="grid gap-2">
				<Card.Title>Tareas</Card.Title>
				<Card.Description>En orden de mas reciente a mas antigua</Card.Description>
			</div>
			<div class="ml-auto gap-1">
				<Button onclick={() => goto('/tasks/create')} size="sm" class="ml-auto gap-1">
					Crear nueva tarea
					<FilePlus class="h-4 w-4" />
				</Button>
				<Button onclick={() => goto('/tasks/categories')} size="sm" class="ml-auto gap-1">
					Ver categorias
					<Bookmark class="h-4 w-4" />
				</Button>
			</div>
		</Card.Header>
		<Card.Content>
			<Table.Root>
				<Table.Header>
					<Table.Row>
						<Table.Head>Tarea</Table.Head>
						<Table.Head class="xl:table.-column">Categoria</Table.Head>
						<Table.Head class="xl:table.-column">Creada</Table.Head>
						<Table.Head class="xl:table.-column">Finalizar</Table.Head>
						<Table.Head class="xl:table.-column">Estado</Table.Head>
						<Table.Head></Table.Head>
					</Table.Row>
				</Table.Header>
				<Table.Body>
					{#each $userTasks as task}
						<Table.Row>
							<Table.Cell>
								<div class="max-w-64 font-medium">
									{task.texto_tarea}
								</div>
							</Table.Cell>
							<Table.Cell class="xl:table.-column">
								<Badge class="text-xs" variant="outline"
									>{toUppercaseFirst(task.categoria.nombre)}</Badge
								>
							</Table.Cell>
							<Table.Cell class="md:table.-cell xl:table.-column"
								>{toFormattedDate(task.fecha_creacion)}</Table.Cell
							>
							<Table.Cell class="md:table.-cell xl:table.-column">
								{toFormattedDate(task.fecha_tentativa_finalizacion)}
							</Table.Cell>
							<Table.Cell class="xl:table.-column">
								<Badge class="text-xs" variant="outline">
									{toUppercaseFirst(task.estado)}
									<!-- Quick and dirty capitalization for first letter -->
								</Badge>
							</Table.Cell>
							<Table.Cell class="md:table.-cell xl:table.-column"
								><Button class="size-9 p-2" onclick={() => goto(`/tasks/modify/${task.id}`)}>
									<Pen class="size-3" />
								</Button></Table.Cell
							>
						</Table.Row>
					{/each}
				</Table.Body>
			</Table.Root>
		</Card.Content>
	</Card.Root>
{/if}
