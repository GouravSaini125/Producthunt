from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    hunter = models.ForeignKey(User,related_name = 'creator', on_delete=models.CASCADE)
    response = models.ManyToManyField(User,through='Response',related_name='user_response',blank=True)
#     response = models.ManyToManyField(User,related_name='user_response',blank=True)

    def summary(self):
        return self.body[:115]+'...'

    def stitle(self):
        if len(self.title) > 27:
            return self.title[:25]+'...'
        else:
            return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Response(models.Model):
    
    LIKE = 'like'
    DISLIKE = 'dislike'
    NONE = 'none'
    CHOICES = (
        (LIKE,'Like'),
        (DISLIKE,'Dislike'),
        (NONE,'None'),
    )

    user = models.ForeignKey(User,related_name='responser',on_delete=models.CASCADE)
    lproduct = models.ForeignKey('Product',related_name ='responsed_product',on_delete=models.CASCADE)
    choice = models.CharField(max_length=7,choices=CHOICES, default=NONE)

    def __str__(self):
        return str(self.user)+' '+self.choice+' '+str(self.lproduct)

# from django.db import models 


# class Pizza(models.Model):

#     name = models.CharField(max_length=30)
#     toppings = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas')
#     def __str__(self):
#         return self.name


# class Topping(models.Model):

#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class ToppingAmount(models.Model):

#     REGULAR = 1
#     DOUBLE = 2
#     TRIPLE = 3
#     AMOUNT_CHOICES = (
#         (REGULAR, 'Regular'),
#         (DOUBLE, 'Double'),
#         (TRIPLE, 'Triple'),
#     )

#     pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
#     topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
#     amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
