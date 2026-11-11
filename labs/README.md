# Yerel laboratuvar

Bu laboratuvar isteğe bağlı Docker Compose web örneği ve Python ile çalışan sentetik günlük alıştırmalarından oluşur. Harici hedeflere trafik göndermez.

## Gereksinimler

- Günlük alıştırmaları için Python 3
- İsteğe bağlı web örneği için Docker ve Docker Compose

## Sentetik günlük alıştırması

Depo kök dizininden:

```bash
python3 scripts/generate-sample-logs.py
python3 scripts/analyze-logs.py data/sample-auth.log
```

Üretici yalnızca `data/sample-auth.log` dosyasına sentetik satırlar yazar. Üretim günlüklerini veya `/var/log` içeriğini değiştirmez.

## Yerel web örneği

```bash
docker compose -f labs/docker-compose.yml up -d
```

Tarayıcıdan `http://127.0.0.1:8080` adresine gidin. Bitirdiğinizde:

```bash
docker compose -f labs/docker-compose.yml down
```

Port eşlemesi yalnızca loopback arayüzündedir; örneği internete açmayın. İmaj sürümü sabitlenmiştir. Kurumsal/üretim kullanımı için değildir.

## Temizlik

```bash
docker compose -f labs/docker-compose.yml down --volumes --remove-orphans
```

Komut bu Compose projesinin kaynaklarını kaldırır. Örnek günlük dosyasını isterseniz elle `rm data/sample-auth.log` ile silebilirsiniz.
