<script lang="ts">
  import type { Field } from "../interfaces/Field";
  import Table from "../components/Table.svelte";
  import { store } from "../store.svelte";

  let fields: Field[] = $state([]);

  $effect(() => {
    store.services
      .resource("fields")
      .get()
      .then((data: any) => {
        fields = data.fields;
      });
  });
</script>

{#snippet headers()}
  <th scope="col" class="px-6 py-3"> Key </th>
  <th scope="col" class="px-6 py-3"> Value </th>
  <th scope="col" class="px-6 py-3"> Type </th>
{/snippet}

{#snippet rows()}
  {#each fields as field}
    <tr class="odd:bg-white even:bg-gray-50 border-gray-200">
      <th scope="col" class="px-6 py-3">
        {field.key}
      </th>
      <th scope="col" class="px-6 py-3">
        {field.value}
      </th>
      <th scope="col" class="px-6 py-3">
        {field.type}
      </th>
    </tr>
  {/each}
{/snippet}

<div class="px-16">
  <Table title="Fields" {headers} {rows} />
</div>
