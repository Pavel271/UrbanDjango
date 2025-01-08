from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'fourth_task/main.html')

def shop(request):
    games = ['Haak', 'Hollow survivors: prologue', 'Supraland']
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    cart_items = request.session.get('cart', [])
    return render(request, 'fourth_task/cart.html', {'cart_items': cart_items})
