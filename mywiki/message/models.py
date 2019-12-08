from django.db import models
from user.models import UserProfile
from topic.models import Topic

# Create your models here.
class Message(models.Model):

    topic = models.ForeignKey(Topic)
    content = models.CharField(max_length=100, verbose_name='内容')
    publisher = models.ForeignKey(UserProfile)
    parent_message = models.IntegerField(default=0,verbose_name='父信息id')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message'









