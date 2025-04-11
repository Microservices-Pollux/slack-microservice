<script lang="ts">
  import type { SelectProps } from '../interfaces/SelectProps';

    let { label = '', value = $bindable(), options = [] }: SelectProps = $props();
</script>

<div>
  <label for="countries_disabled" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{label}</label>
  <select bind:value id="countries_disabled" class="border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
    {#each options as item}
      <option value={item.name}>{item.name}</option>
    {/each}
  </select>
</div>