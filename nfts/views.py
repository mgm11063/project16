from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def index(request):
    all_nfts = models.Nft.objects.all()
    user = request.user.is_authenticated
    if user:
        return render(request, "nfts/nft_list.html", context={"nfts": all_nfts})
    else:
        return redirect(reverse("users:login"))


@login_required(login_url="/users/login/")
def test(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "nfts/test.html")
    else:
        return redirect(reverse("users:login"))
