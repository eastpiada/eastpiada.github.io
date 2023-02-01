import { defineConfig } from 'vite'
import { sveltekit } from '@sveltejs/kit/vite';

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
};

export default defineConfig ({
	base: "/eastpiada.github.io/",
	plugins: [svelte()],
});
