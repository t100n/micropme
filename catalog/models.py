import uuid  # Required for unique book instances
from datetime import date

from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a borrower

class Document(models.Model):
    """Model representing a document"""
    #internal_number = models.AutoField(primary_key=False)

    document_date = models.DateField(null=True, blank=True)

    country = models.TextField(max_length=1000, help_text="Country")

    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['document_date']
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('document-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.document_date, self.country)
