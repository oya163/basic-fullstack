"""Models module for CompanyName"""

from django.db import models


class CompanyName(models.Model):
    """
        Company Name model
    """
    name = models.CharField(max_length=255, default='Happy Fun Corp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
            Meta class for Company Name model
        """
        managed = True
        db_table = 'companyname'

    def __str__(self):
        return f"{self.name}"
