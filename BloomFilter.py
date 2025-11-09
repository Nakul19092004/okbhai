# ============================
# Simple Bloom Filter Example
# ============================

size = 15          # Bit array size (jitna bada, utni accuracy)
hash_count = 2     # Kitne hash functions (2 kaafi hain)
bit_array = [0] * size  # Initially sab 0 hai


# Function to add number
def add(num):
    # Har number ke liye 2 hash index banayenge aur bit 1 karenge
    for i in range(hash_count):
        idx = hash(str(num) + str(i)) % size   # Hash index nikal lo
        bit_array[idx] = 1                     # Bit ko 1 kar do


# Function to check number present hai ya nahi
def check(num):
    # Har hash index check karo, agar sab 1 hain to True
    for i in range(hash_count):
        idx = hash(str(num) + str(i)) % size
        if bit_array[idx] == 0:
            return False     # Agar koi ek 0 mila to definitely nahi hai
    return True              # Agar sab 1 mile to ho sakta hai present ho


# Kuch numbers add karo filter mein
data = [7, 14, 21, 28]
for n in data:
    add(n)     # Har number ko add kar rahe hain


# Membership check karo
print('7:', check(7))     # True (added)
print('28:', check(28))   # True (added)
print('15:', check(15))   # False (not added)
print('14:', check(14))   # True (added)
print('9:', check(9))     # False (not added)
