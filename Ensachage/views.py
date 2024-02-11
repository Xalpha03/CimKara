from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.db.models import Sum, Avg, Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

today = date.today()
this_day = today.day
this_month = today.month
this_year = today.year
last_date = this_year-1
jour = datetime.now()

this_yesterday = today - timedelta(days=1)

print("=="*5, "Mois: ", this_month, "=="*5)
print("=="*5, "Année: ", this_year, "=="*5)
print("=="*5, "jour: ", this_day, "=="*5)
print("=="*5, "hier: ", this_yesterday, "=="*5)
print("=="*5, "today: ", today, "=="*5)
print("=="*5, "jour: ", jour, "=="*5)

def index_views(request):
    
    post = Ensachage.objects.filter(Q(created=today))
    
    liv_total = Ensachage.objects.filter(Q(created=today)).aggregate(liv=Sum('livraison'))
    cas_total = Ensachage.objects.filter(Q(created=today)).aggregate(cas=Sum('casse'))
    ens_total = Ensachage.objects.filter(Q(created=today)).aggregate(ens=Sum('ensache'))
    tx_cas_total = Ensachage.objects.filter(Q(created=today)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
    vra_total = Ensachage.objects.filter(Q(created=today)).aggregate(vra=Sum('vrac'))
    context={
        
        'posts': post,
        'liv_total':liv_total,
        'cas_total':cas_total,
        'ens_total':ens_total,
        'tx_cas_total':tx_cas_total,
        'vra_total':vra_total,
    }
    return render(request, 'index.html', context)

def detail_views(request):
    
    if request.method == 'GET':
        get_user = request.GET.get('username', None)
        user = get_object_or_404(User, username=get_user)
        month = request.GET.get('month', None)
        year = request.GET.get('year', None)
        
        
        print(user.id, month, year)
        
        if user.id:
        
            posts=Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).order_by('-created')
            
            liv_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).aggregate(liv=Sum('livraison'))
            cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).aggregate(cas=Sum('casse'))
            ens_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).aggregate(ens=Sum('ensache'))
            tx_cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
            vra_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=this_month) & Q(created__year=this_year)).aggregate(vra=Sum('vrac'))
        
        if user.id and month and year:
            
            posts=Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).order_by('-created')
            
            liv_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).aggregate(liv=Sum('livraison'))
            cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).aggregate(cas=Sum('casse'))
            ens_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).aggregate(ens=Sum('ensache'))
            tx_cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
            vra_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__month=month) & Q(created__year=year)).aggregate(vra=Sum('vrac'))
            
        
        context={
            'month': month,
            'year': year,
            'posts': posts,
            'liv_total':liv_total,
            'cas_total':cas_total,
            'ens_total':ens_total,
            'tx_cas_total':tx_cas_total,
            'vra_total':vra_total,
        }
        
        
    return render(request, 'Production/detail.html', context)

# def edit_views(request):
    get_id = request.GET.get('id_post')
    obj = Ensachage.objects.get(id=get_id)
    form = EnsachageFormEdit(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('data:index_name')
            
    return render(request, 'Production/edit.html', {'form': form})


def update_form_views(request):
    
    update=False
    get_id_ = request.GET.get('id_post')
    obj = Ensachage.objects.get(id=get_id_)
    print(get_id_)
    
    if request.method=="POST":
        username = request.POST.get('username', None)
        get_name = User.objects.get(username=username)
        get_id = get_name.id
        livraison = int(request.POST.get('livraison', None))
        casse = int(request.POST.get('casse', None))
        vrac = float((request.POST.get('vrac', None)).replace(',','.'))
        date = request.POST.get('date', None).replace('/', '-')
        ensache = livraison*20
        
        if ensache != 0 and casse != 0:
            tx_casse = (casse * 100)/(ensache + casse)
        else:
            tx_casse = 0
        
        article = Ensachage.objects.filter(id=get_id_)
        article= article.update(
            username=get_id,
            livraison=livraison,
            casse=casse,
            ensache=ensache,
            tx_casse=tx_casse,                
            vrac=vrac,
            created=date,
        )
        
        if article:
            update=True
            return render(request, 'Production/validate.html', {'update': update})
    return render(request, 'Production/update_form.html', {'obj': obj})

def filter_views(request):

    if request.method == 'GET':
        get_user = request.GET.get('username', None)
        user = get_object_or_404(User, username=get_user)
        year = request.GET.get('year', None)
        
        
        print(user.id, year)
        
        if user.id:
            posts=Ensachage.objects.filter(Q(username=user.id)).order_by('-created')
            
            liv_total = Ensachage.objects.filter(Q(username=user.id)).aggregate(liv=Sum('livraison'))
            cas_total = Ensachage.objects.filter(Q(username=user.id)).aggregate(cas=Sum('casse'))
            ens_total = Ensachage.objects.filter(Q(username=user.id)).aggregate(ens=Sum('ensache'))
            tx_cas_total = Ensachage.objects.filter(Q(username=user.id)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
            vra_total = Ensachage.objects.filter(Q(username=user.id)).aggregate(vra=Sum('vrac'))
            
            if user.id and year:
                posts=Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).order_by('-created')
                
                liv_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).aggregate(liv=Sum('livraison'))
                cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).aggregate(cas=Sum('casse'))
                ens_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).aggregate(ens=Sum('ensache'))
                tx_cas_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
                vra_total = Ensachage.objects.filter(Q(username=user.id) & Q(created__year=year)).aggregate(vra=Sum('vrac'))
        
        context={
            'year': year,
            'posts': posts,
            'liv_total':liv_total,
            'cas_total':cas_total,
            'ens_total':ens_total,
            'tx_cas_total':tx_cas_total,
            'vra_total':vra_total,
        }
            
        
    return render(request, 'Production/filter.html', context)


