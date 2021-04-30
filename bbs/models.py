from django.db import models

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    comment = models.CharField(verbose_name="コメント", max_length=2000)
    title = models.TextField(verbose_name="タイトル", null=True)
    price = models.IntegerField(verbose_name="金額", null=True)


    def __str__(self):
        return self.comment
