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
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>Modificar tarea existente</Card.Title>
		<Card.Description>Puedes cambiar el estado de la tarea a continuacion</Card.Description>
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
		<Button class="mt-2 w-48" onclick={updateTask}>Modificar tarea</Button>
	</Card.Content>
</Card.Root>
