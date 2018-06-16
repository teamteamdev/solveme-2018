# док йынсапозеБ: Write-up

Так как весь текст в задании задом-наперёд, попробуем [развернуть](http://string-functions.com/reverse.aspx) данную нам строку.
Получаем: `t4iLuAiLuAiLt4CIt4iLg4iLuA...` (очевидно, что это BASE64). 
Кидаем это всё в BASE64 [декодер](https://www.base64decode.org/)... Что-то мы сделали не так.

Значит не нужно ревёрсить строку. Ладно, ещё раз повторяем наши действия.
Ухты, на выходе получили [азбуку Морзе](https://ru.wikipedia.org/wiki/%D0%90%D0%B7%D0%B1%D1%83%D0%BA%D0%B0_%D0%9C%D0%BE%D1%80%D0%B7%D0%B5), неплохо.

Находим какой-либо переводчик, например, [этот](https://morsecode.scphillips.com/translator.html), и пытаемся получить флаг.
Что же у нас получилось? Ничего хорошего. Точно, забыли развернуть.

Попытка №2:
Получаем: `birds are singing flowers are blooming your flag is: easy-reversed-morse`, сдаём. PROFIT!

Флаг: **easy-reversed-morse**
