from django.http import HttpResponse
from django.shortcuts import render
from commentstoreapp.commentstore import CommentStore
from commentstoreapp.forms import InsertNewComment
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def commentstore(request):

    store = CommentStore()
    cmnt_list = []

    if request.method == 'POST':
        form = InsertNewComment(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["comment_str"]
            d = form.cleaned_data["visit_date"]
            store.insertcomment(n, d, c)
            cmnt_list = list(store.commentlist.queue)

        return render(request, "commentstore/home.html", {'cmnt_list': cmnt_list})
    else:
        form = InsertNewComment()

    return render(request, "commentstore/comment.html", {"form": form})


def home(request):
    store = CommentStore()
    cmnt_list = list(store.commentlist.queue)
    return render(request, "commentstore/home.html", {'cmnt_list': cmnt_list})