# Login va rollar (US-07, issue #6)

Sprint 1 · branch: `feature/login`

## Maqsad
Foydalanuvchi email va parol bilan tizimga kiradi va o'z roliga mos sahifaga yo'naltiriladi.

## Rollar va bosh sahifalar
| Rol | Bosh sahifa |
|---|---|
| Administrator | Foydalanuvchilar va rollar |
| Dekanat xodimi | Hisobotlar |
| O'qituvchi | Baholar jurnali |
| Kurator | Guruh davomati |
| Talaba | Mening baholarim |

## Acceptance criteria
- [ ] Email noyob bo'lishi tekshiriladi, takror email rad etiladi
- [ ] 5 roldan biri tanlanadi
- [ ] Rolga mos bo'lmagan sahifaga kirishda 403 «Ruxsat yo'q» xabari chiqadi
- [ ] Noto'g'ri parol 5 marta kiritilsa, 5 daqiqaga bloklanadi
