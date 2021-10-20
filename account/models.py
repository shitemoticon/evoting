from django.core.files import File
from io import BytesIO
from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class AccountManager(BaseUserManager):
    def create_superuser(self,email,password,first_name,last_name,staff_id,department,**kwargs):
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            staff_id = staff_id,
            department = department,
            is_admin = True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_user(self,email,password,first_name,last_name,student_id,course):
       
            user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                student_id = student_id,
                course = course,
            )

            user.set_password(password)
            user.save(using=self._db)
            
            return user



class Account(AbstractBaseUser):
    student_id = models.CharField(max_length=100, blank=True)
    staff_id = models.CharField(max_length=100, blank=True)

    email = models.EmailField(max_length=254,verbose_name='email address', unique=True)
    password = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    course = models.CharField(max_length=255,blank=True)
    department = models.CharField(max_length=255,blank=True)

    is_admin = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

    profile_picture = models.ImageField(upload_to='media/profile_pictures',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='media/thumbnails',null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'password',
        'first_name',
        'last_name',
        'student_id', 
        'staff_id',
        'course',
        'department', 
    ]

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.first_name + '' + self.last_name
    
    def make_thumbnail(self,image,size=(200,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail = File(thumb_io,name=image.name)
        return thumbnail

    def get_thumbnail(self):
        if self.profile_picture:
            self.thumbnail = self.make_thumbnail(self.profile_picture)
            self.save()
            return ("http://localhost:8000" + self.thumbnail.url)
        else:
            return ''
        

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
