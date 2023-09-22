from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("""<h1>Hey i am django Server ,Fuck you Mortal Brain!!!</h1>
    #                     <p>Hey this is coming from django Server</p>
    #                     <hr>
    #                     <h3 style="color:red">hope you are lovng it :)</h3>
    #                     """)
    peoples=[{'name':'A','age':26},
             {'name':'B','age':17},
             {'name':'C','age':28},
             {'name':'D','age':29},
             {'name':'E','age':30}
             ]
    return render(request,"index.html",context={'page':'Django 2023','peoples':peoples})

# Create your views here.
def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html",context)

# Create your views here.
def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)

def success_page(request):
    return HttpResponse("<h1>Hey This is a success page!</h1>")
