from rest_framework import serializers
from .models import Bank, Branches
from django.contrib.auth.models import User


class BankSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Bank
        fields = ('bank_id', 'name')

class BranchesSerializer(serializers.ModelSerializer):  # create class to serializer model
    bank_name = serializers.RelatedField(source='bank', read_only='True', )
    class Meta:
        model = Branches
        fields = '__all__'