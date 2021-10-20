from django.contrib import admin
from .models import Election,Vote,Candidate

# Register your models here.
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)