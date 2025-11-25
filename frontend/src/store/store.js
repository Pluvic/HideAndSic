// This file defines a Svelte writable store to manage the current page state
import { writable } from 'svelte/store';

export const currentPage = writable('analyze');