<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	import type { DateValue } from '@internationalized/date';
	import type { Task } from '../../../types/task';
	import PresetCalendar from '../ui/preset-calendar/presetCalendar.svelte';

	type TaskViewProps = {
		tasks: Task[];
	};

	let date: DateValue | null = $state(null);

	const { tasks } = $props();
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>Product Details</Card.Title>
		<Card.Description>Lipsum dolor sit amet, consectetur adipiscing elit</Card.Description>
	</Card.Header>
	<Card.Content>
		<div class="grid gap-6">
			<div class="grid gap-3">
				<Label for="name">Tarea</Label>
				<Input id="name" type="text" class="w-full" />
			</div>
			<div class="grid gap-3">
				<p class="text-sm">Fecha a finalizar</p>
				<div class="flex flex-row">
					<PresetCalendar onSelect={(innerDate) => (date = innerDate)} />
				</div>
			</div>
		</div>
	</Card.Content>
</Card.Root>
