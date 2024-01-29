from django.db import models

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Student(BaseModel):
    title=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=9)
    university=models.ForeignKey("University", on_delete=models.CASCADE, blank=True, null=True)
    type=(("Bakalavr","Bakalavr"),("Magistratura","Magistratura"))
    type_of_student=models.CharField(max_length=12, choices=type, default='Bakalavr')
    price_of_contract=models.IntegerField()

    class Meta:
        verbose_name='Student'
        verbose_name_plural='Students'

    def __str__(self) -> str:
        return self.title


class Investor(BaseModel):
    title=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=9)
    money=models.IntegerField()
    choice=(("Yangi","Yangi"), ("Moderatsiyada","Moderatsiyada"), ("Tasdiqlangan","Tasdiqlangan"), ("Bekor qilingan","Bekor qilingan"))
    action=models.CharField(max_length=30, choices=choice, default='Moderatsiyada')

    class Meta:
        verbose_name='Investor'
        verbose_name_plural='Investors'

    def __str__(self) -> str:
        return self.title
    
class University(BaseModel):
    title=models.CharField(max_length=250)

    class Meta:
        verbose_name='University'
        verbose_name_plural='Universities'

    def __str__(self):
        return self.title

class Operation(BaseModel):
    choosen_student=models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    # content_object=GenericForeignKey(choosen_student, 'title')
    choosen_investor=models.ForeignKey(Investor, on_delete=models.CASCADE, blank=True, null=True)
    sending_money=models.IntegerField()

    class Meta:
        verbose_name='Operation'
        verbose_name_plural='Operations'

    def __str__(self) -> str:
        return f"{self.choosen_student}"



