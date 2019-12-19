from django.shortcuts import render, redirect
from datetime import datetime
from random import randint

# Create your views here.
def index(request):
    if "user_gold" not in request.session:
        request.session['user_gold'] = 0
        request.session['activities'] = []
    print(f"user gold = {request.session['user_gold']}")
    return render(request, "ninja_gold_app/index.html")

def process_money(request):
    gold = 0
    building = ""
    print('**** start process_money ****')
    if request.POST['building'] == 'farm':
        gold = randint(10,20)
        request.session['user_gold'] += gold
        building = 'farm'
        print(f"farm: {request.session['user_gold']}")
    if request.POST['building'] == 'cave':
        gold = randint(5,10)
        request.session['user_gold'] += gold
        building = 'cave'
        print(f"cave: {request.session['user_gold']}")
    if request.POST['building'] == 'house':
        gold = randint(2,5)
        request.session['user_gold'] += gold
        building = 'house'
        print(f"house: {request.session['user_gold']}")
    if request.POST['building'] == 'casino':
        gold = randint(-50,50)
        request.session['user_gold'] += gold
        building = 'casino'
        print(f"casino: {request.session['user_gold']}")
    print('**** end process_money ****')

    if gold < 0:
        result = f"<p class='text-danger'>Entered the casino and lost {gold} gold! {datetime.now()}</p>"
    else:
        result = f"<p class='text-success'>Earned {gold} from {building}, {datetime.now()}</p>"

    request.session['activities'].append({'result': result})
    print(request.session['activities'])

    return redirect('/')

def reset(request):
    request.session.clear()
    print('**** game reset by user ****')
    return redirect('/')