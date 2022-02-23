from django.db import models
from core import models as core_models


class AbstractItem(core_models.CreatedAndUpdateModel):
    """Abstract Item"""

    name = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        abstract = True
        # 이 클레스는 데이터 베이스에 올라가지 않게된다 movie모델에서 many to many에서 사용되는 용도이기 때문에 설정해주는것

    def __str__(self):
        return self.name  # admin 페이지에서 각각 이름 주기 (필수 아님)


class HashtagType(AbstractItem):
    pass


class Nft(core_models.CreatedAndUpdateModel):

    """NFT 모델입니다 :)"""

    title = models.CharField(max_length=30, default="")
    hashtag_list = models.ManyToManyField(HashtagType, null=True)

    def __str__(self):
        return self.title  # admin 페이지에서 각 무비들 이름 주기 (필수 아님)
