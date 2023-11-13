from django.db import models

# Modifiying Base User Manager and creating Custom User 
from django.contrib.auth.models import BaseUserManager

# Base User Manager class for Modifiying
class UserManager(BaseUserManager):

     # Create User Function will create a normal user
    def create_user(self, email, password=None, **extra_fields):

        # if email is not input than this error will show 
        if not email:
            raise ValueError("User Must have Email")
        
        # If every input is okay than else condition will execute
        else:
            """ 
            this model function will take an email make it normalize(capital
            to smaller) and extra fields 
            """
            user=self.model(email=self.normalize_email(email),
                            **extra_fields)
            #Set_password function will set a password for user.
            # It will encrypt password

            user.set_password(password)

            #saving user in database with using = self._db method
            user.save(using=self._db)

            #Finally returning user for use other functions

            return user
    
    #Create super user function will create a super user or admin for this project
    def create_superuser(self, email, password=None, **extra_fields):
        # calling create user function for creating a super user.
        user= self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        ) 
        #set different function for an admin or super user
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        #saving as super user in database
        user.save(using=self._db)
        # Finally return user
        return user