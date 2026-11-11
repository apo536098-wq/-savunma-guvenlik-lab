#!/usr/bin/env python3
"""Count a few defensive indicators in a user-supplied local log file."""

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile", type=Path, help="İncelenecek yerel metin günlük dosyası")
    args = parser.parse_args()

    if not args.logfile.is_file():
        parser.error(f"Dosya bulunamadı: {args.logfile}")

    failed = invalid = total = 0
    try:
        with args.logfile.open(encoding="utf-8", errors="replace") as stream:
            for line in stream:
                total += 1
                failed += "Failed password" in line
                invalid += "Invalid user" in line
    except OSError as exc:
        parser.error(f"Dosya okunamadı: {exc}")

    print(f"İncelenen satır: {total}")
    print(f"Başarısız parola kaydı: {failed}")
    print(f"Geçersiz kullanıcı kaydı: {invalid}")
    print("Not: Bu basit örnek bir alarm/olay kararı vermez; bulguları bağlam içinde inceleyin.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
