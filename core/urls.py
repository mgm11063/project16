from django.urls import path
from nfts import views as nft_views

app_name = "core"


urlpatterns = [
    path("", nft_views.index, name="home"),
]
