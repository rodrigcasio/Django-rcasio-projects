from django.shortcuts import render
from datetime import date, timedelta
from django.db.models import Count
from .models import *

# 1 
def index(request):
    customers = Customer.objects.all()
    context = {"customer": customers}
    return render(request, "index.html", context=context)

# 2 
def create_customer(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        customer = Customer.objects.create(name=name, email=email, phone=phone, address=address)
        customer.save()
        msg = "Successfully Saved a Customer"
        return render(request, "add.html", context={"msg": msg})
    
    return render(request, "add.html")

# 3
def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)
    interactions = Interaction.objects.filter(interactions_date__gte=thirty_days_ago)

    count = len(interactions)
    interactions = interactions.values("channel", "direction").annotate(count=Count('channel'))

    context = {
        "interactions": interactions,
        "count": count
    }

    return render(request, "summary.html", context=context)

# 4
def interact(request, cid):
    channel = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES
    context = {"channel":channels, "directions":directions}

    if request.method = "POST":
        customer = Customer.objects.get(id=cid)
        channel = request.POST["channel"]
        direction = request.POST["directions"]
        summary = request.POST["summary"]
        interaction = Interaction.objects.create(
                                customer=customer,
                                channel=channel,
                                direction=direction,
                                summary=summary)
        interaction.save()
        context["msg"] = "Interaction Succcess"
        return render(request, "interact.html", context=context)
    
    return render(request, "interact.html", context=context)


