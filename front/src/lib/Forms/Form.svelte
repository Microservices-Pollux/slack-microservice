<script lang="ts">
  import Input from "../../components/Input.svelte";
  import Button from "../../components/Button.svelte";
  import { store } from "../../store.svelte";

  let name: string = $state("");

  const submit = async (e: Event) => {
    store.isLoading = true;
    store.services
      .resource("forms")
      .create({ name })
      .then(() => {
        name = "";
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

<div class="mt-10 px-16 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-1">
  <div>
    <Input label="Name" name="name" type="text" bind:value={name} />
  </div>
  <div class="col-span-3 flex items-center justify-end">
    <Button label="Guardar" onClick={submit} />
  </div>
</div>
