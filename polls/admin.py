from django.contrib import admin
from .models import Choice, Question ,Questions ,Choices
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questions)
admin.site.register(Choices)