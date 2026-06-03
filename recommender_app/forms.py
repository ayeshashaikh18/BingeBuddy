from django import forms

MOOD_CHOICES = [
    ("happy", "Happy"),
    ("sad", "Sad"),
    ("excited", "Excited"),
    ("romantic", "Romantic"),
    ("thoughtful", "Thoughtful"),
]

COMPANION_CHOICES = [
    ("alone", "Alone"),
    ("friends", "Friends"),
    ("family", "Family"),
    ("date", "Date"),
]

LANGUAGE_CHOICES = [
    ("English", "English"),
    ("Hindi", "Hindi"),
]

GENRE_CHOICES = [
    ("action", "Action"),
    ("comedy", "Comedy"),
    ("drama", "Drama"),
    ("romance", "Romance"),
    ("thriller", "Thriller"),
    ("scifi", "Sci-Fi"),
    ("animation", "Animation"),
]

YEAR_RANGE_CHOICES = [
    ("1980-1990", "1980–1990"),
    ("1990-2000", "1990–2000"),
    ("2000-2010", "2000–2010"),
    ("2010-2020", "2010–2020"),
    ("2020-present", "2020–Present"),
]


class MoviePreferenceForm(forms.Form):
    mood = forms.ChoiceField(choices=MOOD_CHOICES)
    companion = forms.ChoiceField(choices=COMPANION_CHOICES)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    year_range = forms.ChoiceField(choices=YEAR_RANGE_CHOICES)