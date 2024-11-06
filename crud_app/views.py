# crud_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
#from django.db.models import Q

# List (Read)
def book_list(request):
    books = Book.objects.all()
    return render(request, template_name='book_list.html', context={'books': books})

# Create
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='book_list')
    else:
        form = BookForm()
    return render(request, template_name='book_form.html', context={'form': form})

# Update
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='book_list')
    else:
        form = BookForm(instance=book)
    return render(request, template_name='book_form.html', context={'form': form})

# Delete
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name='book_confirm_delete.html', context={'book': book})

#for testing purpose
def testing(request):
    return render(
        request,
        template_name="templ.html",
        context={
            'books': Book.objects.order_by('-title').values()
        }
    )
