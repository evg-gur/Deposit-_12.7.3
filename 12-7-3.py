money = int(input("Ввести сумму вклада:"))
per_cent = {"TKB":5.6, "SKB":5.9, "VTB":4.2, "SBER":4.0}
TKB = int((per_cent["TKB"])* (money/100))
SKB = int((per_cent["SKB"])*(money/100))
VTB = int((per_cent["VTB"])*(money/100))
SBER = int((per_cent["SBER"])*(money/100))
deposit = {"TKB":TKB, "SKB":SKB, "VTB":VTB, "SBER":SBER}
print (deposit)

max_number = max(deposit.values())
print("Максимальная сумма, которую вы можете заработать:", max_number)

C:\Users\Пользователь\AppData\Local\Programs\Python\Python38\python.exe C:/Users/Пользователь/PycharmProjects/pythonProject2/main.py
Ввести сумму вклада:100000
{'TKB': 5600, 'SKB': 5900, 'VTB': 4200, 'SBER': 4000}
Максимальная сумма, которую вы можете заработать: 5900

Process finished with exit code 0
