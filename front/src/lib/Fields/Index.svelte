<script lang="ts">
  import Form from "./Form.svelte";
  import Body from "./Body.svelte";

  let { route } = $props();
</script>

<div>
  <Form {route} />
  <Body {route} />
</div>
