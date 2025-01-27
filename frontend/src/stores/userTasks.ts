import { writable, type Writable } from 'svelte/store';
import type { Task } from '../types/task';

export const userTasks: Writable<Task[] | null> = writable(null);
