def units_produced(units_per_hour, hours_worked):
    return units_per_hour * hours_worked

def shift_report(shift_name, units_per_hour, hours_worked):
    units = units_produced(units_per_hour, hours_worked)

    return "shift", shift_name, ":", units, "units produced"

def weekly_report():
    shifts = ["alpha", "beta", "gamma"]
    shift_hours_worked = ["10", "3", "8"]

    for name, hours in [range(0,3), range(0, 3)]:
        print(shift_report(shifts[name], shift_hours_worked[hours]))

weekly_report()