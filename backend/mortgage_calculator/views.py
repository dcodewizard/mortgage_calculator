from rest_framework.generics import ListCreateAPIView

from .models import Mortgage
from .serializer import MortgageSerializer


# Create your views here.
class MortgageListCreate(ListCreateAPIView):
    serializer_class = MortgageSerializer
    queryset = Mortgage.objects.all()

    def perform_create(self, serializer):
        data = self.request.data
        if data["down_payment_type"] == "percentage":
            down_payment_amount = (
                serializer.validated_data["down_payment"]
                * serializer.validated_data["principal_amount"]
            ) / 100
        elif data["down_payment_type"] == "currency":
            down_payment_amount = serializer.validated_data["down_payment"]

        if data["loan_term_type"] == "years":
            loan_term_years = data["loan_term"]
            n = loan_term_years * 12
        elif data["loan_term_type"] == "months":
            n = data["loan_term"]
            loan_term_years = n / 12

        print(loan_term_years)

        taxable_amount = (
            serializer.validated_data["principal_amount"] - down_payment_amount
        )
        r = serializer.validated_data["interest_rate"] / 12 / 100
        monthly_payment = (taxable_amount * (pow(1 + r, n) * r)) / (pow(1 + r, n) - 1)
        total_loan_amount = monthly_payment * n
        total_interest_paid = total_loan_amount - taxable_amount
        total_mortgage_amount = total_loan_amount + down_payment_amount

        extra_data = {
            "monthly_payment": monthly_payment,
            "total_loan_amount": total_loan_amount,
            "total_interest_paid": total_interest_paid,
            "total_mortgage_amount": total_mortgage_amount,
        }

        serializer.validated_data["loan_term"] = loan_term_years
        serializer.validated_data.update(extra_data)
        serializer.save()
