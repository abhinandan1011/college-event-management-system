from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech Fest'),
        ('cultural', 'Cultural Fest'),
        ('sports', 'Sports Meet'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
