import json
from django.http import JsonResponse
from app.models import Cart, Product

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    print(data)
    
    # Kiểm tra xem sản phẩm có tồn tại không
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        return JsonResponse('Product not found', safe=False)

    count = data.get('count', 1)

    print(action)
    print(count)

    order = Cart.objects.filter(user=request.user, product=product).first()

    if action == 'addProduct':
        if order:
            order.quantity += count
        else:
            order = Cart(user=request.user, product=product, quantity=count)
    elif action == 'add':
        order.quantity += count
    elif action == 'remove':
        order.quantity -= count

    if order and (int(order.quantity) <= 0 or action == 'delete'):
        order.delete()
    elif order:
        order.save()

    return JsonResponse('added', safe=False)


