from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from beers.models import Beer
from breweries.models import Brewery
from reviews.models import Review

User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with sample breweries, beers, and reviews"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Breweries
        societe, _ = Brewery.objects.get_or_create(
            name="Societe Brewing Company",
            defaults={
                "city": "San Diego",
                "state": "CA",
                "country": "USA",
                "url": "https://www.societebrewing.com",
                "is_approved": True,
            },
        )
        fremont, _ = Brewery.objects.get_or_create(
            name="Fremont Brewing",
            defaults={
                "city": "Seattle",
                "state": "WA",
                "country": "USA",
                "url": "https://www.fremontbrewing.com",
                "is_approved": True,
            },
        )
        abnormal, _ = Brewery.objects.get_or_create(
            name="Abnormal Beer Company",
            defaults={
                "city": "San Diego",
                "state": "CA",
                "country": "USA",
                "url": "https://www.abnormal.co",
                "is_approved": True,
            },
        )
        eppig, _ = Brewery.objects.get_or_create(
            name="Eppig Brewing",
            defaults={
                "city": "Vista",
                "state": "CA",
                "country": "USA",
                "url": "https://www.eppigbrewing.com",
                "is_approved": True,
            },
        )

        self.stdout.write(f"  Breweries: {Brewery.objects.count()}")

        # Beers
        beers_data = [
            ("Glorious Odds",           societe,   "21c", 7.5, "", "labels/beer1.png"),
            ("Head Full of Dynomite v39", fremont,  "21c", 6.8,
                "Head Full of Dynomite [HFOD] is an ongoing series of hazy IPAs, "
                "each one different from the one before. Check out our website for "
                "the malt and hops used in the one in your hand...FremontBrewing.com",
                "labels/beer2.png"),
            ("10:45 to Denver",         abnormal,  "21a", 7.0,
                "Contemporary West Coast IPA that celebrates San Diego's historic hoppy "
                "heritage. Intense aromas of dank Mosaic hops are backed up with pleasant "
                "pine and grapefruit notes from Cascade hops.",
                "labels/beer3.png"),
            ("Boss Pour",               eppig,     "21a", 7.0,
                "A soft bitterness from the Nugget and Cascade hops make this a classic IPA. "
                "The addition of the aromatic Mosaic and Citra hops lend grapefruit and "
                "tropical citrus notes.",
                "labels/beer4.png"),
            ("The Pupil",               societe,   "21a", 7.0, "", "labels/beer5.png"),
        ]

        glorious_odds = None
        for name, brewery, style, abv, notes, label_path in beers_data:
            beer, _ = Beer.objects.get_or_create(
                name=name,
                defaults={
                    "brewery": brewery,
                    "style": style,
                    "abv": abv,
                    "beer_notes": notes,
                    "is_approved": True,
                },
            )
            if not beer.label:
                beer.label = label_path
                beer.save(update_fields=["label"])
            if name == "Glorious Odds":
                glorious_odds = beer

        self.stdout.write(f"  Beers: {Beer.objects.count()}")

        # User
        user, created = User.objects.get_or_create(
            email="someone@somesite.com",
            defaults={"username": "someone@somesite.com"},
        )
        if created:
            user.set_password("changeme123")
            user.save()

        self.stdout.write(f"  Users: {User.objects.count()}")

        # Review
        Review.objects.get_or_create(
            beer=glorious_odds,
            author=user,
            defaults={
                "overall": 9.0,
                "review": "Another great one from Societe",
                "is_approved": True,
            },
        )

        self.stdout.write(f"  Reviews: {Review.objects.count()}")
        self.stdout.write(self.style.SUCCESS("Done."))
