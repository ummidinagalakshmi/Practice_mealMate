from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Customer, Restaurant, Item

# Create your views here.
def index(request):
    return render(request, 'index.html')
def open_signIn(request):
    return render(request, 'signin.html')
def open_signUp(request):
    return render(request, 'signup.html')
def open_add_restaurant(request):
    return render(request, "add_restaurant.html")

def open_show_restaurant(request):
    restaurants = Restaurant.objects.all()   # fetch data
    return render(request, "display_restaurants.html", {'restaurants': restaurants})


def signUp(request):
    #return HttpResponse("Received")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        try: 
            Customer.objects.get(username=username)
            return HttpResponse("Duplicate usernames are not allowed")
        except:
            Customer.objects.create(username = username,
                                password = password,
                                email = email,
                                phone = phone,
                                address = address)
            return render(request, "signin.html")

        
    
def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    try:
        Customer.objects.get(username = username, password=password)
        if username == 'admin':
            return render(request, "admin_home.html")
        else:
            restaurants = Restaurant.objects.all()   # fetch data
            return render(request, "customer_home.html", {
                    'restaurants': restaurants,
                    'username': username
                })
            #return render(request, "customer_home.html", {'restaurants': restaurants})
            


    except Customer.DoesNotExist:
        return render(request, "fail.html")
    
def add_restaurant(request):
    # return HttpResponse("Working")
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        Restaurant.objects.create(
            name=name,
            picture=picture,
            cuisine=cuisine,
            rating=rating
        )

        #restaurants = Restaurant.objects.all()
        #return render(request, 'show_restaurants.html', {'restaurants': restaurants})
        return HttpResponse("Added succesfully")

    return HttpResponse("Invalid request")



def open_update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'update_restuarant.html', {"restaurant": restaurant})

def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()

        restaurants = Restaurant.objects.all()
        return render(request, 'show_restaurants.html', {"restaurants": restaurants})

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()

    restaurants = Restaurant.objects.all()
    return render(request, 'show_restaurants.html', {"restaurants": restaurants})

def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get( id=restaurant_id)
    # itemList = Item.objects.all()
    itemList = restaurant.items.all()
    return render(request, 'update_menu.html', 
{"itemList": itemList, "restaurant": restaurant})


def update_menu(request,restaurant_id ):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_veg = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')

        
        Item.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            is_veg=is_veg,
            picture=picture
        )
        return render(request, 'admin_home.html')

# view Menu
def view_menu(request, restaurant_id, username):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    itemList = restaurant.items.all()
    return render(request, 'customer_menu.html', {
        'restaurant': restaurant,
        'itemList': itemList,
        'username':username
    })