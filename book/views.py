from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from book.forms import BookForm
from book.models import Book

# Create your views here.
def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'book successfully registered')
            return HttpResponseRedirect(reverse('getAllBooks'))
        else:
            #messages.error(request, 'fill out the form correctly')
            return HttpResponseRedirect(reverse('createBook'))

    form = BookForm()
    context = {'form': form}
    return render(request, 'book/create.html', context=context)

def getAllBooks(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/books.html', context=context)

def updateBook(request, idBook):
    try:
        book = Book.objects.get(pk=idBook)
    except ObjectDoesNotExist:
        #messages.error(request, 'book does not exist')
        return HttpResponseRedirect(reverse('getAllBooks'))
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'book updated successfully')
            return HttpResponseRedirect(reverse('getAllBooks'))
        else:
            #messages.error(request, 'fill out the form correctly')
            return HttpResponseRedirect(reverse('updateBook', args=[idBook]))

    form = BookForm(instance=book)
    context = {'form': form, 'book': book}
    return render(request, 'book/update.html', context=context)

def deleteBook(request, idBook):
    try:
        book = Book.objects.get(pk=idBook)
        book.delete()
        #messages.success(request, 'book deleted successfully')
    except ObjectDoesNotExist:
        pass
        #messages.error(request, 'book does not exist')

    return HttpResponseRedirect(reverse('getAllBooks'))
    
def getBook(request, idBook):
    try:
        book = Book.objects.get(pk=idBook)
    except ObjectDoesNotExist:
        #messages.error(request, 'book does not exist')
        return HttpResponseRedirect(reverse('getAllBooks'))

    context = {'book': book}
    return render(request, 'book/book.html')

    