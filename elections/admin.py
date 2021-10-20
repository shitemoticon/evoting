from django.contrib import admin
from .models import Election
from .models import Vote
from .models import Candidate

# Register your models here.
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)