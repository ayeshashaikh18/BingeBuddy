import os
import django
import tkinter as tk

# Connect Tkinter to Django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bingebuddy_config.settings"
)

django.setup()

from recommender_app.models import Movie


def recommend_movie():

    selected_mood = mood.get()
    selected_genre = genre.get()

    movies = Movie.objects.filter(
        mood=selected_mood,
        genre=selected_genre
    ).order_by("-rating")

    if movies.exists():

        movie = movies.first()

        result_label.config(

            text=(
                f"🎬 {movie.title}\n\n"
                f"⭐ Rating: {movie.rating}\n"
                f"🎭 Genre: {movie.genre}"
            )

        )

    else:

        result_label.config(
            text="😢 No matching movie found"
        )


# Window

root = tk.Tk()

root.title("BingeBuddy Desktop Recommender")

root.geometry("600x650")

root.configure(bg="#121212")

# Title

title = tk.Label(

    root,

    text="🎬 BingeBuddy",

    font=("Arial", 24, "bold"),

    fg="white",

    bg="#121212"

)

title.pack(pady=20)

# Mood

tk.Label(

    root,

    text="Select Mood",

    font=("Arial", 12, "bold"),

    fg="white",

    bg="#121212"

).pack()

mood = tk.StringVar()

moods = [

    "happy",
    "sad",
    "romantic",
    "thoughtful"

]

for m in moods:

    tk.Radiobutton(

        root,

        text=m.title(),

        variable=mood,

        value=m,

        bg="#121212",

        fg="white",

        selectcolor="#222"

    ).pack()

# Genre

tk.Label(

    root,

    text="Select Genre",

    font=("Arial", 12, "bold"),

    fg="white",

    bg="#121212"

).pack(pady=20)

genre = tk.StringVar()

genres = [

    "action",
    "comedy",
    "drama",
    "romance",
    "scifi"

]

for g in genres:

    tk.Radiobutton(

        root,

        text=g.title(),

        variable=genre,

        value=g,

        bg="#121212",

        fg="white",

        selectcolor="#222"

    ).pack()

# Button

tk.Button(

    root,

    text="Recommend Movie",

    command=recommend_movie,

    bg="#ff4b5c",

    fg="white",

    font=("Arial", 12, "bold"),

    padx=20,

    pady=10

).pack(pady=30)

# Result

result_label = tk.Label(

    root,

    text="",

    font=("Arial", 16, "bold"),

    fg="yellow",

    bg="#121212",

    justify="center"

)

result_label.pack(pady=20)

root.mainloop()