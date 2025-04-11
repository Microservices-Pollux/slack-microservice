<script lang="ts">
    import type { ButtonProps } from '../interfaces/ButtonProps';
    let { label, onClick }: ButtonProps = $props();
</script>

<button onclick={onClick} class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
    {label}
</button>