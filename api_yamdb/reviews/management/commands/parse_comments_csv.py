import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Comment, Review

PATH = "static/data/"


class Command(BaseCommand):
    help = "import data from comments.csv"

    def handle(self, *args, **kwargs):
        with open(f"{PATH}/comments.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                review = get_object_or_404(Review, id=row[1])
                comment = Comment(
                    id=row[0], text=row[2], author=row[3], pub_date=row[4]
                )
                comment.save()
                comment.review.add(review)
