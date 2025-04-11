<script lang="ts">
  import type { TableProps } from "../interfaces/TableProps";

  let { title, headers, rows }: TableProps = $props();
</script>

<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
  <h2 class="p-5 text-lg text-center font-semibold text-gray-900">
    {title}
  </h2>
  <table
    class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400"
  >
    <thead
      class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
    >
      <tr>
        {@render headers()}
      </tr>
    </thead>
    <tbody>
      {@render rows()}
    </tbody>
  </table>
</div>
