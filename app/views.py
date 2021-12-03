from django.shortcuts import render,redirect
from django.views import View
from .models import Student, Course, Cart, OrderPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')

class CoursesView(View):
    def get(self, request):
        courses = Course.objects.filter(category="Computer Science & Engineering")
        return render(request, 'app/home.html', {'courses': courses})


# def course_detail(request):
#  return render(request, 'app/coursedetail.html')

class CourseDetailView(View):
    def get(self, request,pk):
        course = Course.objects.get(pk=pk)
        return render(request, 'app/coursedetail.html', {'course': course})


def add_to_cart(request):
 user = request.user
 course_id = request.GET.get('course_id')
 course = Course.objects.get(id=course_id)
 Cart(user=user, course=course).save()
 return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        total_amount = 0.0
        cart_course = [c for c in cart if Cart.objects.all() if c.user==user]
        # print(cart_course)
        if cart_course :
            for c in cart_course :
                tempAmmount = (c.quantity* c.course.discounted_price)
                amount+=tempAmmount
                total_amount=amount
            return render(request, 'app/addtocart.html', {'cart': cart, 'total_amount': total_amount, 'amount': amount})
        
        else:
            return render(request, 'app/emptycart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-warning'})
    
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Student(user = usr,name=name, locality=locality, city=city, zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-warning'})



def address(request):
 add = Student.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add': add, 'active': 'btn-warning'})

def orders(request):
 return render(request, 'app/orders.html')



def courses(request, data=None):
    if data == None:
        courseShow = Course.objects.filter(category="Computer Science & Engineering")
    elif data == 'ComputerScience&Engineering' or data == 'Electrical&ElectronicEngineering' or data == 'AerospaceEngineering' or data == 'BiomechanicalEngineering' or data == 'ChemicalEngineering' or data == 'MechanicalEngineering' or data == 'CivilEngineering' or data == 'Computer&CommunicationEngineering' or data == 'AppliedMath' or data == 'AppliedPhysics':
        courseShow = Course.objects.filter(category=data)
    
    elif data == 'below':
        courseShow = Course.objects.filter(discounted_price__lt=4000)
    elif data == 'above':
        courseShow = Course.objects.filter(discounted_price__gt=4000)
    # elif data == 'ComputerScience&Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Electrical & Electronic Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Aerospace Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Biomechanical Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Chemical Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Mechanical Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Civil Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Computer & Communication Engineering':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Applied Math':
    #     courseShow = Course.objects.filter(category=data)
    # elif data == 'Applied Physics':
    #     courseShow = Course.objects.filter(category=data)

    return render(request, 'app/courses.html', {'courseShow': courseShow})
#no need to write view code for login as iam using the default authentication of django
# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! You have successfully registered')
            form.save()
        # form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form': form})



def checkout(request):
 return render(request, 'app/checkout.html')


