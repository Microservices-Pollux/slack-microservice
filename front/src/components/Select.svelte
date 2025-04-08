<script lang="ts">
   import { INPUT_TYPES } from '../constants/inputTypes';  
   import { SelectProps } from '../interfaces/SelectProps';

    let { label, value, onClick }: SelectProps = $props();
</script>

<div>
  <label class="block text-sm/6 font-medium text-gray-900">{label}</label>
  <div class="relative mt-2">
    <button type="button" class="grid w-full cursor-default grid-cols-1 rounded-md bg-white py-1.5 pr-2 pl-3 text-left text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" aria-haspopup="listbox" aria-expanded="true" aria-labelledby="listbox-label">
      <span class="col-start-1 row-start-1 flex items-center gap-3 pr-6">
        <span class="block truncate">{value}</span>
      </span>
    </button>

    <ul class="absolute z-10 mt-1 max-h-56 w-full overflow-auto rounded-md bg-white py-1 text-base ring-1 shadow-lg ring-black/5 focus:outline-hidden sm:text-sm" tabindex="-1" role="listbox" aria-labelledby="listbox-label" aria-activedescendant="listbox-option-3">
        {#each INPUT_TYPES as item}
            <li class="relative cursor-default py-2 pr-9 pl-3 text-gray-900 select-none" onclick={() => onClick(item)}>
                <div class="flex items-center">
                    <span class="ml-3 block truncate font-normal">{item.name}</span>
                </div>
            </li>
        {/each}
    </ul>
  </div>
</div>