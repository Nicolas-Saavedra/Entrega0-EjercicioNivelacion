<script lang="ts">
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table';
	import { Bookmark, FilePlus, Pen } from 'lucide-svelte';
	import type { Task } from '../../../types/task';

	type TaskViewProps = {
		tasks: Task[];
	};

	const { tasks } = $props();
</script>

<Card.Root class="xl:col-span-2">
	<Card.Header class="flex flex-row items-center">
		<div class="grid gap-2">
			<Card.Title>Tareas</Card.Title>
			<Card.Description>En orden de mas reciente a mas antigua</Card.Description>
		</div>
		<div class="ml-auto gap-1">
			<Button href="##" size="sm" class="ml-auto gap-1">
				Crear nueva tarea
				<FilePlus class="h-4 w-4" />
			</Button>
			<Button href="##" size="sm" class="ml-auto gap-1">
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
				<Table.Row>
					<Table.Cell>
						<div class="max-w-64 font-medium">
							Lorem ipsum dolor, sit amet consectetur adipisicing elit. Beatae, ipsam.
						</div>
					</Table.Cell>
					<Table.Cell class="xl:table.-column">
						<Badge class="text-xs" variant="outline">Approved</Badge>
					</Table.Cell>
					<Table.Cell class="md:table.-cell xl:table.-column">2023-06-23</Table.Cell>
					<Table.Cell class="md:table.-cell xl:table.-column">2023-06-23</Table.Cell>
					<Table.Cell class="xl:table.-column">
						<Badge class="text-xs" variant="outline">Approved</Badge>
					</Table.Cell>
					<Table.Cell class="md:table.-cell xl:table.-column"
						><Button class="size-9 p-2">
							<Pen class="size-3" />
						</Button></Table.Cell
					>
				</Table.Row>
			</Table.Body>
		</Table.Root>
	</Card.Content>
</Card.Root>
