from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class Status(models.Model):
    owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    upvotes = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['-created']

    @property
    def getUpVote(self):
        reviews = self.statusreview_set.all()
        upVotes = reviews.filter(value='up').count()
        self.upvotes = upVotes

        self.save()

class Statusreview(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value



