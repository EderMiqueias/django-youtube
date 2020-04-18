from django.shortcuts import render, get_object_or_404
from .models import Video
from django.contrib import messages
from .forms import ContatoForm
from pymongo import MongoClient
from bson.objectid import ObjectId
from operator import attrgetter

client = MongoClient(host='35.193.200.100',port=2323)
db = client.teste7
colect = db.objects

def index(request):
    form = ContatoForm(request.POST or None)
    videos = list()
    for x in colect.find():
        var = Video(titulo=x['titulo'],tema=x['tema'],url=x['url'],likes=x['likes'],deslikes=x['deslikes'],identification=str(x["_id"]))
        videos.append(var)
    if str(request.method) == 'POST':
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            tema = form.cleaned_data['tema']
            url = form.cleaned_data['url']
            url = str(url).replace("watch?v=","embed/")
            conteudo = {
                'titulo':titulo,
                'tema':tema,
                'url':url,
                'likes':0,
                'deslikes':0
            }
            db.objects.insert_one(conteudo)
            messages.success(request, 'Video Saved Successfully')
            form = ContatoForm()
        else:
            messages.error(request,"Invalid")
    context = {
        'form':form,
        'videos':videos
    }
    return render(request,"index.html",context)

def dislike(request,pk):
    var = colect.find_one({"_id": ObjectId(pk)})
    colect.update_one({"_id": ObjectId(pk)}, {'$set': {'deslikes': var['deslikes'] + 1}})
    return render(request, "dislike.html")

def like(request,pk):
    var = colect.find_one({"_id": ObjectId(pk)})
    colect.update_one({"_id": ObjectId(pk)}, {'$set': {'likes': var['likes'] + 1}})
    return render(request,"like.html")

def classification(request):
    videos = list()
    temas = list()
    for x in colect.find():
        var = Video(titulo=x['titulo'], tema=x['tema'], url=x['url'], likes=x['likes'], deslikes=x['deslikes'],
                    identification=str(x["_id"]), score=int(x['likes']-x['deslikes']))
        videos.append(var)
        if not x['tema'] in temas:
            temas.append(x['tema'])
    videos.sort(key=attrgetter('score'))
    videos = videos[::-1]
    context = {
        'temas':temas,
        'videos': videos
    }
    return render(request, "classification.html",context)