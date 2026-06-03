from .models import Movie

from django.shortcuts import render, redirect


def landing(request):

    request.session.flush()

    return render(request, "landing.html")


def step1(request):
    if request.method == "POST":
        request.session["mood"] = request.POST.get("mood")
        return redirect("step2")

    return render(request, "step1.html")


def step2(request):
    if request.method == "POST":
        request.session["companion"] = request.POST.get("companion")
        return redirect("step3")

    return render(request, "step2.html")


def step3(request):
    if request.method == "POST":
        request.session["language"] = request.POST.get("language")
        return redirect("step4")

    return render(request, "step3.html")


def step4(request):
    if request.method == "POST":
        request.session["genre"] = request.POST.get("genre")
        return redirect("step5")

    return render(request, "step4.html")


def step5(request):
    if request.method == "POST":
        request.session["year_range"] = request.POST.get("year_range")
        return redirect("results")

    return render(request, "step5.html")


import pandas as pd
from django.conf import settings
import os


from .models import Movie
from .poster_fetcher import fetch_poster, save_resized_poster


def results(request):

    mood = request.session.get("mood")
    companion = request.session.get("companion")
    language = request.session.get("language")
    genre = request.session.get("genre")
    year_range = request.session.get("year_range")


    movies = Movie.objects.all()


    def score_movie(movie):

        score = 0

        if movie.mood == mood:
            score += 1

        if movie.companion == companion:
            score += 1

        if movie.language == language:
            score += 1

        if movie.genre == genre:
            score += 1

        if movie.year_range == year_range:
            score += 1

        return score


    ranked_movies = sorted(
        movies,
        key=lambda movie: (score_movie(movie), movie.rating),
        reverse=True
    )[:3]


    # NEW PART: download posters automatically

    for movie in ranked_movies:

        poster_url = fetch_poster(movie.title)

        local_path = save_resized_poster(poster_url, movie.title)

        movie.poster_local = local_path
        movie.match_score = score_movie(movie)


    return render(
        request,
        "results.html",
        {"movies": ranked_movies}
    )