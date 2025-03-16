import os
import csv
from django.core.management.base import BaseCommand
from Wordbase.word import SpellingBeeWord


# NOTE: 
# THIS WILL NOT WORK UNTIL DJANGO IMPLEMENTATION IS DONE, NO TESTING HAS BEEN DONE
# eg python manage.py import_words <path_to_csv_file>
# This command will import words from a CSV file into the database.

class Command(BaseCommand):
    help = "Import spelling bee words from CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the CSV word list file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        
        words_added = 0
        words_updated = 0
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    word = row.get('word', '').strip().lower()
                    
                    if not word:
                        continue
                    word_obj, created = SpellingBeeWord.objects.get_or_create(word=word)                    
                    for field, value in row.items():
                        if field != 'word' and hasattr(word_obj, field):
                            setattr(word_obj, field, value.strip())
                    word_obj.save()
                    if created:
                        words_added += 1
                    else:
                        words_updated += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing word {word}: {str(e)}'))
        self.stdout.write(
            self.style.SUCCESS(f"Import complete: {words_added} words added, {words_updated} words updated")
        )