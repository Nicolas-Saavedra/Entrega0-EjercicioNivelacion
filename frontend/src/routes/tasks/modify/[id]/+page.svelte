<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import * as Select from '$lib/components/ui/select';
	import { page } from '$app/state';
	import api from '$lib/api';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { userTasks } from '../../../../stores/userTasks';
	import { goto } from '$app/navigation';
	import { Undo2 } from 'lucide-svelte';

	const { id } = page.params;

	let taskState: string | null = $state(null);

	async function updateTask() {
		if (taskState) {
			const taskUpdateResponse = await api.put(
				`${PUBLIC_API_URL}/tareas/${id}`,
				{
					estado: taskState
				},
				{
					validateStatus: (status) => status >= 200 && status <= 300
				}
			);
			userTasks.update((currentTasks) => {
				if (currentTasks) {
					return currentTasks.map((task) => {
						if (task.id === Number(id)) {
							return taskUpdateResponse.data;
						}
						return task;
					});
				}
				return null;
			});
			goto('/tasks');
		}
	}

	async function deleteTask() {
		await api.delete(`${PUBLIC_API_URL}/tareas/${id}`, {
			validateStatus: (status) => status >= 200 && status <= 300
		});
		userTasks.update((currentTasks) => {
			if (currentTasks) {
				return currentTasks.filter((task) => task.id !== Number(id));
			}
			return null;
		});
		goto('/tasks');
	}
</script>

<Card.Root>
	<Card.Header class="flex flex-row items-center">
		<div class="grid gap-2">
			<Card.Title>Modificar tarea existente</Card.Title>
			<Card.Description>Puedes cambiar el estado de la tarea a continuacion</Card.Description>
		</div>
		<div class="ml-auto gap-1">
			<Button onclick={() => goto('/tasks')} size="sm" class="ml-auto gap-1">
				Volver
				<Undo2 class="h-4 w-4" />
			</Button>
		</div>
	</Card.Header>
	<Card.Content>
		<Label for="name">Estado</Label>
		<Select.Root
			onSelectedChange={(v) => {
				if (v) taskState = v.value as string;
			}}
		>
			<Select.Trigger class="w-[180px]">
				<Select.Value placeholder="Theme" />
			</Select.Trigger>
			<Select.Content>
				<Select.Item value="sin empezar">"Sin empezar"</Select.Item>
				<Select.Item value="empezada">"Empezada"</Select.Item>
				<Select.Item value="finalizada">"Finalizada"</Select.Item>
			</Select.Content>
		</Select.Root>
		<div class="flew-row mt-4 flex gap-3">
			<Button class="mt-2 w-48" onclick={updateTask}>Modificar tarea</Button>
			<Button class="mt-2 w-48 bg-red-400" onclick={deleteTask}>Eliminar tarea</Button>
		</div>
	</Card.Content>
</Card.Root>
