<script lang="ts">
  import { type ISchoolInfo } from "$lib/interfaces";
  import School from "$lib/components/School.svelte";
  export let schoolList: ISchoolInfo[];
</script>

<div class="flex flex-wrap">
  {#each schoolList as school}
    <School {school} />
  {/each}
</div>
