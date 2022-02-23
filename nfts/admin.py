from django.contrib import admin
from . import models


@admin.register(models.HashtagType)
class NftTypeAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    pass


@admin.register(models.Nft)
class NftsAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    pass