def add_form_views(request):
    
    add=False
    if request.method == 'POST':
        username = request.POST.get('username', None)
        get_name = User.objects.get(username=username)
        get_id = get_name.id
       
        livraison = int(request.POST.get('livraison', None))
        casse = int(request.POST.get('casse', None))
        vrac = float(request.POST.get('vrac', None).replace(',','.'))
        date = request.POST.get('date', None).replace('/', '-')
        
        print(get_id, livraison, casse, vrac, date)
        
        # if livraison is None or casse is None or vrac is None:
        article=Ensachage.objects.create(
            username=get_name,
            livraison=livraison,
            casse=casse,
            vrac=vrac,
            created=date,
        )
        
        if article:
            add=True
            article.save()
            return redirect('data:index_name')
                
    return render(request, 'Production/add_form.html', { })

def yesterday_views(request):
    
    # yes = Ensachage.objects.get(created=this_yesterday)
    # yes = yes.livraison
    # print("=="*5,yes, "=="*5)
    # post = Ensachage.objects.filter(Q(created__day=this_yesterday) & Q(created__month=this_month) & Q(created__year=this_year))
    liv_total = Ensachage.objects.filter(Q(created=this_yesterday)).aggregate(liv=Sum('livraison'))
    cas_total = Ensachage.objects.filter(Q(created=this_yesterday)).aggregate(cas=Sum('casse'))
    ens_total = Ensachage.objects.filter(Q(created=this_yesterday)).aggregate(ens=Sum('ensache'))
    tx_cas_total = Ensachage.objects.filter(Q(created=this_yesterday)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
    vra_total = Ensachage.objects.filter(Q(created=this_yesterday)).aggregate(vra=Sum('vrac'))
    context={
        'liv_total':liv_total,
        'cas_total':cas_total,
        'ens_total':ens_total,
        'tx_cas_total':tx_cas_total,
        'vra_total':vra_total,
    }
    return render(request, 'Production/yesterday.html', context)

def day_views(request):
    
    liv_total = Ensachage.objects.filter(Q(created=today)).aggregate(liv=Sum('livraison'))
    cas_total = Ensachage.objects.filter(Q(created=today)).aggregate(cas=Sum('casse'))
    ens_total = Ensachage.objects.filter(Q(created=today)).aggregate(ens=Sum('ensache'))
    tx_cas_total = Ensachage.objects.filter(Q(created=today)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
    vra_total = Ensachage.objects.filter(Q(created=today)).aggregate(vra=Sum('vrac'))
    context={
        'liv_total':liv_total,
        'cas_total':cas_total,
        'ens_total':ens_total,
        'tx_cas_total':tx_cas_total,
        'vra_total':vra_total,
    }
    
    return render(request, 'Production/day.html', context)

def month_views(request):
    print(this_month)
    liv_total = Ensachage.objects.filter(Q(created__month=this_month) & Q(created__year=this_year)).aggregate(liv=Sum('livraison'))
    cas_total = Ensachage.objects.filter(Q(created__month=this_month) & Q(created__year=this_year)).aggregate(cas=Sum('casse'))
    ens_total = Ensachage.objects.filter(Q(created__month=this_month) & Q(created__year=this_year)).aggregate(ens=Sum('ensache'))
    tx_cas_total = Ensachage.objects.filter(Q(created__month=this_month) & Q(created__year=this_year)).aggregate(tx_cas=Avg('tx_casse'))                                                                                                                                    
    vra_total = Ensachage.objects.filter(Q(created__month=this_month) & Q(created__year=this_year)).aggregate(vra=Sum('vrac'))
    context={
        'liv_total':liv_total,
        'cas_total':cas_total,
        'ens_total':ens_total,
        'tx_cas_total':tx_cas_total,
        'vra_total':vra_total,
    }
    return render(request, 'Production/month.html', context)
