def calculate_bp_level(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic >= 120 and systolic <= 129 and diastolic < 80:
        return "Elevated"
    elif systolic >= 130 and systolic <= 139 or diastolic >= 80 and diastolic <= 89:
        return "High Blood Pressure Stage 1"
    elif systolic >= 140 or diastolic >= 90:
        return "High Blood Pressure Stage 2"
    else:
        return "Hypertensive Crisis"

systolic = int(input("Enter Systolic reading: "))
diastolic = int(input("Enter Diastolic reading: "))

bp_level = calculate_bp_level(systolic, diastolic)

print("Your Blood Pressure level is:", bp_level)
