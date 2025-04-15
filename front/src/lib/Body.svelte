<script lang="ts">
  import type { Field } from "../interfaces/Field";
  import { onMount } from "svelte";
  import { store } from "../store.svelte";
  import Table from "../components/Table.svelte";

  onMount(() => {
    store.services
      .resource("fields")
      .get()
      .then((data: any) => {
        store.fields = data.fields;
        store.isLoading = false;
      });
  });

  const handleDelete = (field: Field): void => {
    store.isLoading = true;
    store.services
      .resource("fields")
      .delete(field.id)
      .then(() => {
        store.services
          .resource("fields")
          .get()
          .then((data: any) => {
            store.fields = data.fields;
            store.isLoading = false;
          });
      });
  };
</script>

{#snippet headers()}
  <th scope="col" class="px-6 py-3"> Key </th>
  <th scope="col" class="px-6 py-3"> Value </th>
  <th scope="col" class="px-6 py-3"> Type </th>
  <th scope="col" class="px-6 py-3"> Actions </th>
{/snippet}

{#snippet rows()}
  {#each store.fields as field}
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
      <th scope="col" class="px-6 py-3">
        <button
          class="text-red-600 hover:text-red-900"
          onclick={() => handleDelete(field)}
        >
          Delete
        </button>
      </th>
    </tr>
  {/each}
{/snippet}

<div class="px-16 my-6">
  <Table title="Fields" {headers} {rows} />
</div>
