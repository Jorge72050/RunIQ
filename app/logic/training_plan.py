# app/logic/training_plan.py

from datetime import datetime, timedelta

# Based on Strava's marathon prep article + health factors that commonly affect running
# Average starting time derived from RunRepeat's article on times based on gender + percentile
# Start with basic marathon plan

def build_plan(profile):
    
    # Initializing all variables
    prev_injury = profile["basic_info"]["prev_injury"]
    dob = (int(num) for num in profile["basic_info"]["date_of_birth"].split("-"))
    gender = profile["basic_info"]["gender"]
    injury_type = profile["basic_info"]["specific_injury"]
    new_to_running = profile["running_history"][""]
    weekly_mileage = profile["running_history"]["weekly_mileage"]
    goal_distance = profile["goals"]["goal_distance"]
    date_of_race = profile["goals"]["date_of_race"]
    age = (datetime.today() - datetime(dob[0], dob[1], dob[2])) // 365

    # If new to running, start out with lower intensity work, basic mileage - 
    # Then get to real workout plan. Ease them into running
    
    # Otherwise, they can jump into the plan
    # Will determine average times based on male or female - assuming mostly new runners. 
    # Based off of 50th percentile values for times and weights
    # As weight increases past 50th percentile and age increase (past 30), decrease starting running pace by fixed amount
    
    # Conditions and their effects:
        # <7 hours of sleep - Increases paces by 5%, aerobic endurance decreases by 8-12%
        # Injury recovery - implement second recovery day and increase
    
    # All avg times in seconds for easier calculations, paces in sec/mile
    male_avg5k_time = (31 * 60) + 28                # 34:37
    male_avg5k_pace = male_avg5k_time // 3.11        
    male_avg10k_time = (57 * 60) + 15               # 1:02:08
    male_avg10k_pace = male_avg10k_time // 6.22 
    male_avghalf_time = (1 * 60 + 59) * 60 + 48     # 1:59:48
    male_avghalf_pace = male_avghalf_time // 13.1
    male_avgmar_time = (4 * 60 + 14) * 60 + 29      # 4:14:29
    male_avgmar_pace = male_avgmar_time // 26.2
    female_avg5k_time = (37 * 60) + 28              # 37:28
    female_avg5k_pace = female_avg5k_time // 3.11
    female_avg10k_time = (66 * 60) + 54             # 1:06:54
    female_avg10_pace = female_avg10k_time // 6.22
    female_avghalf_time = (2 * 60 + 24) * 60 + 3    # 2:24:03
    female_avghalf_pace = female_avghalf_time // 13.1
    female_avgmar_time = (4 * 60 + 42) * 60 + 9     # 4:42:09
    female_avgmar_pace = female_avgmar_time // 26.2
    
    # Basic statistics (lbs)
    male_avgweight = 199.8
    female_avgweight = 170.6

    # Performance (pace) decreases by this factor every year, assuming starting from new
    age_factor = 0.075
    plan = {}
    if gender == "Male":

        # Assumes average paces
        if new_to_running:
            if age > 30:



            # For simplicity, each
            standard_plan()
        if age > 30:
            
        
        if goal_distance == "Marathon":

    
    else:


def standard_plan()