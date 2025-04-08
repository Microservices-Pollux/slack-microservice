<script lang="ts">
  import Input from '../components/Input.svelte'
  import Button from '../components/Button.svelte'
  import Select from '../components/Select.svelte';
  import { Item }  from '../interfaces/Item';
  
  let key: string = $state('')
  let value: string = $state('')
  let type: string = $state('')

  const handleTypeChange = (item: Item) => {
    console.log(item)
    type = item.name
  }

  const submit = (e: Event) => {
    // TODO handle form submission
    e.preventDefault()
  }
</script>

<form>
  <div class="mt-10 py-10 px-16 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-3">
    <div> 
      <Input 
        label="Key"
        name="key"
        type="text"
        bind:value={key}
        />
    </div>
    <div> 
      <Input
        label="Value"
        name="value"
        type="text"
        bind:value={value}
        />
    </div>
    <div> 
      <Select 
        label="Type"
        name="type"
        value={type}
        onClick={handleTypeChange}
        /> 
    </div>
    <div class="col-span-3 flex items-center justify-end">
      <Button label="Guardar" onclick={submit} />
    </div>
  </div>
</form>
  