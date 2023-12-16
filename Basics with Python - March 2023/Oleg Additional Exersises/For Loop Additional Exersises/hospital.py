days = int(input())

counter_pregl = 0
counter_nepregl = 0
doctors = 7

for i in range(1, days + 1):
    patients = int(input())

    if i % 3 == 0 and counter_nepregl > counter_pregl:
        doctors += 1

    if patients <= doctors:
        counter_pregl += patients

    elif patients > doctors:
        counter_pregl += doctors
        counter_nepregl += patients - doctors

print(f"Treated patients: {counter_pregl}.")
print(f"Untreated patients: {counter_nepregl}.")

