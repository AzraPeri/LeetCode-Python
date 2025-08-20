LeetCode 1189 - Balloon Kelimesi

📌 Problem
Verilen bir string `text` içinden **"balloon"** kelimesini en fazla kaç kere oluşturabileceğimizi bulmamız isteniyor.  

Her karakteri sadece bir kez kullanabilirsiniz. Döndürülmesi gereken değer, oluşturulabilecek maksimum **"balloon"** sayısıdır.

Örnek 1:

Input: text = "nlaebolko"
Output: 1

Örnek 2:

Input: text = "loonbalxballpoon"
Output: 2

Örnek 3:

Input: text = "leetcode"
Output: 0
 
💡 Çözüm Mantığı
Amaç, verilen string içinden **"balloon"** kelimesini kaç kere oluşturabileceğimizi bulmak:  

- "balloon" kelimesindeki harfler: `b, a, l, l, o, o, n`  
- `l` ve `o` harfleri **iki kere** gerekir.  
- Metindeki tüm harflerin sayısını sayarız.  
- Her harf için metindeki sayıyı ihtiyaç duyulan sayıya böleriz.  
- Bu değerlerin minimumu, oluşturulabilecek maksimum **"balloon"** sayısını verir.


⏱️ Zaman ve Alan Karmaşıklığı
Zaman: O(n) → string tek geçişte sayılıyor
Alan: O(1) → Counter sabit bir sözlük boyutunda

🔑 Notlar

* Eğer metin boş ise, oluşturulacak balloon sayısı 0 olur.
* Minimum sayıyı almak, tüm gerekli harflerin yeterli olup olmadığını garanti eder.
