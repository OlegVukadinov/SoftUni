lenght = int(input())
width = int(input())
height = int(input())
occupied_percent = float(input())

volume_cm = lenght * width * height
volume_liters = volume_cm / 1000
litri_voda = volume_liters - (volume_liters * occupied_percent / 100)
print(litri_voda)




