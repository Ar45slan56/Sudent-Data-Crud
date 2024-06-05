from django.shortcuts input render
from DijangoCrud.models import crudst
from django.contrib import messages
def stdisaplay(request):
    results=crudst.objects.all()
    return render(request,"Index.html",{"crudst":results})
def stinsert(request):
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest=crudst()
            savest.stname= request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stgender=request.POST.get('stgender')
            savest.save()
            message.sucess(request,"The Record ",savest.stname,"Is Saved Successfully..!")
            return render(request,"create.html")
        else:
            return render(request,"create.html")
