from math import ceil

time_for_pictures = int(input())
pcs_scenes = int(input())
scenes_time = int(input())

prep_teren = time_for_pictures * 0.15
time_for_all_scenes = scenes_time * pcs_scenes
needed_time = prep_teren + time_for_all_scenes
diff = abs(needed_time - time_for_pictures)

if needed_time < time_for_pictures:
    print(f"You managed to finish the movie on time! You have {ceil(diff)} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {ceil(diff)} minutes.")