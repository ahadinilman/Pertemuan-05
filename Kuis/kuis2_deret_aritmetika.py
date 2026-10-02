print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

while n <= 0:
    print("Banyak suku n harus lebih besar dari 0.")
    n = int(input("Banyak suku n: "))

total = 0.0
suku_list = []

for i in range(n):
    suku = a + i * d
    suku_list.append(suku)
    total += suku

suku_str = ", ".join([f"{x:g}" for x in suku_list])
print(f"Suku: {suku_str}")
print(f"Jumlah: {total:.2f}")