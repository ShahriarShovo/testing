from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from user_auth.models.user_manager import UserManager





class User(AbstractBaseUser, PermissionsMixin):
    
    ADMIN = 1
    CUSTOMER = 2
    MALE = 1
    FEMALE = 2

    GOOGLE_SIGNUP=1
    GITHUB_SIGNUP=2
    FACEBOOK_SIGNUP=3
    SITE_SIGNUP =4


    ROLE_CHOOSED                   =                       ((ADMIN, 'admin'),
                                                           (CUSTOMER, 'customer'),)
    GENDER_CHOOSED                 =                       ((MALE, 'male'),
                                                           (FEMALE, 'female'))
    
    SIGNUP_PLATFORM                =                        ((GOOGLE_SIGNUP,'google_signup'),
                                                             (GITHUB_SIGNUP, 'github_signup'),
                                                             (FACEBOOK_SIGNUP,'facebook_signup'),
                                                             (SITE_SIGNUP,'site_signup'),
                                                             )

    first_name                     =                        models.CharField(max_length=50, null=True, blank=True)
    last_name                      =                        models.CharField(max_length=50, null=True, blank=True)
    username                       =                        models.CharField(max_length=50, unique=True)
    email                          =                        models.EmailField(max_length=100, unique=True)
    phone                          =                        models.CharField(max_length=20, blank=True)

    role                           =                        models.PositiveSmallIntegerField(choices=ROLE_CHOOSED,
                                                                              blank=True, null=True)
    
    gender_choosed                 =                        models.PositiveSmallIntegerField(choices=GENDER_CHOOSED,
                                                                              blank=True, null=True)
    sign_up_platform               =                        models.PositiveSmallIntegerField(choices=SIGNUP_PLATFORM,
                                                                              blank=True, null=True)

    # requires fields
    date_joined                    =                        models.DateTimeField(auto_now_add=True)
    last_login                     =                        models.DateTimeField(auto_now_add=True)
    created_date                   =                        models.DateTimeField(auto_now_add=True)
    modify_date                    =                        models.DateTimeField(auto_now=True)
    is_admin                       =                        models.BooleanField(default=False)
    is_staff                       =                        models.BooleanField(default=False)
    is_active                      =                        models.BooleanField(default=False)
    is_superuser                   =                        models.BooleanField(default=False)


    USERNAME_FIELD                 =                        'email'
    # REQUIRED_FIELDS                =                        ['email',]

    objects                        =                         UserManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True