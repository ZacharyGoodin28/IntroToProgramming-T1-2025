wind_speed = float(input("Enter the wind speed in MPH:"))

if wind_speed < 74:
     print("Tropical Storm")
elif wind_speed < 96:
     print("Category 1 Hurricane")
elif wind_speed < 111:
     print("Category 2 Hurrican")
elif wind_speed < 130:
     print("Category 3 Hurrican")
elif wind_speed < 157:
     print("Category 4 Hurrican")
else:
     print("Category 5 Hurrican")