<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { currentUser } from '../stores/currentUser';
	import api from '$lib/api';
	import * as Avatar from '$lib/components/ui/avatar';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { type Task } from '../types/task';
	import { BookCheck, LogOut } from 'lucide-svelte';
	import TaskView from '$lib/components/app/taskview.svelte';
	import { Button } from '$lib/components/ui/button';
	import { currentAuthTokens } from '../stores/auth';
	import { goto } from '$app/navigation';

	let tasksPromise = $state(
		api
			.get<Task[]>(`${PUBLIC_API_URL}/usuarios/${$currentUser!.id}/tareas`)
			.then((response) => response.data)
	);

	function onCreateTask() {}
	function onViewCategories() {}
	function onEditTask(task: Task) {}
	function closeSession() {
		currentUser.set(null);
		currentAuthTokens.set(null);
		goto('/login');
	}
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
							<div class="ml-auto gap-1">
								<Button onclick={closeSession}>Cerrar sesión <LogOut class="ml-2 size-4" /></Button>
							</div>
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
			<TaskView {tasks} {onCreateTask} {onViewCategories} {onEditTask} />
		</div>
	</div>
{/await}
