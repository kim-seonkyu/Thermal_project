from django.db import models

# Create your models here.

class TempData(models.Model):
    seq = models.AutoField(db_column='SEQ', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME')  # Field name made lowercase.
    maxtemp = models.FloatField(db_column='MAXTEMP', blank=True, null=True)  # Field name made lowercase.
    mintemp = models.FloatField(db_column='MINTEMP', blank=True, null=True)  # Field name made lowercase.
    avgtemp = models.FloatField(db_column='AVGTEMP', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField(db_column='DAY', blank=True, null=True)  # Field name made lowercase.
    hour = models.TimeField(db_column='HOUR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_Data'