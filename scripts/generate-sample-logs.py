#!/usr/bin/env python3
"""Create harmless, synthetic authentication log lines for local practice."""

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "sample-auth.log"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%b %d %H:%M:%S")
    lines = [
        f"{now} lab-host sshd[1001]: Failed password for invalid user sample from 192.0.2.10 port 2200 ssh2",
        f"{now} lab-host sshd[1002]: Invalid user guest from 198.51.100.15",
        f"{now} lab-host sshd[1003]: Accepted publickey for labuser from 192.0.2.20 port 2200 ssh2",
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Sentetik örnek günlük yazıldı: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
