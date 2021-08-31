from django.contrib import admin
from .models import Person
from .models import Feed
from .models import Group
from .models import Member
from .models import Booking
from .models import Workshop
from .models import SensorData
from .models import Plants
from .models import Comment
from .models import *

admin.site.register(Person)
admin.site.register(Feed)
admin.site.register(Group)
admin.site.register(Member)
admin.site.register(Booking)
admin.site.register(Workshop)
admin.site.register(SensorData)
admin.site.register(Plants)
admin.site.register(Comment)

# Register your models here.
admin.site.register(Users)
