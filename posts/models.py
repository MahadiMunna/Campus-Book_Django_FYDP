from django.db import models
from users.models import UserAccount
# Create your models here.
POST_TYPE=(
    ('Sharing','Sharing'),
    ('borrowing','borrowing'),
)
class PostModel(models.Model):
    post=models.TextField()
    author=models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    post_type=models.CharField(choices=POST_TYPE, max_length=20)
    availability = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Book name - {self.book_name}, {self.post_type} post by {self.author.user.first_name} {self.author.user.last_name}"