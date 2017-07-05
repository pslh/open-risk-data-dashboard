from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Profile, OptIn,
    KeyCategory, KeyDatasetName, KeyDescription,
    KeyScale, KeyPeril, KeyDataset, KeyTag, KeyTagGroup,
    Dataset, Url)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfilesInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfilesInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(OptIn)

admin.site.register(KeyCategory)
admin.site.register(KeyDatasetName)
admin.site.register(KeyTag)
admin.site.register(KeyTagGroup)
admin.site.register(KeyDescription)
admin.site.register(KeyPeril)
admin.site.register(KeyScale)
admin.site.register(KeyDataset)

admin.site.register(Url)
admin.site.register(Dataset)
