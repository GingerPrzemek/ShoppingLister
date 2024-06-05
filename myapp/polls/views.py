from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from .models import Item
def index(request):
    latest_item_list = Item.objects.order_by("id")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_item_list": latest_item_list,}
    return render(request, "polls/index.html", context)

def info(request, item_id):
    return HttpResponse("You are looking at the item number %s" % item_id)
