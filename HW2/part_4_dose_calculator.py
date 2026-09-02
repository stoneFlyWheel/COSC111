# distance must be >= 0, since dividing by zero or by a negative distance produces useless results
def dose_estimate(activity, distance, time_hours):
    """estimates radiation dose based on activity, distance, and time

    activity: the activity of the source in millicuries
    distance: the distance from the source in meters
    time_hours: the time of exposure in hours
    """

    dose = (activity / (distance ** 2)) * time_hours
    return dose

def safe_exposure_time(activity, distance, dose_limit):
    """estimates the safe exposure time based on activity, distance, and dose limit

    activity: the activity of the source in millicuries
    distance: the distance from the source in meters
    dose_limit: the maximum acceptable dose in millicuries
    """

    exposure_time = (dose_limit * (distance ** 2)) / activity
    return exposure_time

print("estimated dose in millicuries:", dose_estimate(activity=50, distance=2, time_hours=3))
print("safe exposure time in hours:", safe_exposure_time(activity=50, distance=2, dose_limit=25))

# writing the precondition is important, because it prevents the function's user from
# making a caller's error, or a valid code input that doesn't produce a valid output