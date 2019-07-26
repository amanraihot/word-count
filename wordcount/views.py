from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter
#function for homepage
def hompage(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    new_list=fulltext.split()
    word_l={}
    for word in new_list:
        if word not in  ['*','---','<','.',':',',','$','...']:
            if word in word_l:
                word_l[word]+=1
            else:
                word_l[word]=1
    new=sorted(word_l.items(),key=itemgetter(1), reverse=True)
    return render(request,'count.html',{'max1':word_l,'count':len(word_l),'new':new})
