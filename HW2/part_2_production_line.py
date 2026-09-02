shifts = ["alpha", "beta", "gamma"]
shift_hours_worked = [10, 3, 8]
unit_production_rate = 30 # 30 units per hour

# first function
def units_produced(units_per_hour, hours_worked):
    return units_per_hour * hours_worked

# second function, load-bearing for 3rd
def shift_report(shift_name, units_per_hour, hours_worked):
    units = units_produced(units_per_hour, hours_worked)

    return "shift " + shift_name + ": " + str(units) + " units produced"

# da important function!
def weekly_report():
    for index in range(len(shifts)):
        print(shift_report(shifts[index], unit_production_rate, shift_hours_worked[index]))

weekly_report()