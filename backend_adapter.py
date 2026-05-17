import os
import json

USER_FILE = "user_data.json"
ACTIVITY_FILE = "activity_data.json"
ENROLL_FILE = "enroll_data.json"


def init_files():
    # create files with initial data if missing
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

    if not os.path.exists(ACTIVITY_FILE):
        init_act = {
            "Social Gathering": [
                "Handicraft Art Club — Every Thursday 13:00-15:00",
                "Board Game & Leisure Tea Time — Every Sunday 14:00-16:00",
                "Singing & Music Exchange — Every Sunday 10:30-11:30"
            ],
            "Skills Teaching": [
                "Beginner Gardening — Every Sunday 14:00-16:00",
                "Calligraphy Practice — Every Saturday 13:00-16:00",
                "Simple Dessert Baking — Every Friday 10:00-16:00"
            ],
            "Volunteering": [
                "Community Garden Assistance — Every morning 9:00-10:30",
                "Children's Story Reading — Community Library",
                "Senior Digital Device Assistance — Senior Activity Center"
            ],
            "My Activities": []
        }
        with open(ACTIVITY_FILE, "w", encoding="utf-8") as f:
            json.dump(init_act, f, ensure_ascii=False, indent=2)

    if not os.path.exists(ENROLL_FILE):
        with open(ENROLL_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)


def get_all_user():
    with open(USER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_user(user_list):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(user_list, f, ensure_ascii=False, indent=2)


def get_all_activity():
    with open(ACTIVITY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_enroll():
    with open(ENROLL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_enroll(enroll_data):
    with open(ENROLL_FILE, "w", encoding="utf-8") as f:
        json.dump(enroll_data, f, ensure_ascii=False, indent=2)
