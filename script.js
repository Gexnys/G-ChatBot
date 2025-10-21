function getBotResponse(userText) {
    const lowerCaseInput = userText.toLowerCase();

   
    if (lowerCaseInput.includes("merhaba") || lowerCaseInput.includes("selam") || lowerCaseInput.includes("günaydın")) {
        return "Merhaba! Hoş geldiniz. Size nasıl yardımcı olabilirim? 😊";
    }
    
  
    if (lowerCaseInput.includes("nasılsın") || lowerCaseInput.includes("iyi misin")) {
        const responses = [
            "Ben iyiyim, teşekkür ederim. Siz nasılsınız? 😄",
            "Harika hissediyorum! Umarım siz de öylesinizdir! 😎",
            "Bugün çok enerjik hissediyorum! Sen nasılsın? 💪"
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }

    if (lowerCaseInput.includes("espiri yap") || lowerCaseInput.includes("şaka yap")) {
        const jokes = [
            "Neden bilgisayarlar soğuktur? Çünkü çok fanatikler! ",
            "İki atom çarpışmış. Biri demiş ki: 'Eyvah, bir elektron kaybettim!' ",
            "Bir kitapla bir CD konuşuyormuş. Kitap demiş ki: 'Benim hayatım çok ilginç!' CD cevap vermiş: 'Ama ben daha çok şarkı söylüyorum!' "
        ];
        return jokes[Math.floor(Math.random() * jokes.length)];
    }

   
    if (lowerCaseInput.includes("hava nasıl") || lowerCaseInput.includes("hava durumu")) {
        const weatherResponses = [
            "Maalesef, hava durumu verilerine şu anda erişimim yok, ama dışarıya bakarak öğrenebilirsin! 🌞☁️",
            "Bugün hava güzel, dışarı çıkıp biraz yürüyüş yapabilirsin! 🌤️",
            "Bakalım dışarıda yağmur yağıyor mu? Benim pencereyi göremiyorum! "
        ];
        return weatherResponses[Math.floor(Math.random() * weatherResponses.length)];
    }

    
    if (lowerCaseInput.includes("hayatın anlamı") || lowerCaseInput.includes("ne yapmalıyım") || lowerCaseInput.includes("amaç nedir")) {
        return "Hayatın anlamı kişisel bir yolculuktur. Kimi insanlar gezmeyi sever, kimisi yeni şeyler öğrenir. Senin için hayatın anlamı nedir? 🌱";
    }

    
    return "Üzgünüm, bu konuda bir şey bilmiyorum ama başka bir konuda yardımcı olabilirim!";
}


function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput === "") return;

   
    const chatBox = document.getElementById('chatbox');
    chatBox.innerHTML += `<div class="message user-message"><strong>Sen:</strong> ${userInput}</div>`;

    
    const botResponse = getBotResponse(userInput);
    chatBox.innerHTML += `<div class="message bot-message"><strong>Bot:</strong> ${botResponse}</div>`;

   
    document.getElementById('userInput').value = "";
    chatBox.scrollTop = chatBox.scrollHeight; 
}


document.getElementById('userInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); 
        sendMessage(); 
    }
});

// Bu Program " Gexnys " tarafından yazılmıştır.
// Açık kaynak kodludur.
// İletişim için " developergokhan@proton.me " adresine mail gönderebilirsiniz.

// ...
