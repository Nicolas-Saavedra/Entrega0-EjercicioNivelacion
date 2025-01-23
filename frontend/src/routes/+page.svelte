<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { currentUser } from '../stores/currentUser';
	import api from '$lib/api';
	import * as Avatar from '$lib/components/ui/avatar';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { type Task } from '../types/task';
	import { BookCheck } from 'lucide-svelte';
	import TaskView from '$lib/components/app/taskview.svelte';
	let tasksPromise = $state(
		api
			.get<Task[]>(`${PUBLIC_API_URL}/usuarios/${$currentUser!.id}/tareas`)
			.then((response) => response.data)
	);
</script>

{#await tasksPromise then tasks}
	<div class="grid grid-cols-12">
		<div class="col-span-6 col-start-4 mt-48 flex flex-col justify-center">
			<Card.Root class="mb-2">
				<Card.Header>
					<Card.Title>
						<div class="flex items-center">
							<Avatar.Root class="mr-2">
								<Avatar.Image src={$currentUser!.imagen_perfil} />
							</Avatar.Root>
							Hola de nuevo, {$currentUser!.nombre_usuario}!
						</div>
					</Card.Title>
				</Card.Header>
				<Card.Content>
					<div class="flex items-center">
						<BookCheck class="ml-1 mr-2 size-5 text-slate-500" />
						<Card.Description>
							{#if tasks.length > 0}
								Tienes un total de {tasks.length} tareas por terminar
							{:else}
								No tienes tareas aun en el sistema
							{/if}
						</Card.Description>
					</div>
				</Card.Content>
			</Card.Root>
			<TaskView {tasks} />
		</div>
	</div>
{/await}
