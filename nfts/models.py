from django.db import models
from core import models as core_models


class Nft(core_models.CreatedAndUpdateModel):

    """NFT 모델입니다 :)"""

    title = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title  # admin 페이지에서 각 무비들 이름 주기 (필수 아님)
