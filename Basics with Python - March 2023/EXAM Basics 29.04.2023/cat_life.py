from math import floor

type_cat = input()
cat_sex = input()

if type_cat == "British Shorthair" and cat_sex == 'm':
    cat_mounts = 13 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "British Shorthair" and cat_sex == 'f':
    cat_mounts = 14 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Siamese" and cat_sex == 'm':
    cat_mounts = 15 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Siamese" and cat_sex == 'f':
    cat_mounts = 16 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Persian" and cat_sex == 'm':
    cat_mounts = 14 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Persian" and cat_sex == 'f':
    cat_mounts = 15 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Ragdoll" and cat_sex == 'm':
    cat_mounts = 16 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Ragdoll" and cat_sex == 'f':
    cat_mounts = 17 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "American Shorthair" and cat_sex == 'm':
    cat_mounts = 12 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "American Shorthair" and cat_sex == 'f':
    cat_mounts = 13 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Siberian" and cat_sex == 'm':
    cat_mounts = 11 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")
elif type_cat == "Siberian" and cat_sex == 'f':
    cat_mounts = 12 * 12 / 6
    print(f"{floor(cat_mounts)} cat months")

# if type_cat != "British Shorthair" or type_cat != "Siamese" or type_cat != "Persian" or type_cat != "Ragdoll" \
   # or type_cat != "American Shorthair" or type_cat != "Siberian":
    #print(f'{type_cat} is invalid cat!')
else:
    print(f'{type_cat} is invalid cat!')