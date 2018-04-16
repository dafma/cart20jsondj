
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
import json
from .models import  Book,  BookOrder,  Order
from django.db.models import Q
from itertools import chain

from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def category1(request, category):


    products = Book.objects.all()

    featured_products = products.filter(featured=True)\
                            .order_by('-pub_date')[:8]


    page_class = 'showcase ' + category
    page_title = category

    product_sections = [featured_products, products]
    return render(request, 'showcase.html', locals())



def saveOrderProducts(order_content, order):

    amount = 0
    prod_error = False

    for product in order_content:
        product_uid = product['id'].split("-")
        category = product_uid[0]
        p_id = product_uid[1]
        quantity = product['quantity']
        p_price = product['price'].split(' ')[0]
        p_price = p_price.replace(',','.')
        amount += float(p_price) * float(quantity)

        if category == 'books':
            book_obj = Book.objects.get(pk=p_id)
            book_obj.popularity += quantity
            book_obj.save()
            prod_order = order.bookorder_set.create(product=book_obj,
                                                    quantity=quantity)
        else:
            prod_error = True
            print("product error")
        if not prod_error:
            prod_order.save()
    return amount



@login_required(login_url='/sign')
def checkOut(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            user = request.user
            order_content = json.loads(request.POST['cartJSONdata'])
            order = form.save(commit=False)
            order.user = user
            order.total_amount = 0
            order.save()   #We have to save the order before calculate ammount
            order.total_amount = saveOrderProducts(order_content, order)
            order.save()


            books = BookOrder.objects.filter(order=order)


            products = list(chain( books,))
            page_class = 'checkout-page'
            page_title = "Order done!"

            return render(request, 'success.html', locals())
    else:
        form = OrderForm()

    page_class = 'checkout-page'
    page_title = "Check out"
    return render(request, 'order.html', locals())


def home(request):
    books = {'name': 'books'}
    books['products']  = Book.objects.order_by('-pub_date')[:3]



    page_title = 'home'
    page_class = 'showcase home'

    product_sections = [books,]
    return render(request, 'showcase.html', locals())

def product(request, category, p_id):

    if category == "books":
        products = Book.objects.all()

    product = products.get(pk=p_id)
    product.popularity += 1
    product.save()

    products = products.exclude(pk=p_id)

    for p in products:
        if p.popularity > 0:
            p.popularity -= 1
            p.save()

    products = products.order_by('popularity')[:4]

    related = {'title': "Related products", "products": products}

    page_title = product.name
    page_class = 'single-product-page'

    return render(request, 'product.html', locals())


def search(request):

    search = {'error': True, 'hasQuery': False}
    books = {'name': 'books', 'products': ''}

    query = request.GET.get('q', '')
    if query:
        search['hasQuery'] = True
        qset1 = (
            Q(name__icontains=query) |
            Q(description__icontains=query)
            )
        books['products'] = Book.objects.filter(qset1).distinct()\
                            .order_by('popularity')

    if 	not books['products']:
        books['products'] = Book.objects.order_by('popularity')[:3]
        search['hasOtherProducts'] = True

    else:
        search['error'] = False

    product_sections = [books,]
    page_title = query

    page_class = 'showcase search'

    return render(request, 'showcase.html', locals())