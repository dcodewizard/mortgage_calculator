<template>
  <div class="mt-5 my-5">
    <h3>Loan Payment Calculator</h3>
  </div>
  <div class="mt-5 my-5">
    <form-component />
  </div>
  <div class="mt-5 my-5">
    <loan-table :columns="loanTableColumn" />
  </div>
</template>

<script>
import { defineComponent } from "vue"
import LoanTable from '@/components/LoanTable.vue';
import FormComponent from "@/components/Form.vue";

const loanTableColumn = [
  { field: 'id', label: 'ID' },
  { field: 'principal_amount', label: 'Principal Amount $' },
  { field: 'interest_rate', label: 'Interest Rate %' },
  { field: 'down_payment', label: 'Down Payment $' },
  { field: 'loan_term', label: 'Mortgage Term (years)' },
  { field: 'monthly_payment', label: 'Monthly Payment $' },
  { field: 'total_loan_amount', label: 'Total Loan Amount $' },
  { field: 'total_mortgage_amount', label: 'Total Mortgage Amount $' },
  { field: 'total_interest_paid', label: 'Total Interest Paid %' }
];

export default defineComponent({
  name: "HomeView",
  components: {
    LoanTable,
    FormComponent
  },
  setup() {
    return {
      loanTableColumn
    }
  },
})
</script>
