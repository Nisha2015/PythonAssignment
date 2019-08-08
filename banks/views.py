from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Bank, Branches
from .serializers import BankSerializer, BranchesSerializer
from .pagination import CustomPagination
from django.http import HttpResponse

class get_delete_update_bank(RetrieveUpdateDestroyAPIView):
    serializer_class = BankSerializer

    def get_queryset(self, pk):
        try:
            bank = Bank.objects.get(pk=pk)
        except bank.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return bank

    # Get a bank
    def get(self, request, pk):

        bank = self.get_queryset(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a bank
    def put(self, request, pk):
        
        bank = self.get_queryset(pk)
        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a bank
    def delete(self, request, pk):

        bank = self.get_queryset(pk)

        bank.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

class get_post_bank(ListCreateAPIView):
    serializer_class = BankSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       banks = Bank.objects.all()
       return banks

    # Get all banks
    def get(self, request):
        banks = self.get_queryset()
        paginate_queryset = self.paginate_queryset(banks)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new bank
    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_delete_update_branches(RetrieveUpdateDestroyAPIView):
    serializer_class = BranchesSerializer

    def get_queryset(self, pk):
        try:
            branch = Branches.objects.get(pk=pk)
        except Branches.DoesNotExist:
            return HttpResponse(status=404)
        return branch

    # Get a branch
    def get(self, request, pk):
        branch = self.get_queryset(pk)
        serializer = BranchesSerializer(branch)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_post_branches(ListCreateAPIView):
    serializer_class = BranchesSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       branches = Branches.objects.all()
       return branches

    # Get all banks
    def get(self, request):
        branches = self.get_queryset()
        paginate_queryset = self.paginate_queryset(branches)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

class get_branches_with_bank_name(RetrieveUpdateDestroyAPIView):
    serializer_class = BranchesSerializer
    pagination_class = CustomPagination

    def get_queryset(self, name, city):
        try:
            bank = Bank.objects.get(name=name)
            branches = Branches.objects.filter(bank_id=bank, city=city)
        except Branches.DoesNotExist:
            return HttpResponse(status=404)
        return branches

    # Get a branch
    def get(self, request, name, city):
        name = self.kwargs['name']
        city = self.kwargs['city']
        branches = self.get_queryset(name, city)
        paginate_queryset = self.paginate_queryset(branches)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
