from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Drink
from .serializers import DrinkSerializer
# endpoints will:
  # get all drinks
  # serialize them
  # return json

# api_view decorator is used to define the request methods a function can receive
# api_view is part of the django-restframework package
@api_view(['GET', 'POST']) # Function can only accept GET and POST
def drink_list(request):  
    if request.method == "GET":
      return drink_list_GET()
    elif request.method == "POST":
      return drink_list_POST()
      
def drink_list_GET():
  drinks = Drink.objects.all() # Gets all the Drink objects that have been created
  serializer = DrinkSerializer(drinks, many=True) # Serializes drink data into correct JSON format
  return JsonResponse({'drinks': serializer.data}) # Return the reponse as a JSON object

def drink_list_POST():
  print("This is a POST request and it's action is not yet defined.\n\n")
  return JsonResponse({'drinks': []})
  
    