from django.shortcuts import render

# عرض الصفحة الرئيسية
def index(request):
    return render(request, "bookmodule/index.html")

# عرض قائمة الكتب
def list_books(request):
    return render(request, "bookmodule/list_books.html")

# عرض تفاصيل كتاب واحد (مثلاً لما المستخدم يختار كتاب)
def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

# عرض صفحة "من نحن"
def aboutus(request):
    return render(request, "bookmodule/aboutus.html")
