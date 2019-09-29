from django.db import models

# Create your models here.

class Personne(models.Model):
    gender = models.CharField(max_length=60, verbose_name="Genre")
    name = models.CharField(max_length=60, verbose_name="Nom")
    amount = models.CharField(max_length=60, verbose_name="Montant")
    deadline = models.DateField(auto_now=False, verbose_name="Délai")
    phone = models.IntegerField(verbose_name="Numéro")

    def __str__(self):
        gender = self.gender
        name = self.name
        amount = self.amount
        deadline = self.deadline
        phone = self.phone

        return "%s, %s, %s, %s, %s" %(gender, name, amount, deadline, phone)