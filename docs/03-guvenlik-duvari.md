# Güvenlik duvarı

Güvenlik duvarı kuralları işletim sistemi, ağ topolojisi ve hizmet gereksinimlerine bağlıdır. Önce izin verilen trafiği belirleyin; mevcut uzaktan yönetim yolunu yanlışlıkla kapatmamaya dikkat edin.

## Güvenli değişiklik yaklaşımı

- Mevcut kuralları ve açık portları kaydedin.
- Yalnızca gerekli hizmetlere erişim verin; mümkünse kaynak ağları sınırlayın.
- Önce test ortamında doğrulayın.
- Uzak bir makinede kural değiştiriyorsanız sağlayıcı konsolu/yerel konsol erişimi ve geri alma planı hazır olsun.
- Uygulamadan sonra beklenen hizmetlerin çalıştığını ve beklenmeyen erişimin kapalı olduğunu doğrulayın.

## Yerel Docker alıştırması

`labs/docker-compose.yml` web örneğini yalnızca `127.0.0.1` adresine bağlar; laboratuvar hizmetini yerel makine dışına açmaz. Başlatmak ve durdurmak için [laboratuvar yönergelerine](../labs/README.md) bakın.

Bu doküman kasıtlı olarak ana makinenizin güvenlik duvarını değiştiren komutlar içermez. Üretim veya uzaktaki sistemlerde değişiklikleri kurumunuzun değişiklik yönetimi sürecine göre yapın.
