# Linux güvenli yapılandırma

Bu kontrol listesi genel bir başlangıç noktasıdır; dağıtıma ve iş gereksinimlerine göre uyarlayın. Önce mevcut yapılandırmayı yedekleyin, değişiklikleri test edin ve geri alma yöntemi hazırlayın.

## Kontrol listesi

- Sistemi ve paketleri desteklenen güvenlik güncellemeleriyle güncel tutun.
- Gereksiz servis ve yazılımları kaldırın veya devre dışı bırakın.
- Her kullanıcıya ayrı hesap verin; yönetici yetkisini sınırlayın ve düzenli gözden geçirin.
- SSH gerekiyorsa anahtar tabanlı kimlik doğrulamayı tercih edin; root ile doğrudan oturumu kapatmayı değerlendirin.
- SSH yapılandırmasını değiştirmeden önce alternatif konsol erişimi sağlayın ve yeni oturumla test etmeden mevcut oturumu kapatmayın. Hatalı ayar uzaktan erişimi kesebilir.
- Dosya izinlerini ve sahiplikleri asgari gerekli düzeyde tutun.
- Güvenlik günlüğü, zaman eşitleme ve yedekleme durumunu doğrulayın.
- Dağıtımın sağladığı AppArmor veya SELinux gibi zorunlu erişim denetimlerini etkin ve güncel tutun.

## Değişiklik yönetimi

1. Mevcut durumu ve etkilenecek hizmetleri kaydedin.
2. Yapılandırmayı yedekleyin.
3. Tek seferde küçük, geri alınabilir değişiklikler yapın.
4. Yapılandırma doğrulaması ve işlev testleri uygulayın.
5. Sonucu ve geri alma adımlarını kayda geçirin.

Bu depo ana makinede otomatik hardening çalıştırmaz; ayarları körlemesine kopyalayıp uygulamayın.
