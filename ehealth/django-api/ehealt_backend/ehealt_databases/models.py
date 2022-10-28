# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Person(models.Model):
    person_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    second_lastname = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'person'


class Patient(models.Model):
    patient_id = models.PositiveIntegerField(primary_key=True)
    person = models.ForeignKey('Person', on_delete = models.CASCADE)

    class Meta:
        #managed = False
        db_table = 'patient'


class Doctor(models.Model):
    doctor_id = models.PositiveIntegerField(primary_key=True)
    person = models.ForeignKey('Person', on_delete = models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'doctor'


class DoctorAcount(models.Model):
    doctor_account_id = models.PositiveIntegerField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    doctor_username = models.CharField(max_length=100, blank=True, null=True)
    doctor_email = models.CharField(max_length=100, blank=True, null=True)
    doctor_password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'doctor_acount'


class PatientDiagnostic(models.Model):
    diagnostic_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    diagnostic_text = models.TextField()

    class Meta:
        #managed = False
        db_table = 'patient_diagnostic'
        unique_together = (('diagnostic_id', 'doctor'),)


class PhoneNumbers(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=10)
    phone_content= models.CharField(max_length=10, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)

    class Meta:
        #managed = False
        db_table = 'phone_numbers'


class UserAccount(models.Model):
    user_account_id = models.PositiveIntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'user_account'


class VitalSigns(models.Model):
    register_number = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    oxigen = models.FloatField(blank=True, null=True)
    heart_rate = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    resp_rate = models.FloatField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    day_taken = models.PositiveIntegerField(blank=True, null=True)
    year_taken = models.PositiveIntegerField(blank=True, null=True)
    month_taken = models.PositiveIntegerField(blank=True, null=True)
    hour_taken = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'vital_signs'
        

