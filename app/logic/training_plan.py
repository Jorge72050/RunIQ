# app/logic/training_plan.py

from datetime import datetime
from all_workouts import track_glossary, track_workouts, tempo_workouts, glossary_tempo, \
    hill_workouts, glossary_hills,strcond_workouts, shakeouts_workouts, introduction_runners, \
    mobility_workouts, cross_and_mobility_workouts, longrun_workouts

# Based on Strava's marathon prep article + health factors that commonly affect running
# Average starting time derived from RunRepeat's article on times based on gender + percentile
# Start with basic marathon plan

def build_plan(profile):
    
    # Initializing all variables
    request_date = profile["basic_info"]["request_date"]
    prev_injury = profile["basic_info"]["prev_injury"]
    dob = (int(num) for num in profile["basic_info"]["date_of_birth"].split("-"))
    gender = profile["basic_info"]["gender"]
    injury_type = profile["basic_info"]["specific_injury"]
    new_to_running = profile["running_history"][""]
    weekly_mileage = profile["running_history"]["weekly_mileage"]
    goal_distance = profile["goals"]["goal_distance"]
    date_of_race = (int(val) for val in profile["goals"]["date_of_race"].split("-"))
    age = (datetime.today() - datetime(dob[0], dob[1], dob[2])) // 365
    longrun_day = profile["goals"]["longrun_day"]
    plan_length = profile["goals"]["plan_length"]

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
    # Paces will be used for time estimates and if a goal pace is set
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
    
    # Basic statistics
    male_avgweight = 199.8      #lbs
    female_avgweight = 170.6    #lbs
    new_runner_km = 3
    max_hr = 208 - 0.7 * age
    zone1_lower = 0.5 * max_hr
    zone1_upper = 0.6 * max_hr
    zone2_lower = 0.6 * max_hr
    zone2_upper = 0.7 * max_hr
    zone3_lower = 0.7 * max_hr
    zone3_upper = 0.8 * max_hr
    zone4_lower = 0.85 * max_hr
    zone4_upper = 0.9 * max_hr
    zone5_base = 0.85 * max_hr
    zone5_upper = 0.95 * max_hr
    age_factor = 0.075
    plan = {}

    # Have plans start the day after
    start_date = compute_plan_start(request_date, longrun_day)
    current_date = start_date
    new_mar_planlength = 24 * 7
    exp_mar_planlength = 16 * 7
    new_half_planlength = 12 * 7
    exp_half_planlength = 8 * 7
    days_until_race = date_of_race - start_date

#################################################################
################# PLAN CALCULATION ###################
#################################################################
    if new_to_running:
        plan = basic_newrunner_plan(goal_distance, plan, current_date, date_of_race)
    match goal_distance:
        case "Marathon":
            plan = basic_mar_plan(new_to_running, plan, current_date, date_of_race)
        case "Half-Marathon":
            plan = basic_halfmar_plan(new_to_running, plan, current_date, date_of_race)
        case "10k":
            plan = basic_10k_plan(new_to_running, plan, current_date, date_of_race)

# Plan keys formatted as "Week x, month_name day (YYYY-MM-DD)"

