<template>
  <div>
    <form @submit="handleSubmit()" class="w-75 mx-auto border rounded shadow p-5">
      <div class="form-group row mt-3">
        <label for="purchasePrice" class="col-sm-4 col-form-label">Purchase Price *</label>
        <div class="col-sm-6">
          <input v-model="purchasePrice" type="number" class="form-control" id="purchasePrice"
            placeholder="E.g. $ 100,000,000" min="0" required />
        </div>
      </div>
      <div class="form-group row mt-3">
        <label for="interestRate" class="col-sm-4 col-form-label">Interest Rate *</label>
        <div class="col-sm-6">
          <input v-model="interestRate" type="number" class="form-control" id="interestRate" placeholder="E.g. 20 %"
            min="0" required />
        </div>
      </div>
      <div class="form-group row mt-3">
        <label for="downPaymentInDollars" class="col-sm-4 col-form-label">Down Payment in $</label>
        <div class="col-sm-6">
          <input v-model="downPaymentInDollars" type="number" class="form-control" id="downPaymentInDollars"
            placeholder="E.g. $ 15,000,000" :disabled="!purchasePrice" min="0" step="0.01" required />
        </div>
      </div>
      <div class="form-group row mt-3">
        <label for="downPaymentInPercentage" class="col-sm-4 col-form-label">Down Payment in %</label>
        <div class="col-sm-6">
          <input v-model="downPaymentInPercent" type="number" class="form-control" id="downPaymentInPercentage"
            placeholder="E.g. 20 %" :disabled="!purchasePrice" min="0" max="100" step="0.01" required />
        </div>
      </div>
      <div class="form-group row mt-3">
        <label for="mortgageTerm" class="col-sm-4 col-form-label">Mortgage Term *</label>
        <div class="col-sm-6">
          <input v-model="mortgageTerm" type="text" class="form-control" id="mortgageTerm"
            :placeholder="isChecked ? 'E.g. 90 months' : 'E.g. 2 years'" required />
        </div>
      </div>

      <div class="form-group row mt-3">
        <div class="col-sm-4"></div>
        <div class="col-sm-6">
          <input class="form-check-input mx-3" type="checkbox" value="" id="flexCheckChecked" v-model="isChecked" />
          <label for="flexCheckChecked">
            mortgage in months
          </label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary w-25 my-3">Submit</button>
    </form>
  </div>
</template>

<script>
import { defineComponent, ref, watch } from "vue"
import { useStore } from 'vuex';
import { request } from "../api/loan";

export default defineComponent({
  name: "FormComponent",
  props: [],
  setup() {
    const store = useStore();
    const purchasePrice = ref();
    const interestRate = ref();
    const downPaymentInDollars = ref();
    const downPaymentInPercent = ref();
    const mortgageTerm = ref();

    const isChecked = ref(true)

    watch([downPaymentInDollars], ([updateDPInDollars]) => {
      if (purchasePrice.value >= 0) {
        downPaymentInPercent.value = ((updateDPInDollars * 100) / purchasePrice.value)
      }
    })

    watch([downPaymentInPercent], ([updateDPInPercent]) => {
      if (purchasePrice.value >= 0) {
        downPaymentInDollars.value = ((purchasePrice.value * updateDPInPercent) / 100)
      }
    })

    watch([purchasePrice], () => {
      if (downPaymentInDollars.value >= 0 && downPaymentInPercent.value >= 0) {
        [downPaymentInPercent.value, downPaymentInDollars.value] = [undefined, undefined]
      }
    })

    const handleSubmit = async () => {
      const payload = {
        principal_amount: purchasePrice.value,
        interest_rate: interestRate.value,
        down_payment_type: "currency",
        down_payment: downPaymentInDollars.value,
        loan_term: Number(mortgageTerm.value),
        loan_term_type: isChecked.value ? "months" : "years"
      };

      const response = await request('POST', '/', payload)
      if (response && response?.id) {
        [purchasePrice.value, interestRate.value, downPaymentInDollars.value, downPaymentInPercent.value, mortgageTerm.value] = [null, null, null, null, null]
        store.state.loans = await request('GET', '/')
      }
    }


    return {
      purchasePrice,
      interestRate,
      downPaymentInDollars,
      downPaymentInPercent,
      mortgageTerm,
      isChecked,
      handleSubmit
    }
  },
})
</script>
