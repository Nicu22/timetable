import datetime
import pytz
from django.utils import timezone
#202211111646 ATTEMPT — check age of token
import datetime
import pytz
from django.conf import settings
from django.utils import timezone

#UNUSED, DUMP
def custom_create_token(token_model, user, serializer):
    token = token_model.objects.create(user=user)
    utc_now = timezone.now()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    token.created = utc_now
    token.save()
    return token

'''
#absolute state of
def is_he_fresh(token):
    utc_now = timezone.now()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    if token.created < utc_now - settings.TOKEN_TTL:
'''