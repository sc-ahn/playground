<script lang="ts">
  import { type ISchoolInfo } from "$lib/interfaces";
  export let school: ISchoolInfo;
</script>

<button
  on:click={() => alert(school.school_name)}
  class="border border-gray-300 rounded-lg p-3 m-3 w-48 h-24 flex flex-col justify-center items-center hover:bg-gray-100 transition-colors duration-300 ease-in-out shadow-md"
>
  <div class="text-lg font-bold" id={school.standard_code}>{school.school_name}</div>
  <div class="text-sm">{school.standard_code}</div>
</button>
