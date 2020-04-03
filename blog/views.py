from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Wpis

# Create your views here.

def glowna(request):
    wpisy = Wpis.objects.filter(data_publikacji__lte=timezone.now()).order_by('data_publikacji')
    return render(request, 'blog/glowna.html', {'wpisy': wpisy})

def wpis_wpis(request, pk):
    wpis = get_object_or_404(Wpis, pk=pk)
    return render(request, 'blog/wpis_wpis.html', {'wpis': wpis})
