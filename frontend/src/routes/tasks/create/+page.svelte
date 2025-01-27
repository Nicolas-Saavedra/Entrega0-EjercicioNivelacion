<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import type { DateValue } from '@internationalized/date';
	import PresetCalendar from '$lib/components/ui/preset-calendar/presetCalendar.svelte';
	import PresetHour from '$lib/components/ui/preset-hour/presetHour.svelte';
	import { Button } from '$lib/components/ui/button';
	import * as Select from '$lib/components/ui/select';
	import api from '$lib/api';
	import { PUBLIC_API_URL } from '$env/static/public';
	import type { Category } from '../../../types/category';
	import type { Task } from '../../../types/task';
	import { currentUser } from '../../../stores/currentUser';
	import { userTasks } from '../../../stores/userTasks';
	import { goto } from '$app/navigation';
	import { taskCategories } from '../../../stores/taskCategories';

	let taskContent: string | null = $state(null);
	let date: DateValue | null = $state(null);
	let hour: number | null = $state(null);
	let category: Category | null = $state(null);

	function setCategory(name: string) {
		if ($taskCategories)
			category = $taskCategories.find((innerCategory) => innerCategory.nombre == name) || null;
	}

	async function createTask() {
		if (taskContent && date && hour && category) {
			const jsDate = date.toDate('UTC-5');
			jsDate.setHours(hour);
			const taskToCreate: Omit<Task, 'categoria' | 'id'> = {
				texto_tarea: taskContent!,
				fecha_creacion: new Date().toISOString(),
				fecha_tentativa_finalizacion: jsDate.toISOString(),
				estado: 'activa',
				id_Usuario: $currentUser!.id,
				id_Categoria: category.id
			};
			const createTaskResponse = await api.post(`${PUBLIC_API_URL}/tareas`, taskToCreate, {
				validateStatus: (status) => status >= 200 && status <= 300
			});
			userTasks.update((current) => (current ? [...current, createTaskResponse.data] : null));
			goto('/tasks');
		}
	}
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>Crear nueva tarea</Card.Title>
		<Card.Description>Puedes cambiar estos valores en el menu principal despues</Card.Description>
	</Card.Header>
	<Card.Content>
		<div class="grid gap-6">
			<div class="grid gap-3">
				<Label for="name">Tarea</Label>
				<Input id="name" type="text" class="w-full" bind:value={taskContent} />
			</div>
			<div class="grid">
				<div class="flex flex-row items-center gap-8">
					<div>
						<p class="text-sm">Fecha a finalizar</p>
						<PresetCalendar onSelect={(innerDate) => (date = innerDate)} />
					</div>
					<PresetHour label="Hora a finalizar" onSelect={(innerHour) => (hour = innerHour)} />
				</div>
			</div>
			<div class="grid gap-3">
				<Label for="name">Categoria</Label>
				<Select.Root
					onSelectedChange={(v) => {
						if (v) setCategory(v.value as string);
					}}
				>
					<Select.Trigger class="w-[180px]">
						<Select.Value placeholder="Theme" />
					</Select.Trigger>
					{#if $taskCategories}
						<Select.Content>
							{#each $taskCategories as category}
								<Select.Item value={category.nombre}>{category.nombre}</Select.Item>
							{/each}
						</Select.Content>
					{/if}
				</Select.Root>
			</div>
			<Button class="mt-2 w-48" onclick={createTask}>Crear nueva tarea</Button>
		</div>
	</Card.Content>
</Card.Root>
