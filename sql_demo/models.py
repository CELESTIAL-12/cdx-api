from django.db import models

class question(models.Model):
    Question = models.CharField(max_length = 500)
    # class Meta:
    #     db_table = 'demo'
