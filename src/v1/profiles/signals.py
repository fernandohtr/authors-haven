import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from v1.profiles.models import Profile

User = get_user_model()

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def creat_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}'s profile has been created.")
