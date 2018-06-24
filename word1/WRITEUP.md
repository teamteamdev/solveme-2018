# Word: Reader: Write-up

**Reader** | [Invisible](../word2/WRITEUP.md) | [Meta](../word3/WRITEUP.md) | [Figure](../word4/WRITEUP.md) | [С чем поиграть](../word5/WRITEUP.md) | [Template](../word6/WRITEUP.md) | [Corrupt](../word7/WRITEUP.md)

Открываем файл, видим приветствие и много пустых страниц. Но пустые ли они? Листаем и внимательно смотрим.

На 60-й странице послание: `synt1_uryybpnrfne`.

Похоже на шифр. Но на какой же? Переберем варианты и поймем, что это всего лишь [шифр Цезаря](https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F). 

Воспользуемся [готовой утилитой](https://www.dcode.fr/caesar-cipher) и получим флаг.

Флаг: **flag1_hellocaesar**
