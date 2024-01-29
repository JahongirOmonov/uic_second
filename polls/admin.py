from django.contrib import admin
# from .models import *
# from django.apps import apps

# models = apps.get_models()

# # # Register your models here.

# for i in models:
#     try:
#         admin.site.register(i)
#     except:
#         pass


from .models import Student, University, Operation, Investor
admin.site.register(Student)
admin.site.register(Investor)
admin.site.register(University)
admin.site.register(Operation)