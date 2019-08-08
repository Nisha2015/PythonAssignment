from django.db import models

class Bank(models.Model):
    bank_id = models.BigIntegerField(unique=True, null=False, blank=False, db_index=True)
    name = models.CharField(max_length=49, null=False, blank=False)

class Branches(models.Model):
    ifsc_code = models.CharField(primary_key=True, max_length=11, null=False, blank=False, db_index=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.PROTECT)
    branch = models.CharField(max_length=74, null=False, blank=False)
    address = models.CharField(max_length=195, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26, null=False, blank=False)



