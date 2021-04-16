
from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request):
        product = None
        categories = Category.get_all_category()

        category_id = request.GET.get('category')

        if category_id:
            product = Product.get_all_product_by_categoryId(category_id)
        else:
            product = Product.get_all_product()
        return render(request, 'store/home.html', {'products':product, 'categoris':categories})

    def post(self,request):
        product_id = request.POST.get('productid')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantitiy = cart.get(product_id)
            if quantitiy:
                if remove:
                    if quantitiy<=1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantitiy - 1
                else:
                    cart[product_id] = quantitiy + 1
            else:
                cart[product_id] = 1
            
        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart

        #print(request.session['cart'])
        return redirect('home')


    