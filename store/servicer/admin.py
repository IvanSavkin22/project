from django.contrib import admin
from .models import Part, Appointment, PersonalizationRequest

admin.site.register(Part)
admin.site.register(Appointment)
admin.site.register(PersonalizationRequest)
