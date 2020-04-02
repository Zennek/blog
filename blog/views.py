from django.shortcuts import render
from django.utils import timezone
from .models import Wpis

# Create your views here.

def glowna(request):
    wpisy = Wpis.objects.filter(data_publikacji__lte=timezone.now()).order_by('data_publikacji')
    return render(request, 'blog/glowna.html', {'wpisy': wpisy})
