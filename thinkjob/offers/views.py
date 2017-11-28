from django.shortcuts import render
from django.http import HttpResponseRedirect

from offers.models import Offer, Enterprise
from offers.forms import OfferForm


#def my_first_view(request,who):
#    return render(request, 'offers/hello.html',{
#	    'who':who,
#	    })

def offer_detail(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    return render(request, 'offers/offer_detail.html',{
        'offer':offer,
    })

def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'offers/offer_list.html',{
        'offers':offers,
    })

def offer_add(request):
    if request.POST:
        form = OfferForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            #return HttpResponseRedirect('URL') NOT GOOD because NOT MAINTENABLE so BETTER TO USE GET ABSOLUTE URL
            return HttpResponseRedirect(new_form.get_absolute_url())
    else:
        form=OfferForm()
    return render(request, 'offers/offer_form.html', {
        'form':form,
    })

def enterprise_detail(request, enterprise_id):
    enterprise = Enterprise.objects.get(id=enterprise_id)
    return render(request, 'offers/enterprise_detail.html',{
        'enterprise':enterprise,
    })