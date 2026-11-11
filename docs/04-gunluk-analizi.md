# Günlük analizi

Günlükler olayları anlamaya yardım eder; tek başına kesin saldırı kanıtı değildir. Zaman damgası, kaynak, ilgili hizmet ve çevresel bağlamı birlikte değerlendirin.

## Yerel örnek alıştırması

Depodaki sentetik kayıtları üretin ve analiz edin:

```bash
python3 scripts/generate-sample-logs.py
python3 scripts/analyze-logs.py data/sample-auth.log
```

Analiz aracı dosyayı salt okunur biçimde inceler; `Failed password` ve `Invalid user` metinlerini sayar. Yalnızca belirtilen dosyayı okur, ağ bağlantısı kurmaz ve kayıtları değiştirmez.

## İnceleme kontrol listesi

- Saat dilimi ve sistem saatinin doğru olup olmadığını kontrol edin.
- Aynı hesap, kaynak veya hizmet çevresindeki olayları zaman çizelgesinde birleştirin.
- Başarısız ve başarılı oturum açma kayıtlarını birlikte değerlendirin.
- Günlük saklama süresi, erişim izinleri ve bütünlüğünü gözden geçirin.
- Gerçek günlükleri paylaşmadan önce kişisel verileri ve sırları çıkarın.

Örnek IP adresleri dokümantasyon için ayrılmış adres bloklarından seçilmiştir; gerçek sistemlere ait değildir.
