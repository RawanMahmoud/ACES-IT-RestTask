from django.db import models




class committee (models.Model):

    name = models.CharField(max_length=50)
    members_no = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class member (models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    committee_ID = models.ForeignKey('committee')

    def __str__(self):
        return self.name





