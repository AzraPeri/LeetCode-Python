LeetCode Python

Bu repo, LeetCode problemlerinin Python çözümlerini içerir.
Her problem için:

Problem 1: Balloon
Açıklama (Türkçe)

Bu problemde bize bir string veriliyor ve bizden şunu istiyor:
Verilen metin içinde "balloon" kelimesinden kaç tane oluşturabiliriz?

Örneğin: "nlaebolko" → "balloon" kelimesini 1 kez oluşturabiliriz.

Mantık: "balloon" kelimesinde harfler: b, a, l, l, o, o, n var.

L ve O harfleri iki kez gerekiyor.

Metindeki her harfin sayısını kontrol ederek kaç tane "balloon" oluşturulabileceğini buluyoruz.

Çözüm Mantığı

Metindeki tüm harfleri sayıyoruz (Counter kullanıyoruz).

"balloon" kelimesinde hangi harflerden kaç tane gerektiğini belirliyoruz.

Her harf için metindeki sayıyı, ihtiyaç duyulan sayıya bölüp minimum değeri alıyoruz.

Minimum değer, "balloon" kelimesini kaç kere yapabileceğimizi verir.
