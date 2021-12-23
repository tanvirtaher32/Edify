from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
MinValueValidator

# DIVISION_CHOICES = (
#     ('Barishal','Barishal'),
#     ('Chittagong','Chittagong'),
#     ('Dhaka','Dhaka'),
#     ('Khulna','Khulna'),
#     ('Rajshahi','Rajshahi'),
#     ('Rangpur','Rangpur'),
#     ('Mymensingh','Mymensingh'),
#     ('Sylhet','Sylhet'),
    
# )

class Student(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    # division = models.CharField(choices=DIVISION_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('Computer Science & Engineering','Computer Science & Engineering'),
    ('Electrical & Electronic Engineering','Electrical & Electronic Engineering'),
    ('Aerospace Engineering','Aerospace Engineering'),
    ('Biomechanical Engineering','Biomechanical Engineering'),
    ('Chemical Engineering','Chemical Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),
    ('Computer & Communication Engineering','Computer & Communication Engineering'),
    ('Applied Math','Applied Math'),
    ('Applied Physics','Applied Physics')
)
class Course(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=150)
    product_image = models.ImageField(upload_to='courseimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.course.discounted_price


STATUS_CHOICES = (
    ('Successfull','Successfull'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
    choices=STATUS_CHOICES,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.course.discounted_price