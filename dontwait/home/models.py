from django.db import models
from django.utils import timezone

class Court(models.Model):
    name = models.CharField(max_length=200)

    adress = models.CharField(max_length=300)
    maxtime = models.IntegerField(default=90)

    booked = models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(max_length=200)

    def __repr__(self):
        return f"< Court: {self.slug} >"

    def save(self, *args, **kwargs):
        super(Court, self).save(*args, **kwargs)
        self.slug = str(self.id + 100)
        super(Court, self).save(*args, **kwargs)
        print("updated booked time: ", self.booked)

    def occupied(self):
        if self.booked <= timezone.now():
            #print(self.booked, timezone.now())
            return False
        return True


    def get_unix(self):
        print(self.booked)
        return str(self.booked)
