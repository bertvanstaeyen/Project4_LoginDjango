from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link.
# This is the profile class.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()


# This class is made for the serialnumber so this can be changed and saved.
class SerialNumber(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    serialNumber = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.serialNumber


# This class is used for authentication.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


# This is auto generated Django code for authentication.
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


# This is auto generated Django code for authentication.
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


# This is auto generated Django code for authentication and is used to check the user.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


# This is auto generated Django code for authentication.
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


# This is auto generated Django code for authentication.
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


# This is auto generated Django code for the admin login.
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


# This is auto generated Django code for content types.
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


# This is auto generated Django code for the migrations.
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


# This is auto generated Django code for session usage.
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


# This is auto generated Django code for authentication.
class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


# This is auto generated Django code for authentication.
class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


# This is auto generated Django code for authentication.
class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


# This is auto generated Django code for authentication.
class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


# This is auto generated Django code for authentication.
class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


# This class is used for the Azure database environment.
class WimhElectricity(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tijdstip = models.DateTimeField()
    switch = models.IntegerField()
    serialmeter = models.CharField(db_column='serialMeter', max_length=15)  # Field name made lowercase.
    currentrate = models.IntegerField(db_column='currentRate')  # Field name made lowercase.
    totaldayconsumption = models.FloatField(db_column='totalDayConsumption')  # Field name made lowercase.
    totalnightconsumption = models.FloatField(db_column='totalNightConsumption')  # Field name made lowercase.
    totaldayproduction = models.FloatField(db_column='totalDayProduction')  # Field name made lowercase.
    totalnightproduction = models.FloatField(db_column='totalNightProduction')  # Field name made lowercase.
    l1consumption = models.FloatField(db_column='l1Consumption', blank=True, null=True)  # Field name made lowercase.
    l2consumption = models.FloatField(db_column='l2Consumption', blank=True, null=True)  # Field name made lowercase.
    l3consumption = models.FloatField(db_column='l3Consumption', blank=True, null=True)  # Field name made lowercase.
    currentconsumption = models.FloatField(db_column='currentConsumption')  # Field name made lowercase.
    l1production = models.FloatField(db_column='l1Production', blank=True, null=True)  # Field name made lowercase.
    l2production = models.FloatField(db_column='l2Production', blank=True, null=True)  # Field name made lowercase.
    l3production = models.FloatField(db_column='l3Production', blank=True, null=True)  # Field name made lowercase.
    currentproduction = models.FloatField(db_column='currentProduction')  # Field name made lowercase.
    l1voltage = models.FloatField(db_column='l1Voltage', blank=True, null=True)  # Field name made lowercase.
    l2voltage = models.FloatField(db_column='l2Voltage', blank=True, null=True)  # Field name made lowercase.
    l3voltage = models.FloatField(db_column='l3Voltage', blank=True, null=True)  # Field name made lowercase.
    l1current = models.FloatField(db_column='l1Current', blank=True, null=True)  # Field name made lowercase.
    l2current = models.FloatField(db_column='l2Current', blank=True, null=True)  # Field name made lowercase.
    l3current = models.FloatField(db_column='l3Current', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'wimh_electricity'

    def __str__(self):
        return self.serialmeter
