from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    transaction_id = serializers.CharField(max_length=200)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    timestamp = serializers.DateTimeField()
