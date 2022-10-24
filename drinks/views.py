from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Drink
from .serializers import DrinkSerializer
# endpoints will:
  # get all drinks
  # serialize them
  # return json
@api_view(['GET', 'POST'])
def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks': serializer.data})
    