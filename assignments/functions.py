def bmi_calculation(height, weight):
    BMI = weight / ((height / 100) ** 2)
    return BMI   # ✅ BMI qiymatini qaytarish kerak

name = input("Enter your name: ")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# Ideal og‘irlik diapazoni (1.84 metr uchun misol)
W_up = 25.9 * 1.84 ** 2
W_low = 18.5 * 1.84 ** 2

# Funksiyadan natija olish
BMI = bmi_calculation(height, weight)

# BMI ga qarab baholash
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a healthy weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

# Foydalanuvchi uchun qo‘shimcha info
#print(f"{name}, your BMI is {BMI:.2f}")
print(f"Your healthy weight range (for 1.84m height) is from {round(W_low,1)}kg to {round(W_up,1)}kg")
