import hashlib

def flajolet_martin():
    
    # ---------- USER INPUT ----------
    data = input("Enter elements separated by space: ")
    stream = data.split()  # Split by space into list

    # ---------- ALGORITHM ----------
    def count_trailing_zeros(num):
        binary = bin(num)[2:]
        return len(binary) - len(binary.rstrip('0'))
    
    R = 0
    for item in stream:
        h = hashlib.sha1(item.encode()).hexdigest()
        hv = int(h[:8], 16)
        r = count_trailing_zeros(hv)
        R = max(R, r)
    
    estimate = 2 ** R

    # ---------- OUTPUT ----------
    print("\nData Stream:", stream)
    print("True Unique Elements:", len(set(stream)))
    print("Estimated Unique Elements (Flajolet-Martin):", estimate)


# ---------- RUN ----------
flajolet_martin()
