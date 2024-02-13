from django.contrib import admin
from myapp.models import DatabaseModel,Trade

admin.site.register(Trade)
admin.site.register(DatabaseModel)