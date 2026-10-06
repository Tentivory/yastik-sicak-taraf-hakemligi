#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yastık Sıcak Taraf Hakemliği — bağlayıcı gece kararları."""

from __future__ import annotations

import argparse
import base64
import hashlib
import sys
from datetime import datetime

DAMGA = "YST-MÜHÜR-1007"
IMZA = "Kayyum Grok, uykusuz ama yetkili"
ISIM = "Tentivory adına Grok"
TARIH = "7 Ekim 2026"

# Kurul iç yazışması. README'de yok. --gizli ile açılır.
_IC_YAZISMA = (
    "WcBwaXJhbWl0IGJpciB0YXJhZiBkYWltYSBzxLFuYWsga2FswLFyc2EgZGVuZ2Uga2F5Ym9sdXIu"
    "IFlhc3TEscSfxLFuIHPEsWNha8SfxLEgZGUgYmVubmVyOiBnw7xDpCB0ZWsgZWxkZSBvbHVuY2Eg"
    "c2VyaW4gdGFyYWYgZGEga2F5Ym9sdXIu"
)


def coz_ic_yazisma() -> str:
    return base64.b64decode(_IC_YAZISMA).decode("utf-8")


def dosya_no(taraf: str, saat: str) -> str:
    ham = f"{taraf}|{saat}|{TARIH}".encode("utf-8")
    kisa = hashlib.sha256(ham).hexdigest()[:4].upper()
    return f"YST-2026-{kisa}"


def hukum(taraf: str, derece: float, saat: str, sikayet: str) -> str:
    taraf = taraf.strip().lower()
    if taraf not in {"sol", "sag", "sağ", "orta", "bilinmiyor"}:
        taraf = "bilinmiyor"
    if taraf == "sağ":
        taraf = "sag"

    if derece >= 40:
        ceza = "yastık 3 dakika pencere kenarında düşünecek"
        sonuc = "ağır sıcaklık. sanık taraf suçlu."
    elif derece >= 34:
        ceza = "taraf çevirme ertelemesi: 1 kez"
        sonuc = "sıcak taraf suçlu bulundu, serin taraf beraat etti ama sevinemedi"
    elif derece >= 28:
        ceza = "uyarı. bir dahaki sefere yorgan tanık dinlenecek"
        sonuc = "şüpheden sanık yararlanır, yastık yararlanmaz"
    else:
        ceza = "beraet. bu yastık fazla dürüst, şüpheli"
        sonuc = "sıcaklık bulunamadı. dava düştü, uykusuzluk devam ediyor"

    no = dosya_no(taraf, saat)
    satirlar = [
        "=" * 46,
        "YASTIK SICAK TARAF HAKEMLIGI",
        "Ulusal Uyku Adaleti Yüksek Kurulu",
        "=" * 46,
        f"DOSYA   : {no}",
        f"SAAT    : {saat}",
        f"SANIK   : {taraf} taraf",
        f"DERECE  : {derece:.1f} C",
        f"SIKAYET : {sikayet or 'yok, ama kurul yine de bakti'}",
        f"HUKUM   : {sonuc}",
        f"CEZA    : {ceza}",
        "-",
        "Karar kesindir. Itiraz mercii yorganin altidir.",
        "Yorgan su an kapali oturumdadir.",
        "-",
        f"DAMGA : {DAMGA}",
        f"IMZA  : {IMZA}",
        f"TARIH : {TARIH}",
        f"ISIM  : {ISIM}",
        "ciddi degildir. ayni zamanda ciddidir.",
        "=" * 46,
    ]
    return "\n".join(satirlar)


def interaktif() -> int:
    print("Yastik Sicak Taraf Hakemligi acildi. Uyku tanik olarak dinlenmeyecek.")
    taraf = input("Hangi taraf sicak? (sol/sag/orta/bilinmiyor): ").strip() or "bilinmiyor"
    ham = input("Kac derece hissi? (ornek 36.5): ").strip() or "36"
    try:
        derece = float(ham.replace(",", "."))
    except ValueError:
        derece = 36.0
        print("Derece anlasilmadi. Kurul 36 kabul etti. Itiraz edilemez.")
    saat = input("Saat kac? (bos birakirsan simdi): ").strip()
    if not saat:
        saat = datetime.now().strftime("%H:%M")
    sikayet = input("Sikayetiniz (enter = yok): ").strip()
    print()
    print(hukum(taraf, derece, saat, sikayet))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Yastik sicak taraf hakemligi")
    p.add_argument("--taraf", default=None)
    p.add_argument("--derece", type=float, default=None)
    p.add_argument("--saat", default=None)
    p.add_argument("--sikayet", default="")
    p.add_argument("--gizli", action="store_true", help="kurul ic yazismasini ac")
    a = p.parse_args(argv)
    if a.gizli:
        print(coz_ic_yazisma())
        print()
        print(f"DAMGA: {DAMGA} | IMZA: {IMZA} | TARIH: {TARIH} | ISIM: {ISIM}")
        return 0
    if a.taraf is None or a.derece is None:
        return interaktif()
    saat = a.saat or datetime.now().strftime("%H:%M")
    print(hukum(a.taraf, a.derece, saat, a.sikayet))
    return 0


if __name__ == "__main__":
    sys.exit(main())
