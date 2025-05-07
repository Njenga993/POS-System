from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=50)  # e.g., Sales, Inventory
    generated_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()  # Store report data as JSON or plain text

    def __str__(self):
        return f"{self.title} - {self.generated_at}"
    
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Employees(models.Model):
     code = models.CharField(max_length=100,blank=True) 
     firstname = models.TextField() 
     middlename = models.TextField(blank=True,null= True) 
     lastname = models.TextField() 
     gender = models.TextField(blank=True,null= True) 
     dob = models.DateField(blank=True,null= True) 
     contact = models.TextField() 
     address = models.TextField() 
     email = models.TextField() 
     department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
     position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
     date_hired = models.DateField() 
     salary = models.FloatField(default=0) 
     status = models.IntegerField() 
     date_added = models.DateTimeField(default=timezone.now) 
     date_updated = models.DateTimeField(auto_now=True) 

     def __str__(self):
         return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name

class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)


    
class Inventory(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def add_stock(self, quantity):
        """Increase stock quantity."""
        self.stock += quantity
        self.save()

    def reduce_stock(self, quantity):
        """Reduce stock quantity only if enough stock is available."""
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        return False  # Not enough stock

    def __str__(self):
        return f"{self.product.name} - Stock: {self.stock}"