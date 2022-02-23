from django.contrib import admin
from . import models


@admin.register(models.Nft)
class nftsAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    pass
