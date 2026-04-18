class Sonlar:
    def __init__(self):
        self.sonlar = []

    def son_qoshish(self):
        son = input("Son kiriting: ")
        self.sonlar.append(int(son))

    def yigindisi(self):
        return sum(self.sonlar)

    def otrtacha(self):
        return sum(self.sonlar) / len(self.sonlar)

    def eng_katta(self):
        return max(self.sonlar)

    def eng_kichik(self):
        return min(self.sonlar)

    def barcha_hisoblar(self):
        print(f"Sonlar: {self.sonlar}")
        print(f"Yig'indisi: {self.yigindisi()}")
        print(f"O'rtacha qiymati: {self.otracha()}")
        print(f"Eng katta qiymati: {self.eng_katta()}")
        print(f"Eng kichik qiymati: {self.eng_kichik()}")

    def bitta_son_kiritish(self):
        self.son_qoshish()

    def bir_necha_son_kiritish(self):
        n = int(input("Neche son kiritsasiz: "))
        for i in range(n):
            self.son_qoshish()

    def asosiy(self):
        while True:
            print("1. Bitta son kiriting")
            print("2. Bir necha son kiriting")
            print("3. Barcha hisoblar")
            print("4. Chiqish")
            tanlov = int(input("Tanlov: "))
            if tanlov == 1:
                self.bitta_son_kiritish()
            elif tanlov == 2:
                self.bir_necha_son_kiritish()
            elif tanlov == 3:
                self.barcha_hisoblar()
            elif tanlov == 4:
                break
            else:
                print("Noto'g'ri tanlov. Qaytadan tanlovni kiriting.")

son = Sonlar()
son.asosiy()