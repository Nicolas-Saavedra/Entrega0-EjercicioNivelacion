<script lang="ts">
	let value = $state('');

	// Generate an array of hours from 00 to 23
	const hours = Array.from({ length: 24 }, (_, i) => i.toString().padStart(2, '0'));

	type PresetHourProps = {
		onSelect: (value: number) => void;
		label: string;
	};

	$effect(() => {
		if (value) {
			onSelect(Number(value));
		}
	});

	const { onSelect, label }: PresetHourProps = $props();
</script>

<div class="hour-picker">
	<label for="hour-select" class="block text-sm font-medium">{label}</label>
	<select
		bind:value
		id="hour-select"
		class="mt-1 block w-full rounded-md border border-gray-200 bg-white py-2 pl-3 pr-10 text-base focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
	>
		{#each hours as hour}
			<option value={hour}>{hour}:00</option>
		{/each}
	</select>
</div>

<style>
	.hour-picker {
		max-width: 200px;
	}
</style>
