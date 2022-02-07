from django.shortcuts import redirect, render, render_to_response
from random import randint
from time import strftime, localtime

# Create your views here.
def index(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold'] = 0
    return render(request, 'index.html')

def process_money(request):
    if 'activities' in request.session:
        pass
    else:
        request.session['activities'] = []
    if request.POST.get('cave'):
        earnings = randint(5, 10)
        request.session['gold'] += earnings
        request.session['activities'].append("Earned " + str(earnings) + " gold from the cave! " + strftime("%m-%d-%Y %H:%M %p", localtime()))
    if request.POST.get('house'):
        earnings = randint(2, 5)
        request.session['gold'] += earnings
        request.session['activities'].append("Earned " + str(earnings) + " gold from the house! " + strftime("%m-%d-%Y %H:%M %p", localtime()))
    if request.POST.get('farm'):
        earnings = randint(10, 20)
        request.session['gold'] += earnings
        request.session['activities'].append("Earned " + str(earnings) + " gold from the farm! " + strftime("%m-%d-%Y %H:%M %p", localtime()))
    if request.POST.get('casino'):
        earnings = randint(0, 50)
        if randint(0, 1) == 0:
            request.session['gold'] += earnings
            request.session['activities'].append("Entered a casino and won " + str(earnings) + " gold! " + strftime("%m-%d-%Y %H:%M %p", localtime()))
        else:
            request.session['gold'] -= earnings
            request.session['activities'].append("Entered a casino and lost " + str(earnings) + " gold! " + strftime("%m-%d-%Y %H:%M %p", localtime()))
    return redirect('/')