from django.shortcuts import render, redirect
from users.models import CustomUser
from .models import Table, Item, Order, OrderHistory, Category
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def home(request):
    return render(request, 'index.html')

def links(request, links, id=None):
    if links == 'view_tables':
        return view_tables(request)
    elif links == 'modify_tables':
        return modify_tables(request)
    elif links == 'modify_staff':
        return modify_staff(request)
    elif links == 'view_staff':
        return view_staff(request)
    elif links == 'view_menu':
        return view_menu(request)
    elif links == 'modify_menu':
        return modify_menu(request)
    elif links == 'order' and id:
        return order(request)

def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect('admin-home')
            else:
                user.session = True
                user.save()
                login(request, user)
                return redirect('staff-home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'login.html')

def logout_(request):
    user = request.user
    user.session = False
    user.save()
    logout(request)
    return redirect('login')

def admin_(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        return render(request, 'admin.html')
    else:
        return redirect('login')

def staff_(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'staff.html')
    else:
        return redirect('login')

def register_staff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register-staff')
        else:
            user = CustomUser.objects.create_user(username=username, password=password, is_staff=True)
            messages.success(request, 'Staff Registered Successfully')
    return render(request, 'register-staff.html')

def view_tables(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'view-tables.html')
    else:
        return redirect('login')
    
def back_home(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        return redirect(reverse('admin-home'))
    else:
        return redirect(reverse('staff-home'))
    
def modify_tables(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'modify-tables.html')
    else:
        return redirect('login')

def modify_staff(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        return render(request, 'modify-staff.html')
    else:
        return redirect('login')

def fetch_staff(request):
    staff = CustomUser.objects.filter(is_staff=True)
    data = []
    for i in staff:
        if i.is_superuser:
            continue
        data.append({
            'username': i.username,
            'id': i.id,
            'session': i.session,
        })
    # print(data)
    return JsonResponse({'data': data})

def delete_staff(request):
    if request.method == 'GET':
        id = request.GET.get('id','')
        CustomUser.objects.filter(id=id).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def view_staff(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        return render(request, 'view-staff.html')
    else:
        return redirect('login')
    
def fetch_tables(request):
    tables = Table.objects.all()
    data = []
    for i in tables:
        data.append({
            'table_number': i.table_number,
            'table_name': i.table_name,
            'id': i.id,
        })
    return JsonResponse({'data': data})

def delete_table(request):
    if request.method == 'GET':
        table_number = request.GET.get('table_number','')
        Table.objects.filter(table_number=table_number).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def add_table(request, table_number):
    if request.method == 'GET':
        if Table.objects.filter(table_number=table_number).exists():
            return JsonResponse({'status': 'error'})
        else:
            Table.objects.create(table_number=table_number, table_name='Table'+str(table_number))
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def view_menu(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'view-menu.html')
    else:
        return redirect('login')
    
def fetch_menu(request):
    items = Item.objects.all()
    data = []
    for i in items:
        data.append({
            'name': i.name,
            'price': i.price,
            'category': i.category.category_name,
            'id': i.id,
        })
    data.sort(key=lambda x: x['category'])    
    # print(data)
    return JsonResponse({'data': data})

def fetch_categories(request):
    categories = Category.objects.all()
    data = []
    for i in categories:
        data.append({
            'category_name': i.category_name,
            'id': i.id,
        })
    return JsonResponse({'data': data})

def modify_menu(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'modify-menu.html')
    else:
        return redirect('login')
     
def add_category(request, category):
    if request.method == 'GET':
        if Category.objects.filter(category_name__iexact=category).exists():
            return JsonResponse({'status': 'error'})
        else:
            Category.objects.create(category_name=category)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def add_item(request, item, category, price):
    if request.method == 'GET':
        if Item.objects.filter(name__iexact=item).exists():
            return JsonResponse({'status': 'error'})
        else:
            category = Category.objects.get(category_name=category)
            Item.objects.create(name=item, price=price, category=category)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def delete_category(request, id):
    if request.method == 'GET':
        Category.objects.filter(id=id).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def delete_item(request, id):
    if request.method == 'GET':
        Item.objects.filter(id=id).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def order(request, table_name):
    user = request.user
    table = Table.objects.get(table_name=table_name)
    print(table.table_name)
    if user.is_authenticated and user.is_staff:
        return render(request, 'order.html', {'table': table})
    else:
        return redirect('login')

def fetch_items(request, category_name):
    print(category_name)
    items = Item.objects.filter(category__category_name=category_name)
    data = []
    for i in items:
        data.append({
            'name': i.name,
            'price': i.price,
            'id': i.id,
        })
    return JsonResponse({'data': data})
