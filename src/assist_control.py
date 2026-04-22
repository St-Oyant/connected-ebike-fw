MAX_ASSIST_LEVEL = 4
THERMAL_DERATING_START_C = 75
LOW_BATTERY_LIMIT_PERCENT = 15

def compute_assist_level(battery_percent, temperature_c, rider_mode):
    assist = rider_mode

    if battery_percent < LOW_BATTERY_LIMIT_PERCENT:
        assist = min(assist, 2)

    if temperature_c >= THERMAL_DERATING_START_C:
        assist = min(assist, 1)

    return max(0, min(assist, MAX_ASSIST_LEVEL))


if __name__ == "__main__":
    print(compute_assist_level(40, 60, 3))
