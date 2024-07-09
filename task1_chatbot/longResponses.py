import random

R_EATING = "I'm a bot. I typically don't eat anything"

R_HOBBIES = "I enjoy learning new things and helping people with their questions. What about you?"
R_WEATHER = "I don't experience weather, but I can help you check the current weather if you'd like!"
R_ORIGIN = "I was created by a team of developers who love AI. What about you, where are you from?"
R_FAVORITE_COLOR = "As a bot, I don't have a favorite color, but I think all colors are beautiful in their own way."

def unknown():
    response = ["Sorry, but I couldn't understand what you said",
                "...",
                "Sounds about right",
                "What does that mean?",
                "Could you please elaborate"][random.randrange(5)]
    return response
