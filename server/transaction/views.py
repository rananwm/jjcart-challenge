from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)


@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)

class TransactionListView(APIView):
    def get(self, request, format=None):
        transactions = [
            {"transaction_id": "txn_12345", "amount": 100.00, "timestamp": "2024-01-01T12:00:00Z"}
        ]
        return Response(transactions)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
