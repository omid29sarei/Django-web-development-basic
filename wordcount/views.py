from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            # Increase Here
            word_dict[word] += 1
        else:
            # Add to the dictionary
            word_dict[word] = 1
    sorted_word = sorted(
        word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {
                      'fulltext': fulltext,
                      'count': len(wordlist),
                      'word_dict': sorted_word
                  }
                  )
