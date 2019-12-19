from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    product = Product.objects.get(id=request.POST["product_id"])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect("/receipt")

def receipt(request):
    last_order = Order.objects.last()
    total_charge = last_order.total_price
    total_quantity = Order.objects.aggregate(Sum('quantity_ordered'))
    total_charged = Order.objects.aggregate(Sum('total_price'))
    totals = {
        "charged": total_charge,
        "total_charged": total_charged.get("total_price__sum"),
        "total_quantity": total_quantity.get("quantity_ordered__sum")
    }
    return render(request, "store/checkout.html", totals)