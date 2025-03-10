from django.db import models


class TodoList(models.Model):
    title = models.CharField('TODO',max_length=50)
    description = models.TextField('설명')
    start_date = models.DateField('시작일')
    end_date = models.DateField('마감일')
    is_completed = models.BooleanField('완료 여부',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
