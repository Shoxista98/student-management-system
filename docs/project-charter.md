# Loyiha xartiyasi — Universitet talabalarini boshqarish tizimi (USMS)

| Parametr | Qiymat |
|---|---|
| Loyiha nomi | Universitet talabalarini boshqarish tizimi (USMS) |
| Loyiha kodi | USMS-2026 |
| Mavzu | 6-mavzu, «Loyihalarni boshqarish» fani |
| Ijrochi | Kozibayeva Shoxista Alisher qizi, Masofaviy KIDT-236 |
| Loyiha rahbari | Shixnazar Xusainov |
| Platforma | Web ilova |
| Muddat | 23.11.2026 – 28.02.2027 (7 bosqich) |
| Hujjat versiyasi | 1.0 (23.11.2026) |

## 1. Muammo
Talabalar, guruhlar, baholar va davomat qog'oz jurnallar va tarqoq Excel fayllarda yuritiladi. Ma'lumot takrorlanadi, xatolar ko'p, dekanat tezkor hisobot ololmaydi.

## 2. Maqsad
Talabalar, o'quv guruhlari, fanlar, baholar va davomatni yagona web ilovada boshqarish; 7 bosqichda ishlaydigan MVP ni taqdim etish.

## 3. Qamrov (scope)
**Kiradi:** login va rollar (RBAC), fakultet va guruhlar, talabalar bazasi, fanlar va o'qituvchilar, baholar jurnali (JN/ON/YN, GPA), davomat, hisobotlar, audit jurnali.

**Kirmaydi (out of scope):** mobil ilova, onlayn to'lov va kontrakt hisobi, HEMIS integratsiyasi, abituriyentlar qabuli, SMS xabarnomalar.

## 4. Manfaatdor tomonlar
| Tomon | Roli | Manfaati |
|---|---|---|
| Dekanat | Buyurtmachi | Kontingent, o'zlashtirish va davomat nazorati |
| O'qituvchi | Foydalanuvchi | Baho va davomatni tez kiritish |
| Talaba | Foydalanuvchi | O'z baholari va davomatini ko'rish |
| Kurator | Foydalanuvchi | Guruh davomatini kuzatish |
| Administrator | Foydalanuvchi | Hisoblar va ruxsatlarni boshqarish |
| Loyiha rahbari | Qabul qiluvchi | Talablarga muvofiqlik va sifat |

## 5. Bosqichlar (milestone)
| № | Bosqich | Muddat | Natija |
|---|---|---|---|
| 1 | Arxitektura va foydalanuvchilar | 23.11–06.12.2026 | Login, rollar, ruxsatlar |
| 2 | Fakultetlar va guruhlar | 07.12–20.12.2026 | Guruhlar katalogi |
| 3 | Talabalar bazasi | 21.12.2026–03.01.2027 | Talaba profili va holati |
| 4 | Fanlar va o'quv yuklamasi | 04.01–17.01.2027 | Fanlar, kreditlar |
| 5 | Baholash tizimi | 18.01–31.01.2027 | Baholar jurnali, GPA |
| 6 | Davomat va hisobotlar | 01.02–14.02.2027 | Davomat, hisobotlar |
| 7 | Dashboard, test va deploy | 15.02–28.02.2027 | Yagona tizim, GitHub Pages |

## 6. Muvaffaqiyat mezonlari (KPI)
1. 5 ta rol bilan tizimga kirish va ruxsatlar to'g'ri ishlaydi.
2. Bitta guruh (25 talaba) uchun baholarni kiritish 5 daqiqadan oshmaydi.
3. GPA va qoldirilgan soatlar qo'lda hisoblangan natija bilan 100% mos keladi.
4. Har bir baho o'zgarishi audit jurnalida qayd etiladi.

## 7. Xatarlar
| Xatar | Ehtimoli | Ta'siri | Chora |
|---|---|---|---|
| Talablarning o'zgarishi | O'rta | Yuqori | Har bosqichda TT ni tasdiqlash |
| Muddatning qisqarishi | Yuqori | O'rta | MVP prioriteti, haftalik nazorat |
| Baholarning noto'g'ri kiritilishi | O'rta | Yuqori | Cheklovlar (0–100), audit jurnali |
| Shaxsiy ma'lumotlar sizib chiqishi | Past | Yuqori | RBAC, parol xeshi, HTTPS |

## 8. Cheklovlar va taxminlar
- Loyiha bitta talaba tomonidan bajariladi; byudjet shartli.
- Birinchi versiya bitta fakultet ma'lumotlari bilan ishlaydi.
- Foydalanuvchilarda zamonaviy brauzer va internet mavjud.

## 9. Vazifalar (GitHub Issues)
- #1 Login sahifasi va rollar
- #2 Talabalar ro'yxati va qidiruv
- #3 Baholar jurnali va GPA hisobi
- #4 Davomat jurnali
- #5 Hisobotlar va CSV eksport

## 10. Natijalar
README, loyiha xartiyasi, ishlaydigan repozitoriy va GitHub Pages orqali ochiladigan dastur:
https://shoxista98.github.io/student-management-system/
