from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from commentstoreapp.forms import InsertNewComment
from commentstoreapp.models import Comment

# import logging
# logging.basicConfig(level=logging.INFO)

@csrf_protect
def commentstore(request):

    if request.method == 'POST':
        form = InsertNewComment(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["comment_str"]
            d = form.cleaned_data["visit_date"]
            t = Comment(name=n, visit_date=d, comment_str=c)
            t.save()
            
            # for cmnt in cmnt_list:
            #    print(cmnt.name + " : " + cmnt.visit_date.__str__() + " : " + cmnt.comment_str)

            return redirect("home")
    else:
        form = InsertNewComment()

    return render(request, "commentstore/comment.html", {"form": form})


def home(request):
    cmnt_list = list(Comment.objects.all())
    return render(request, "commentstore/home.html", {"cmnt_list": cmnt_list})