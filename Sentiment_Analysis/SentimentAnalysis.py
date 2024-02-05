from textblob import TextBlob
from dataclasses import dataclass



@dataclass
class Mood:
    emoji: str 
    sentimentL: float 



def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = sensitivity

    if polarity >= friendly_threshold:
        return Mood("(:", polarity)
    elif polarity <= hostile_threshold:
        return Mood("):", polarity)
    else:
        return Mood("|:", polarity)


def run_boot():
    print("Enter some to get a sentiment analysis back:")
    while True:
        user_input: str = input("You: ")
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f"Bot: {mood.emoji} ({mood.sentimentL})")

if __name__ == "__main__":
    run_boot()
