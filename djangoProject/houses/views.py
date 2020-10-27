from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import House,Image
from django.contrib.auth.models import User
from .forms import HouseCreationForm
# Create your views here.

@login_required
def house_view(request):
    data = House.objects.filter(user = request.user)
    context = {
        'house': data
    }
    return render(request,'houses/view_houses.html',context)

@login_required
def add_house_view(request):
    if request.method == 'POST':
        form = HouseCreationForm(request.POST,request.FILES)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.user = User.objects.get(username = request.user)
            newForm.save()
            for file in request.FILES.getlist('house_pics'):
                instance = Image(house = House.objects.get(pk = newForm.pk),image=file)
                instance.save()

            messages.success(request, f'Your house has been successfully added')
            return redirect('home-view')
    else:
        form = HouseCreationForm()

    return render(request,'houses/add_house.html',{'form':form})

@login_required
def house_info(request, single_slug):
    houses = [h.id for h in House.objects.all()]
    if int(single_slug) in houses:
        this_house = House.objects.get(id=int(single_slug))
        image_src = Image.objects.filter(house__id = single_slug)
        h_form = HouseCreationForm(instance=request.user)
        return render(request, "houses/house_page.html", {'house':this_house, 
                                                          'image_src':image_src, 
                                                          'h_form':h_form})
    else:
        return HttpResponse(f"404 error")