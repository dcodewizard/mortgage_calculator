<template>
  <div class="w-75 mx-auto border rounded shadow p-5">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col"
              v-for="(column, index) in columns"
              :key="index">
            {{ column.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr scope="col"
              v-for="(row, index) in rows"
              :key="index">
              <td v-for="(column, index) in columns" :key="index">
                {{ row[column.field]?.toFixed(column.field == 'id' ? 0 : 2) }}
              </td>
        </tr>

      </tbody>
    </table>
  </div>
</template>

<script>
  import { defineComponent, onMounted, watch, ref } from "vue"
  import { useStore } from 'vuex';
  import { request } from "@/api/loan";
  export default defineComponent({
    name: "HomeView",
    props: ["columns"],
    setup() {
      const store = useStore();
      const rows = ref([]);

      const fetchData = async () => {
        try {
          const response = await request('GET', '/');
          store.state.loans = response;
        } catch (err) {
          console.log(err?.message)
        }
      };

      watch(() => store.state?.loans, () => {
        rows.value = store.state?.loans
      })

      onMounted(() => {
        fetchData();
      });

      return {
        rows
      }
    },
  })
</script>
