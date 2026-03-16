from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Beer


def _update_brewery_stats(brewery):
    if brewery is None:
        return
    approved = brewery.beers.filter(is_approved=True)
    brewery.num_beers = approved.count()
    brewery.avg_score = approved.aggregate(avg=Avg("avg_score"))["avg"] or 0
    brewery.save(update_fields=["num_beers", "avg_score"])


@receiver(post_save, sender=Beer)
def beer_saved(sender, instance, **kwargs):
    _update_brewery_stats(instance.brewery)


@receiver(post_delete, sender=Beer)
def beer_deleted(sender, instance, **kwargs):
    _update_brewery_stats(instance.brewery)
