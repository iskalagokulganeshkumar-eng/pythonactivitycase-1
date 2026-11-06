vehicle=input("enter the type of vehicle : ")
hours=int(input("enter the parking time: "))
if vehicle == "car":
    rate=20
else:
    rate=10
total_free = hours*rate
if total_free > 50:
    total_free = 50
print(f"vehicle type:{vehicle}")
print(f"total parking fee:{total_fee}")