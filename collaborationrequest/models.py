from django.db import models

class CollaborationRequest(models.Model):
    PERSON_TYPE_CHOICES = (
        ('P', 'Person'),
        ('C', 'Company'),
    )
    person_type = models.CharField(max_length=10, choices=PERSON_TYPE_CHOICES, default='P')
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} . {self.full_name} - {self.subject}"

