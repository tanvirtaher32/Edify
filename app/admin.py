from django.contrib import admin
from .models import(
    Student,
    Course,
    Cart,
    OrderPlaced
)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city',
    'zipcode']

@admin.register(Course)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price',
    'discounted_price','description','instructor','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','course','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','student','course','quantity','order_date','status']