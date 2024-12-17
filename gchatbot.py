import re
import random
import time

# Kullanıcı bilgileri ve sohbet geçmişi
user_data = {
    "name": None,
    "mood": None,
    "interests": [],
    "previous_conversations": []
}

chat_history = []

# Yanıtlar ve konular
intents = {
    "greeting": {
        "patterns": ["merhaba", "selam", "günaydın", "nasılsın?", "iyi misin?", "ne haber?"],
        "responses": ["Merhaba! Nasılsınız?", "Selam! Bugün nasılsınız?", "Günaydın! Size nasıl yardımcı olabilirim?"]
    },
    "goodbye": {
        "patterns": ["hoşça kal", "görüşürüz", "iyi günler", "bye", "exit"],
        "responses": ["Hoşça kal!", "Görüşürüz, kendine iyi bak!", "Hoşça kal, görüşmek üzere!"]
    },
    "thanks": {
        "patterns": ["teşekkür ederim", "sağ ol", "teşekkürler", "çok sağ ol"],
        "responses": ["Rica ederim!", "Her zaman yardımcı olurum!", "Bir şey değil!"]
    },
    "how_are_you": {
        "patterns": ["nasılsın?", "iyi misin?", "ne haber?", "keyfin nasıl?"],
        "responses": ["İyiyim, teşekkür ederim! Sen nasılsın?", "Ben de iyiyim, sağ ol! Sen nasılsın?"]
    },
    "mood": {
        "patterns": ["üzgünüm", "mutluyum", "çok neşeliyim", "keyfim yok", "mutsuzum"],
        "responses": {
            "üzgünüm": ["Üzgün olduğunu duyduğuma üzüldüm. Ne oldu?", "Herkesin kötü günleri olur. Kendini daha iyi hissetmeni diliyorum."],
            "mutluyum": ["Mutlu olduğunu duyduğuma sevindim!", "Harika! Umarım mutluluğun devam eder!"],
            "keyfim yok": ["Bazen moral bulmak zor olabilir, ama her şey geçer. Sana yardımcı olabilir miyim?"],
            "neşeliyim": ["Neşelisin, bu çok güzel! Umarım böyle devam eder!"]
        }
    },
    "interests": {
        "patterns": ["hobilerin neler?", "nelerden hoşlanırsın?", "ne ilgin var?"],
        "responses": ["Benim hobim konuşmak! Peki ya senin hobilerin neler?", "Benim için önemli olan, sizinle sohbet etmek. Peki sen nelerden hoşlanırsın?"]
    },
    "time": {
        "patterns": ["saat kaç?", "şu an saat kaç?", "zaman ne?", "saat ne oldu?"],
        "responses": ["Şu anda saat: " + time.strftime("%H:%M:%S")]
    },
    "weather": {
        "patterns": ["hava nasıl?", "hava durumu ne?", "dışarısı nasıl?", "bugün hava nasıl?"],
        "responses": ["Üzgünüm, hava durumu verilerine şu anda erişimim yok. Ama dışarıya bakarak öğrenebilirsin."]
    },
    "name": {
        "patterns": ["adın ne?", "ismin ne?", "senin adın ne?"],
        "responses": ["Benim adım G-Chatbot. Ya senin adın nedir?"]
    },
    "learning": {
        "patterns": ["bunu öğren", "bu konuda ne yapabilirim?", "bunu hatırlamanı istiyorum"],
        "responses": ["Tabii! Öğrenmemi istediğin bir şey var mı?", "Bunu not ediyorum, sana daha iyi yardımcı olabilmek için hatırlayacağım."]
    },
    "no_answer": {
        "patterns": ["bilmiyorum", "fikir yok", "emin değilim", "bu konuda ne yapabilirim?"],
        "responses": ["Üzgünüm, bu konuda bir fikrim yok.", "Bu konuda yardımcı olamıyorum.", "Bilmiyorum, ama başka bir konuda yardımcı olabilirim."]
    }
}

# Mesajı temizleme ve küçük harfe çevirme
def clean_input(user_input):
    user_input = re.sub(r'[^\w\s]', '', user_input)  # Noktalama işaretlerini temizle
    return user_input.lower()

# Kullanıcı bilgilerini güncelleme
def update_user_data(user_input):
    if 'name' not in user_data:
        if "adın ne" in user_input.lower() or "ismin ne" in user_input.lower():
            name = re.sub(r"(adın|ismin) ne?", "", user_input, flags=re.IGNORECASE).strip()
            user_data['name'] = name
            return f"Adım {user_data['name']}! Sizin adınız ne?"
        return None
    return None

# Sohbet geçmişini tutma
def add_to_chat_history(user_input, bot_response):
    chat_history.append({"user": user_input, "bot": bot_response})

# Kullanıcının ruh halini öğrenme
def get_mood_response(user_input):
    for mood, data in intents["mood"]["responses"].items():
        if mood in user_input:
            user_data["mood"] = mood
            return random.choice(data)
    return None

# Kullanıcı ilgi alanlarını öğrenme
def get_interests_response(user_input):
    if "hobilerin neler" in user_input or "nelerden hoşlanırsın" in user_input:
        interests = ", ".join(user_data["interests"]) if user_data["interests"] else "Henüz paylaşmadın."
        return f"Benim hobim sohbet etmek. Peki ya senin hobilerin neler? Şu ana kadar şunları söyledin: {interests}"

    return None

# Eş anlamlı kelimelerle eşleştirme
def match_intent(user_input):
    user_input = clean_input(user_input)  # Mesajı temizle

    # Kullanıcı bilgilerini güncelle
    response = update_user_data(user_input)
    if response:
        return response
    
    # Ruh haline göre yanıt ver
    mood_response = get_mood_response(user_input)
    if mood_response:
        return mood_response

    # İlgi alanlarıyla ilgili yanıt ver
    interests_response = get_interests_response(user_input)
    if interests_response:
        return interests_response

    # Öğrenme komutlarına tepki ver
    if "öğren" in user_input or "hatırlama" in user_input:
        return "Tabii, bu konuyu not ediyorum ve gelecekte hatırlayacağım."

    # Kullanıcının mesajına uygun yanıtı bul
    for intent, data in intents.items():
        if intent == "mood" or intent == "weather" or intent == "help":
            continue  
        for pattern in data["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(data["responses"])
    
    return random.choice(intents["no_answer"]["responses"])

# Sohbet başlatma
print("G-Chatbot: Merhaba! Yardımcı olabilir miyim? (Çıkmak için 'exit' yazın.)")

while True:
    user_input = input("Kullanıcı: ")

    if user_input.lower() == "exit":
        print("G-Chatbot: Hoşça kal!")
        break

    # Yanıt üretme
    response = match_intent(user_input)
    
    # Sohbet geçmişine ekle
    add_to_chat_history(user_input, response)

    # Yanıtı kullanıcıya göster
    print(f"G-Chatbot: {response}")
    
                                         # Gizlenmesi gerek! "Sohbet geçmişi"
                                             #print("Sohbet Geçmişi:", chat_history)
    
    
    # Bu Program " Gexnys " tarafından yazılmıştır.
    # Açık kaynak kodludur.
    # İletişim için " developergokhan@proton.me " adresine mail gönderebilirsiniz.
    # ...