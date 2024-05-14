<script lang="ts">
  export let data; // pre-loaded data
  import SchoolView from '$lib/components/SchoolView.svelte';
</script>
<div class="flex h-screen p-3 items-start">
  <SchoolView schoolList={data.props.schoolList} />
</div>
