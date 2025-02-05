from django.db import models
from django.contrib.auth.models import AbstractBaseUser , UserManager



class CustomUserManager(UserManager):
    def create_user(self,username,email,phone_number,password,**extra_fields):
        if not email:
            raise ValueError('The Email field is required.')
        if not username:
            raise ValueError('The Username field is required.')
        if not phone_number:
            raise ValueError('The Phone number field is required.')
        
        email = self.normalize_email(email)
        user = self.model(username=username , email=email , phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, username, email,phone_number, password, **extra_fields):
        
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email,phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200 , unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11 , unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','phone_number']
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def __str__(self):
        return str(self.email)
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250 , blank=True)
    last_name = models.CharField(max_length=250 , null=True)
    avatar = models.ImageField(upload_to='avatar', blank=True , null=True)
    
    def __str__(self):
        return str(self.user)



class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    # slug = models.SlugField()
    # image = models.ImageField(upload_to='ads')
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=15 , decimal_places=3)
    description = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE , blank=True , null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.title