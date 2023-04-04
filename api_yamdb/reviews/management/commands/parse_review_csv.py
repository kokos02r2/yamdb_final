import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Review, Title

PATH = "static/data/"


class Command(BaseCommand):
    help = "import data from review.csv"

    def handle(self, *args, **kwargs):
        with open(f"{PATH}/review.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                title = get_object_or_404(Title, id=row[1])
                review = Review(
                    id=row[0],
                    text=row[2],
                    author=row[3],
                    score=row[4],
                    pub_date=row[5]
                )
                review.save()
                review.title.add(title)
