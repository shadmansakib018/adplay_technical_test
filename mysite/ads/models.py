from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class AdtrackTest(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    platformtype = models.CharField(max_length=7)
    devicemodel = models.CharField(max_length=25)
    imagename = models.CharField(max_length=35)
    imageurl = models.CharField(max_length=73)
    userid = models.IntegerField()
    companyid = models.CharField(max_length=2, blank=True, null=True)
    brandname = models.CharField(max_length=78)
    name = models.CharField(max_length=24)
    is_youtube = models.CharField(max_length=1)
    gdrivelink = models.CharField(max_length=33)
    destinationlink = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=10)
    category_name = models.CharField(max_length=23)
    advertisername = models.CharField(max_length=69, blank=True, null=True)

    class Meta:
        db_table = 'adtrack_test'

