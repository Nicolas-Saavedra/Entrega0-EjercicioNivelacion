import { writable, type Writable } from 'svelte/store';
import type { Category } from '../types/category';

export const taskCategories: Writable<Category[] | null> = writable(null);
