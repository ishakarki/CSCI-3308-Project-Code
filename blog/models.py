from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # one to many relationship, used to update the aythor

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # is the user has been deleted, the post also deleted
    def __str__(self):
        return self.title


# use model to create the sql table
# run: python manage.py makemigrations to create migration
# run: python manage.py sqlmiigrate blog 0001
# run:  python manage.py migrate
"""
python manage.py shell

used to interact with the model

Example:
input model in shell
from blog.models import Post   // import blog.model
from django.contrib.auth.models import User  // import user model
User.objects.all() // view all users in the database
user = User.objects.filter(username = 'heaathclief').first()
>>> user
<User: heathclief>
>>> user.id
1
>>> user.pk
1
>>> post_2 = Post(title = 'blog', content = '....', author = user)
>>> post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: blog>]>
>>> User.objects.filter(username = 'heathclief').first()
<User: heathclief>
>>> user.post_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00000213A58D4160>
>>> user.post_set.all()
<QuerySet [<Post: blog>]>
>>> user.post_set.create(title = 'blog 2', content = '...')
<Post: blog 2>
"""
