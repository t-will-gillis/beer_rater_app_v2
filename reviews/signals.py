from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


def _update_beer_stats(beer):
    approved = beer.reviews.filter(is_approved=True)
    beer.num_reviews = approved.count()
    beer.avg_score = approved.aggregate(avg=Avg("overall"))["avg"] or 0
    beer.save(update_fields=["num_reviews", "avg_score"])


@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    _update_beer_stats(instance.beer)


@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    _update_beer_stats(instance.beer)
