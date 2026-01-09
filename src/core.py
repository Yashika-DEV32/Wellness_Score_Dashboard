# core.py
import pandas as pd

def compute_wellness(row, w_sleep=0.4, w_steps=0.3, w_mood=0.3):
    """
    Compute wellness score (0-100) based on sleep_hours, steps, and mood.
    Weights:
        Sleep: 40%
        Steps: 30%
        Mood: 30%
    """
    sleep_score = min(row['sleep_hours'] / 8, 1)*100
    steps_score = min(row['steps'] / 10000, 1)*100
    mood_score = (row['mood'] / 10)*100
    return round(sleep_score * w_sleep + steps_score * w_steps + mood_score * w_mood, 2)

def calculate_wellness_from_csv(file_path):
    df = pd.read_csv(file_path)
    df['wellness_score'] = df.apply(compute_wellness, axis=1)
    return df
