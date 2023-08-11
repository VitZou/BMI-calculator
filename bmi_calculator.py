# VÝPOČET BMI
# BMI = váha v kg / (výška v metrech) na druhou mocninu

height = input("Zadejte svou výšku v metrech (NE V CENTIMETRECH!!!):\n")
weight = input("Zadejte svou váhu v kg:\n")

counting = round(float(weight) / float(height)**2)

print(f"Vaše BMI je: {counting}")