def basic_mar_plan(new_to_running, plan, current_date, date_of_race):
    offset = 0
    if new_to_running:
        offset = 9
    for w in range(1, 17):
        month_name = current_date.strftime("B%")
        curr_key = f"Week {w + offset},{month_name} {datetime.ordinal(day)} ({current_date})"
        plan[curr_key] = {}
        current_plan = plan[curr_key]
        for d in range (1, 8):
            month_name = current_date.strftime("B%")
            day = current_date.day
            curr_key = f"Week {w + offset},{month_name} {datetime.ordinal(day)} ({current_date})"
            if current_date == date_of_race:
                return "Race Day! ..." ## Some inspirational message
            match d:
                case 1:
                    if w in (13, 14, 15, 16):
                        current_plan[curr_key] = mobility_workouts[w-12]
                    else:
                        current_plan[curr_key] = strcond_workouts[w]
                case 2:
                    current_plan[curr_key] = track_workouts[w]
                case 3:
                    current_plan[curr_key] = cross_and_mobility_workouts[w]
                case 4:
                    if w in (4,8,12):
                        current_plan[curr_key] = hill_workouts[w//4]
                    elif w == 16:
                        current_plan[curr_key] = tempo_workouts[12]
                    else:
                        current_plan[curr_key] = tempo_workouts[w]      
                case 5:
                    current_plan[curr_key] = "Rest + Recovery"
                case 6:
                    current_plan[curr_key] = shakeouts_workouts[w]
                case 7:
                    current_plan[curr_key] = longrun_workouts
            current_date + datetime.timedelta(days=1)
    return plan

## Assumes half of the training of a regular marathon plan
def basic_halfmar_plan(new_to_running, plan, current_date, date_of_race):
    offset = 0
    counter = 1
    if new_to_running:
        offset = 4
        # Do weeks 1: 1,3, 2: 3, 4, 3: 2,3, 4: 2, 4.
        # --> weeks 1, 3, 7, 8, 10, 11, 14, 16
    for w in (1, 3, 7, 8, 10, 11, 14, 16):
        month_name = current_date.strftime("B%")
        day = current_date.day
        curr_key = f"Week {counter + offset},{month_name} {datetime.ordinal(day)} ({current_date})"
        plan[curr_key] = {}
        current_plan = plan[curr_key]
        counter += 1
        for d in range(1, 8):
            month_name = current_date.strftime("B%")
            day = current_date.day
            curr_key = f"Week {w + offset},{month_name} {datetime.ordinal(day)} ({current_date})"
            if current_date == date_of_race:
                return "Race Day! ..." ## Some inspirational message
            match d:
                case 1:
                    if w in (13, 14, 15, 16):
                        current_plan[curr_key] = mobility_workouts[w-12]
                    else:
                        current_plan[curr_key] = strcond_workouts[w]
                case 2:
                    current_plan[curr_key] = track_workouts[w]
                case 3:
                    current_plan[curr_key] = cross_and_mobility_workouts[w]
                case 4:
                    if w in (4,8,12):
                        current_plan[curr_key] = hill_workouts[w//4]
                    elif w == 16:
                        current_plan[curr_key] = tempo_workouts[12]
                    else:
                        current_plan[curr_key] = tempo_workouts[w]      
                case 5:
                    current_plan[curr_key] = "Rest + Recovery"
                case 6:
                    current_plan[curr_key] = shakeouts_workouts[w]
                case 7:
                    current_plan[curr_key] = longrun_workouts
            current_date + datetime.timedelta(days=1)
    return plan

def basic_10k_plan(goal_distance, plan, current_date, date_of_race):
    pass

def basic_newrunner_plan(goal_distance, plan, current_date, date_of_race):
    match goal_distance:
        case "Marathon":
            for w in range(1, 9):
                month_name = current_date.strftime("B%")
                day = current_date.day
                curr_key = f"Week {counter},{month_name} {datetime.ordinal(day)} ({current_date})"
                plan[curr_key] = {}
                current_plan = plan[curr_key]
                counter += 1
                for d in range(1,8):
                    month_name = current_date.strftime("B%")
                    day = current_date.day
                    curr_key = f"Week {counter},{month_name} {datetime.ordinal(day)} ({current_date})"
                    match d:
                        case 1:
                            current_plan[curr_key] = introduction_runners[1]

        case "Half-Marathon":
            for w in range(1,4):
                month_name = current_date.strftime("B%")
                day = current_date.day
                curr_key = f"Week {counter},{month_name} {datetime.ordinal(day)} ({current_date})"
                plan[curr_key] = {}
                current_plan = plan[curr_key]
                counter += 1
                for d in range(1,8):
                    month_name = current_date.strftime("B%")
                    day = current_date.day
                    curr_key = f"Week {counter},{month_name} {datetime.ordinal(day)} ({current_date})"
                    match d:
                        case 1:
                            pass
        case "10k":
            pass

def ordinal(n):
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def compute_plan_start(request_date, longrun_day):
    today_wd = request_date.weekday()

    # days until long run day
    days_to_longrun = (longrun_day - today_wd) % 7

    longrun_date = request_date + datetime.timedelta(days=days_to_longrun)

    # start day is the day AFTER long run
    start_date = longrun_date + datetime.timedelta(days=1)

    return start_date
