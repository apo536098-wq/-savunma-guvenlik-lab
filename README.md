# Savunma Güvenlik Laboratuvarı

Etik ve savunma odaklı siber güvenlik öğrenimi için Türkçe kaynaklar ve güvenli, yerel alıştırmalar. Amaç sistemleri korumayı, günlükleri anlamayı ve olaylara planlı yanıt vermeyi öğrenmektir.

> **Kullanım sınırı:** Örnekleri yalnızca size ait veya açıkça yetkilendirildiğiniz sistemlerde çalıştırın. Bu depodaki alıştırmalar yerel ve kontrollü kullanım için hazırlanmıştır; gerçek sistemlerde değişiklik yapmadan önce yedek alın ve etkilerini değerlendirin.

## Öğrenme başlıkları

- Linux sistemlerini güvenli yapılandırma ve en az ayrıcalık
- Güvenlik duvarı ilkeleri ve ağ yüzeyini azaltma
- Günlük (log) toplama, inceleme ve basit olay tespiti
- İzleme, uyarı ve temel ölçümleme
- Olay müdahalesi, kayıt tutma ve iyileştirme

## Hızlı başlangıç

Python 3 ile örnek olay günlüklerini üretip analiz edin:

```bash
python3 scripts/generate-sample-logs.py
python3 scripts/analyze-logs.py data/sample-auth.log
```

Komutlar yalnızca depodaki `data/` klasörüne örnek dosya yazar; sistem günlüklerini değiştirmez ve ağa bağlanmaz.

İsteğe bağlı, yalnızca yerel makineden erişilen web laboratuvarı:

```bash
docker compose -f labs/docker-compose.yml up -d
# Tarayıcıda http://127.0.0.1:8080 adresini açın
docker compose -f labs/docker-compose.yml down
```

Docker gerekli değildir. Yayına alınmış veya internete açık sistemlerde kullanmak için tasarlanmamıştır.

## İçindekiler

- [Başlangıç ve tehdit modelleme](docs/01-baslangic.md)
- [Linux güvenli yapılandırma](docs/02-linux-guvenligi.md)
- [Güvenlik duvarı](docs/03-guvenlik-duvari.md)
- [Günlük analizi](docs/04-gunluk-analizi.md)
- [İzleme ve uyarılar](docs/05-izleme.md)
- [Olay müdahalesi](docs/06-olay-mudahalesi.md)
- [Yerel laboratuvar](labs/README.md)

## Güvenli kullanım ilkeleri

1. Kapsamı ve yetkiyi önceden belirleyin.
2. Alıştırmaları izole yerel ortamda ve örnek verilerle yapın.
3. Güvenlik duvarı veya SSH gibi uzaktan erişimi etkileyen ayarları uygulamadan önce konsol erişimi ve geri dönüş planı sağlayın.
4. Parola, erişim anahtarı, kişisel veri veya gerçek günlükleri depoya yüklemeyin.
5. Üçüncü taraf sistemlerde tarama, test veya değişiklik yapmayın; yazılı izin ve açık kapsam olmadan işlem yürütmeyin.

## Katkı

Hata düzeltmeleri ve savunma odaklı dokümantasyon katkıları memnuniyetle karşılanır. Katkılarda gizli bilgi, gerçek kişisel veri veya yetkisiz hedeflere yönelik talimat bulunmamalıdır.

## Lisans

MIT. Ayrıntılar için [LICENSE](../LICENSE) dosyasına bakın.
