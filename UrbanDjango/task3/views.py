from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'third_task/main.html')

def shop(request):
    items = {
        'Haak': '780 руб.',
        'Hollow survivors: prologue': 'Бесплатно',
        'Supraland': '380 руб.',}

    if request.method == 'POST':
        selected_item = request.POST.get('item')
        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'].append(selected_item)
        request.session.modified = True
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    cart_items = request.session.get('cart', [])
    return render(request, 'third_task/cart.html', {'cart_items': cart_items})
