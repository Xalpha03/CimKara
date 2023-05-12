from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum, Avg, Q
from .forms import *
from django.contrib.auth.models import User
# Create your views here.
def index_view(request):
    etat_page = False
    try:
        etat_page = True
        posts_date = request.GET.get('get_date')
        posts_name = request.GET.get('name_user')
        #posts_name = User.objects.filter(username=posts_name)
        #posts_article = Article.objects.filter(created = get_date).order_by('created').order_by('-id')
        print("=="*5, posts_date, posts_name, "=="*5)
        posts_livr = Article.objects.filter(Q(created=posts_date)).aggregate(liv=Sum('livraison'))
        posts_casse = Article.objects.filter(Q(created=posts_date)).aggregate(cas=Sum('casse'))
        posts_ensache = Article.objects.filter(Q(created=posts_date)).aggregate(ens=(Sum('livraison'))*20)
        posts_tx_casse = Article.objects.filter(created=posts_date).aggregate(tx_cas=Avg('tx_casse'))

        

    #posts_date = request.GET.get('get_date') 
    


        posts_user = User.objects.all().order_by('-id')
        posts_article = Article.objects.all().order_by('-id')

        livr_total = Article.objects.all().aggregate(liv=Sum('livraison'))
        casse_total = Article.objects.all().aggregate(cas=Sum('casse'))
        ensa_total= Article.objects.all().aggregate(ens=(Sum('livraison'))*20)
        tx_case_total = Article.objects.all().aggregate(tx_cas=Avg('tx_casse'))

        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('product:index')
            form = ArticleForm()

        context ={
                'posts_user': posts_user,
                'posts_article': posts_article,

                'posts_date':posts_date,
                'posts_livr':posts_livr,
                'posts_casse':posts_casse,
                'posts_ensache':posts_ensache,
                'posts_tx_casse':posts_tx_casse,
            

                'form':form,
                'livr_total':livr_total,
                'casse_total':casse_total,
                'ensa_total':ensa_total,
                'etat_page':etat_page,
                'tx_casse_total':tx_case_total,
            }

    except:
        etat_page = False
        #print("=="*5, "bigo", "=="*5)
        context = {'etat_page':etat_page}
    

    return render(request, 'index.html', context)
        
    

def detail_view(request):
    get_id = request.GET.get('id_user')
    if get_id:
       posts_article = Article.objects.filter(name_user=get_id).order_by('-created', '-id')
       print("=="*5, posts_article, "=="*5)

    #calcul des sommes de chaque champs en fonction de l'id de l'utilsateur
    livr_total = Article.objects.filter(name_user=get_id).aggregate(liv=Sum('livraison'))
    casse_total = Article.objects.filter(name_user=get_id).aggregate(cas=Sum('casse'))
    ensa_total = Article.objects.filter(name_user=get_id).aggregate(ens=(Sum('livraison')*20))
    tx_casse_total = Article.objects.filter(name_user=get_id).aggregate(tx_cas=Avg('tx_casse'))



    context = {
        'livr_total':livr_total,
        'casse_total':casse_total,
        'ensa_total':ensa_total,
        'tx_casse_total':tx_casse_total,
        'posts_article':posts_article,
    }
    return render(request, 'product/detail.html', context)

def edite_view(request):
    get_id = request.GET.get('id')
    obj = Article.objects.get(id=get_id)
    form = ArticleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('product:index')
            
    return render(request, 'product/edite.html', {'form': form})
