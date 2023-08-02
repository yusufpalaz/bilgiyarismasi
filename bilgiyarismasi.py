def get_user_choice():
    user_choice = input("Cevabınızı girin (A, B, C, D): ").upper()
    while user_choice not in ["A", "B", "C", "D"]:
        user_choice = input("Geçerli bir seçim yapın (A, B, C, D): ").upper()
    return user_choice

def play_again():
    choice = input("Tekrar oynamak istiyor musunuz? (evet/hayır): ").lower()
    return choice == "evet"

def main():
    questions = [
        {
            "question": "Python programlama dili hangi yıl piyasaya sürülmüştür?",
            "choices": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"],
            "correct_answer": "B"
        },
        {
            "question": "Dünyadaki en yüksek dağ zirvesi hangisidir?",
            "choices": ["A) Mont Everest", "B) K2", "C) Kangchenjunga", "D) Lhotse"],
            "correct_answer": "A"
        },
        {
            "question": "Hangi gezegen Güneş Sistemi'ndeki en büyük gezegendir?",
            "choices": ["A) Mars", "B) Jüpiter", "C) Neptün", "D) Venüs"],
            "correct_answer": "B"
        }
        # Dilediğiniz kadar soru ekleyebilirsiniz.
    ]

    print("Bilgi Yarışması'na hoş geldiniz!")
    score = 0

    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        user_choice = get_user_choice()
        if user_choice == question["correct_answer"]:
            print("Tebrikler, doğru cevap!")
            score += 1
        else:
            print("Üzgünüm, yanlış cevap!")

    print(f"Toplam puanınız: {score}/{len(questions)}")
    if play_again():
        main()
    else:
        print("Oyundan çıkılıyor...")

if __name__ == "__main__":
    main()
