from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField(help_text="in minutes")
    cooking_time = models.PositiveIntegerField(help_text="in minutes")
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def total_time(self):
        return self.preparation_time + self.cooking_time

    def __str__(self):
        return self.title