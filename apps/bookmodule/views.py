from django.shortcuts import render
from django.http import HttpResponse

# Task 1 + Task 2 + Task 4 + Task 5
def index(request):
    # parameter from query string
    name = request.GET.get("name") or "world!"
    # render template and pass context
    return render(request, "bookmodule/index.html", {"name": name})

# Task 3: path parameter view
#def index2(request, val1="0"):
  #  try:
     #   n = int(val1)
     #   context = {"val1": n, "error": None}
   # except ValueError:
    #    context = {"val1": None, "error": f"⚠️ error'{val1}' , expected val1 to be integer "}
    
   # return render(request, "bookmodule/index2.html", context)


def index2(request, val1=0): 
    return HttpResponse("value1 = " + str(val1))

# Task 7: view single book details
def viewbook(request, bookId):
    # sample "database" (hard-coded as required by the lab)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)