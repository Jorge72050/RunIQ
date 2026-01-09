valid_profile = {
    "basic_information": {
        "name": "John Doe",
        "date_of_birth": "2004-12-15",
        "gender": "Male",
        "prev_injury": False,
        "specific_injury": None,
        "weight": 150
    },
    "running_history": {
        "new_to_running": False,
        "trained_for_race": True,
        "trained_properties": {
            "trained_weekly_mileage": 30,
            "trained_pace": 480
        },
        "weekly_mileage": 20,
        "running_how_long": 18
    },
    "goals": {
        "goal_race": "Marathon",
        "date_of_race": "2026-02-15",
        "goal_pace": 450
    },
    "lifestyle": {
        "hours_of_sleep": 7,
        "diet": ""
    }
}

invalid_profile = {
    "basic_information": {
        "name": "John Doe",
        "date_of_birth": "not-a-date",  # invalid date
        "gender": "Male",
        "prev_injury": False,
        "weight": 150
    }
}