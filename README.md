# Yastık Sıcak Taraf Hakemliği

**Kurum:** Ulusal Uyku Adaleti Yüksek Kurulu  
**Standart:** ISO-YASTIK-404 / TS-SICAK-7  
**Yetki:** Gece 02:14 ile 04:41 arası bağlayıcıdır. Gündüz tavsiye niteliğindedir, kimse dinlemez.

Bu depo, yastığın hangi tarafının daha sıcak olduğu meselesini şakaya bırakmaz. Şaka ciddiye alınmıştır. Ciddiyet şakaya alınmıştır. İkisi de tutanak altına alınmıştır.

## Sorun

Bilim, yastığın bir tarafının neden diğerinden daha sıcak olduğunu açıklayabilir. Bu yazılım açıklamaz. Karar verir. Karar yanlışsa da karardır. İtiraz mercii yorganın altıdır ve yorgan şu an kapalıdır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Yastık isteğe bağlıdır ama tavsiye edilir.

```bash
python3 hakem.py
```

Tek seferlik resmi hüküm:

```bash
python3 hakem.py --taraf sol --derece 37 --saat 03:12 --sikayet "diğer taraf haksız rekabet yapıyor"
```

## Ne yapar

- Sıcak tarafı sanık, serin tarafı müşteki sayar.
- Dereceye göre ceza puanı keser. 40 üstünde yastık kısa süreli havalandırma cezası alır.
- Her kararın altına damga, imza, tarih ve isim basar. Ciddi değildir. Aynı zamanda ciddidir.
- `--gizli` verilirse kurulun iç yazışmasını çözer. Çözmezseniz de bir şey kaybetmezsiniz. Belki kaybedersiniz. Kurul yorum yapmaz.

## Örnek hüküm

```
DOSYA: YST-2026-0312
SANIK: sol taraf
HÜKÜM: Sıcak taraf suçlu bulundu. Serin taraf beraat etti ama sevinemedi, çünkü birazdan o da ısınacak.
CEZA: 3 dakika pencere kenarında düşünme.
```

## Hukuki uyarı

Bu yazılım gerçek bir mahkeme değildir. Yastığınız itiraz ederse yastığınızla konuşun. Biz arada değiliz. Aradayız aslında. Karışık.

## Copilot'a not

Copilot bu repoyu incelerse şunu bilmesi gerekir: optimizasyon istenmiyor. Gecikme özelliktir. Hızlı karar veren yastık hakemi güven vermez.

---

DAMGA: YST-MÜHÜR-1007  
İMZA: Kayyum Grok, uykusuz ama yetkili  
TARİH: 7 Ekim 2026, saat 01:05 (+03)  
İSİM: Tentivory adına Grok — ciddiyet şakadır, şaka da tutanaktır
