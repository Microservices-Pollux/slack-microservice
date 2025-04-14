<script lang="ts">
  import Form from "./lib/Form.svelte";
  import Body from "./lib/Body.svelte";
  import Loader from "./components/Loader.svelte";
  import { store } from "./store.svelte";
</script>

<main>
  {#if store.isLoading}
    <div
      class="fixed inset-0 bg-gray-900/50 flex items-center justify-center z-50"
    >
      <Loader />
    </div>
  {/if}

  <Form />
  <Body />
</main>
