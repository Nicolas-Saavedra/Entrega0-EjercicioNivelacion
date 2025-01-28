<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { currentUser } from '../../stores/currentUser';
	import api from '$lib/api';
	import * as Avatar from '$lib/components/ui/avatar';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { type Task } from '../../types/task';
	import { BookCheck, ImageUp, LogOut } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import { currentAuthTokens } from '../../stores/auth';
	import { goto } from '$app/navigation';
	import { userTasks } from '../../stores/userTasks';
	import { taskCategories } from '../../stores/taskCategories';
	import type { Category } from '../../types/category';
	import type { User } from '../../types/user';

	let { children } = $props();
	let selectedFile: File | null = null;

	async function fillUserTasks() {
		const userTasksResponse = await api.get<Task[]>(
			`${PUBLIC_API_URL}/usuarios/${$currentUser!.id}/tareas`,
			{
				validateStatus: (status) => status >= 200 && status <= 300
			}
		);
		userTasks.set(userTasksResponse.data);
	}

	async function fillCategories() {
		const categoriesResponse = await api.get<Category[]>(`${PUBLIC_API_URL}/categorias`, {
			validateStatus: (status) => status >= 200 && status <= 300
		});
		taskCategories.set(categoriesResponse.data);
	}

	async function changeProfilePicture() {
		const imageFileFormData = new FormData();
		imageFileFormData.append('file', selectedFile!);

		const profileUpdateResponse = await api.put<User>(
			`${PUBLIC_API_URL}/usuarios/actualizar-perfil`,
			imageFileFormData,
			{
				validateStatus: (status) => status >= 200 && status <= 300,
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			}
		);
		currentUser.set(profileUpdateResponse.data);
	}

	function closeSession() {
		currentUser.set(null);
		currentAuthTokens.set(null);
		goto('/login');
	}

	function triggerFileInput() {
		const fileInput = document.getElementById('fileInput')!;
		fileInput.click(); // Programmatically click the hidden file input
	}

	function handleFileChange(event: Event) {
		selectedFile = (event.target as HTMLInputElement).files![0];
		if (selectedFile) {
			changeProfilePicture(); // Automatically upload the file after selection
		}
	}

	fillUserTasks();
	fillCategories();
</script>

<input
	id="fileInput"
	type="file"
	onchange={handleFileChange}
	accept="image/*"
	style="display: none;"
/>

{#if $userTasks && $currentUser}
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
								<Button onclick={triggerFileInput}
									>Cambiar imagen perfil<ImageUp class="ml-2 size-4" /></Button
								>
								<Button onclick={closeSession}>Cerrar sesión <LogOut class="ml-2 size-4" /></Button>
							</div>
						</div>
					</Card.Title>
				</Card.Header>
				<Card.Content>
					<div class="flex items-center">
						<BookCheck class="ml-1 mr-2 size-5 text-slate-500" />
						<Card.Description>
							{#if $userTasks.length > 1}
								Tienes un total de {$userTasks.length} tareas por terminar
							{:else if $userTasks.length == 1}
								Tienes 1 tarea por terminar
							{:else}
								No tienes tareas aun en el sistema
							{/if}
						</Card.Description>
					</div>
				</Card.Content>
			</Card.Root>
			{@render children()}
		</div>
	</div>
{/if}
