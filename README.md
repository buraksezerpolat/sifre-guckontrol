Şifre Güç Kontrol Uygulaması
_(Scroll down for English)

Bu proje kullanıcıların şifrelerinin güvenliğini değerlendirmek için geliştirilmiş bir masasüstü uygulamasadır.
Python programlama dili ve Tkinter kütüphanesi kullanılarak oluşturulmuştur.

Özellikler:

-Şifre gücünü analiz eder (zayıf, orta, güçlü)
-Uzunluk, büyük harf, küçük harf, sayı ve özel karakter kriterlerine göre değerlendirme yapar. 
-Şifrelerin 'SHA-256 ile hash'lenmiş hali ve güvenlik için rastgele 'salt' değeri ile log kaydı tutar. 
-Log kayıtlarını gösteren scroll destekli arayüze sahiptir.

Kulllanılan Dil ve Kütüphaneler:

-Python
-Tkniter
-Regex (re modülü)
-Hashlib
-Datetime

Nasıl Kullanılır:

1. Projeyi ZIP olarak indirin.
2. sifreguckontrol.py dosyasını çalıştırın.
3. Gücünü merak ettiğiniz bir şifre girin ve "Şireyi Kontrol Et" butonuna tıklayın. 
4. Dilerseniz logları görmek için "Logları Göster" butonuna tıklayın.

Log Kayıtları

Uygulama 'sifre_log.txt' adında bir dosyada şifrelerin has değerlerini ve analiz sonuçlarını saklar.

Geliştirici Notu:

Bu proje eğitim amaçlıdır ve kullanıcı dostu bir arayüzle şifre güvenliği konusunda temel bir analiz sunar.
Gerçek şifre güvenliği sistemlerinde ek güvenlik önlemleri gereklidir.

-----------------------------------------------------------------------------------------------------------
Password Strength Check Application

This project is a desktop application devoloped to evaluate security of users' passwords
It is built using Python programming language and the Tkinter Library

Features: 

-Analyzes password strength(zayıf = weak, orta = medium, güçlü = strong)
-Evuluates based on criteria such as lenght, uppercase, lowercase, digit, and special character
-Stores log data inculuding the password's SHA-256 hash and randomly generated salt for security 
-Interface with scrollable area to view log records 

Technologies and Libraries Used:

-Python
-Tkinter
-Regex(re module)
-Hashlib
-Datetime

How to Use:
1. Download the project as a ZIP file
2. Run the sifreguckontrol.py file
3. Enter a password you'd like to evaluate and click the "Şifreyi Kontrol Et" button.
4. To view logs, click the "Logları Göster" button

Log Records:
The applications saves hashed passwords and analysis results in a file sifre_log.txt

Devoloper Note:
This project is for a educational purposes and provides a basic analysis of password strength with a user
friendly interface.
Real-world password security systems require additional security measures.


