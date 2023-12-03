import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x*2 + y*2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

result_a = a(8)
result_b = b(5, 4)
result_c = c(2, 4, 6, 8, 10)
result_d = d("hiii")

print("Hasil Fungsi a:", result_a)
print("Hasil Fungsi b:", result_b)
print("Hasil Fungsi c:", result_c)
print("Hasil Fungsi d:", result_d)
