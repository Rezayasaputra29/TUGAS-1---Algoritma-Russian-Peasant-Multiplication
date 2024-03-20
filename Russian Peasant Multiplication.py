def russian_peasant_multiplication(a, b):
    result = 0
    while a > 0:
        if a % 2 == 1:
            result += b
        a //= 2
        b *= 2
    return result

def main():
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    hasil = russian_peasant_multiplication(bilangan1, bilangan2)
    print(f"Hasil dari {bilangan1} x {bilangan2} adalah {hasil}")

if __name__ == "__main__":
    main()
