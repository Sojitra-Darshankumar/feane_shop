from django.db import models
from django.forms import ModelForm

# Create your models here.


# ------------------------------------------------------------------------ Admin ------------------

class admin_registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Photo = models.FileField(upload_to='',default='')
    contact = models.BigIntegerField(default='0')

class admin_registration_form(ModelForm):
    class Meta:
        model = admin_registration
        fields = ["username","email","password","Photo","contact"]

# ----------------------------------------------------------------------- Slider ------------------

# class admin_slider(models.Model):
#     title = models.CharField(max_length=100)
#     off = models.BigIntegerField()
#     description = models.TextField(max_length=300)

# class admin_slider_form(ModelForm):
#     class Meta:
#         model = admin_slider
#         fields = ["title","off","description"]

# ----------------------------------------------------------------------- Food Category ---------------

class food_category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title

class food_category_form(ModelForm):
    class Meta:
        model = food_category
        fields = ["title"]

# ----------------------------------------------------------------------- Food -----------------------------

class food(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    food_category = models.ForeignKey(food_category,on_delete=models.CASCADE,default='')
    photo = models.FileField(upload_to='',default='')
    admin_id = models.BigIntegerField()

class food_form(ModelForm):
    class Meta:
        model = food
        fields = ["title","description","price","food_category","photo","admin_id"]


class tablebook(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    contact = models.BigIntegerField()
    person = models.BigIntegerField()
    date = models.DateField()

class tablebook_form(ModelForm):
    class Meta:
        model = tablebook
        fields = ["name","email","contact","person","date"]

class comments(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    comment = models.CharField(max_length=300)
    photo = models.FileField(upload_to='',default='')

class comments_form(ModelForm):
    class Meta:
        model = comments
        fields = ["name","city","comment","photo"]