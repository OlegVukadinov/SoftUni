from math import floor

serial_name = input()
pcs_seasons = int(input())
pcs_epizodes = int(input())
time_epizodes_without_reclames = float(input())

reclames_time = time_epizodes_without_reclames * 0.20
time_epizod_with_reclames = time_epizodes_without_reclames + reclames_time
special_epizod = pcs_seasons * 10
total_time = time_epizod_with_reclames * pcs_epizodes * pcs_seasons + special_epizod

print(f"Total time needed to watch the {serial_name} series is {floor(total_time)} minutes.")