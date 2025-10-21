import matplotlib.pyplot as plt

num = input("plase enter number for make: ")

numbers = [float(x) for x in num.split()]

plt.figure(figsize=(10, 5))
plt.bar(range(len(numbers)), numbers)
plt.title("Bar chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()

plt.show()
plt.savefig("bar_chat.png")

print("✔")