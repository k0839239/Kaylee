speed_limit = int(input("Enter a speed limit"))

demeritPoints = 0
while True:
    car_speed = int(input("how fast car is going"))
    
    if car_speed > speed_limit:
        demeritPoints += (car_speed - speed_limit)/5
        print(demeritPoints)
    if demeritPoints >= 12:
        print("license suspeded")
        break
    if car_speed <= speed_limit: 
        print("okay")
