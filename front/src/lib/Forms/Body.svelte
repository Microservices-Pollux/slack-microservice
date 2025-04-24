<script lang="ts">
  import { onMount } from "svelte";
  import { store } from "../../store.svelte";
  import Table from "../../components/Table.svelte";
  import type { Form } from "../../interfaces/Form";
  import { goto } from "@mateothegreat/svelte5-router";

  onMount(() => {
    store.services
      .resource("forms")
      .get()
      .then((data: any) => {
        store.forms = data.forms;
        store.isLoading = false;
      });
  });

  const handleShow = (form: Form): void => {
    store.isLoading = true;
    store.services
      .resource("forms")
      .show(form._id)
      .then((data: any) => {
        store.form = data.form;
        store.isLoading = false;
        goto("fields", { "form-id": form._id });
      });
  };

  const handleDelete = (form: Form): void => {
    store.isLoading = true;
    store.services
      .resource("forms")
      .delete(form._id)
      .then(() => {
        store.services
          .resource("forms")
          .get()
          .then((data: any) => {
            store.forms = data.forms;
            store.isLoading = false;
          });
      });
  };
</script>

{#snippet headers()}
  <th scope="col" class="px-6 py-3"> Nombre </th>
  <th scope="col" class="px-6 py-3"> Actions </th>
{/snippet}

{#snippet rows()}
  {#each store.forms as form}
    <tr class="odd:bg-white even:bg-gray-50 border-gray-200">
      <th scope="col" class="px-6 py-3">
        {form.name}
      </th>
      <th scope="col" class="px-6 py-3">
        <button
          class="text-blue-600 hover:text-blue-900 mr-2"
          onclick={() => handleShow(form)}
        >
          Show
        </button>
        <button
          class="text-red-600 hover:text-red-900"
          onclick={() => handleDelete(form)}
        >
          Delete
        </button>
      </th>
    </tr>
  {/each}
{/snippet}

<div class="px-16 my-6">
  <Table title="Forms" {headers} {rows} />
</div>
