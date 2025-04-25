<script lang="ts">
  import Fields from "./lib/Fields/Index.svelte";
  import Forms from "./lib/Forms/Index.svelte";
  import Navbar from "./lib/Navbar/Index.svelte";
  import Loader from "./components/Loader.svelte";
  import { store } from "./store.svelte";
  import { Router, type RouteConfig } from "@mateothegreat/svelte5-router";

  const routes: RouteConfig[] = [
    {
      component: Forms,
    },
    {
      path: "/fields",
      component: Fields,
      props: { "form-id": 0 },
    },
  ];
</script>

{#if store.isLoading}
  <div
    class="fixed inset-0 bg-gray-900/50 flex items-center justify-center z-50"
  >
    <Loader />
  </div>
{/if}

<Navbar />
<Router {routes} />
