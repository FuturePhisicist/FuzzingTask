<div dir="ltr" align=center>
    
[**English 🇺🇸**](README.md) / [**Русский 🇷🇺**](README_RU.md)

</div>
<br>

# Пошаговая инструкция

1. **Дерево каталогов**
```shell
fuzzing_test			# =: FT
├── AFLplusplus
├── FuzzingTask			# этот репозиторий
├── LinguaFranca-FSE19
├── sample-programs
└── ugrep
```

2. Установите `AFLplusplus`
```shell
	# https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/INSTALL.md
	git clone https://github.com/AFLplusplus/AFLplusplus.git
	cd AFLplusplus
	make
	# ИЛИ
	make PERFORMANCE=1
```
Создайте **ярлыки**:
```shell
	cd /usr/local/bin/
	sudo ln -s FT/AFLplusplus/afl-clang-fast .
	sudo ln -s FT/AFLplusplus/afl-clang-fast++ .
	sudo ln -s FT/AFLplusplus/afl-cmin .
	sudo ln -s FT/AFLplusplus/afl-fuzz .
	sudo ln -s FT/AFLplusplus/afl-showmap .
	cd FT
```

3. Установите `ugrep` так, чтобы можно было проводить ***фаззинг***
```shell
	git clone https://github.com/Genivia/ugrep.git
	cd ugrep
	CC=afl-clang-fast CXX=afl-clang-fast++ ./build.sh --disable-shared
	# Проверка
	afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds
	# ИЛИ
	AFL_DEBUG=1 afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds
```

4. Сгенерируйте **текст:**
```shell
	python3 get_invalid_text.py
	python3 get_valid_ascii.py
	python3 get_valid_text.py
```
Получите **code_samples:**
```shell
	# https://github.com/TheRenegadeCoder/sample-programs/tree/main/archive
	cd ..
	git clone https://github.com/TheRenegadeCoder/sample-programs.git
	cp sample-programs/archive FuzzingTask/input_texts/code_samples
	cd FuzzingTask
```

5. Получите **регулярные выражения**
```shell
	# https://github.com/SBULeeLab/LinguaFranca-FSE19/tree/master/data/production-regexes
	cd ..
	git clone https://github.com/SBULeeLab/LinguaFranca-FSE19.git
	cp LinguaFranca-FSE19/data/production-regexes/uniq-regexes-8.json FuzzingTask/
	cd FuzzingTask
``` 
```shell
	python3 get_some_regexes_1.py # Будет получено 1000 случайных регулярных выражений
```
**Минимизируйте** корпус регулярных выражений до **111 (!):**
```shell
	afl-cmin -i some_regexes -o unique_regexes -T all -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts
```

6. **Фаззинг!**
```shell
	bash aflplusplus_system_tweak.sh # требуется sudo
```

В разных терминалах (или используя `tmux`) запустите:
```shell
	bash run_without_mutations_1.sh
	bash run_without_mutations_2.sh
	bash run_without_mutations_3.sh
	bash run_without_mutations_4.sh
```
Затем:
```shell
	bash run_with_mutations_1.sh
	bash run_with_mutations_2.sh
	bash run_with_mutations_3.sh
	bash run_with_mutations_4.sh
```
Затем:
```shell
	bash run_custom_mutations_only_1.sh
	bash run_custom_mutations_only_2.sh
	bash run_custom_mutations_only_3.sh
	bash run_custom_mutations_only_4.sh
```

7. Изучите результаты в `final/`!

# **Возможные мутации**

## **1. Инверсия квантификатора (`flip_quantifier.py`)**
### **Что делает:**  
- Обнаруживает квантификаторы регулярных выражений (`*`, `+`, `?`) и:
  - Заменяет их на другой квантификатор.
  - Удаляет их случайным образом.
  - Не делает регулярное выражение недействительным.
  
### **Примеры мутаций:**

| Входные данные | Мутация | Изменения |
|-------|----------|---------|
| `a+` | `a*` | `+` → `*` (Квантификатор изменён) |
| `b?` | `b+` | `?` → `+` (Квантификатор изменён) |
| `c*` | `c`  | - `*` (Квантификатор `*` удалён) |

## **2. Обработка выражений в квадратных скобках (`handle_bracket_expression.py`)**
### **Что делает:**  
- Изменяет выражения в квадратных скобках (`[a-z]`), выполняя:
  - Добавление отрицания (`^`).
  - Замену символов внутри.
  <!-- - Добавление случайного диапазона символов. -->
  - Не создаёт некорректные регулярные выражения

### **Примеры мутаций:**

| Входные данные | Мутация | Изменения |
|--------|-----------|---------|
| `[a-z]` | `[^a-z]` | + `^` (Добавлено отрицание) |
| `[0-9]` | `[1-9]` | `0` → `1` (Изменён символ) |
<!-- | `[aeiou]` | `[a-iu]` | (Вставлен диапазон символов) | -->

## **3. Вставка известных токенов (`insert_known_token.py`)**
### **Что делает:**  
- Случайным образом вставляет специальные символы регулярных выражений (`^`, `$`, `*`, `[`, `]`, `{`, `}`, `|` и др.).
- Добавляет выражения в квадратных (`[]`) и фигурных (`{}`) скобках, а также группировки (`()`).
- ***Старается*** не делать регулярное выражение недействительным.

### **Примеры мутаций:**

| Входные данные | Мутация | Изменения |
|--------|-----------|---------|
| `1234` | `12*4` | + `*` (Добавлен квантификатор `*`) |
| `abc` | `a[xyz]bc` | + `[xyz]` (Добавлено выражение в квадратных скобках) |
| `def` | `de{2,5}f` | + `{2,5}` (Добавлен диапазон повторений) |
| `ghi` | `g(hi)` | + `(`, + `)` (Обёрнуто в круглые скобки) |

## **4. Нарушение синтаксиса регулярного выражения (`invalidate_regex.py`)**
### **Что делает:**  
- Делает регулярное выражение недействительным, выполняя:
  - Вставку случайных специальных символов.
  - Замену корректных специальных символов на другие.
  
### **Примеры мутаций:**

| Входные данные | Мутация | Изменения |
|--------|-----------|---------|
| `abc+` | `abc\\+` | + `\\` (Добавлена некорректная экранизация) |
| `[a-z]` | `[a-z?]` | + `?` (Вставлен недопустимый символ в квадратные скобки) |
| `a{3,}` | `a{3,+}` | + `+` (Добавлен некорректный синтаксис квантификатора) |
| `f[3-9]` | `f[3-9*` | `]` → `*` (Заменён специальный символ) |

## **5. Случайное удаление (`random_deletion.py`)**
### **Что делает:**  
- Случайным образом удаляет до `MAX_REMOVE_CHAR_CNT` подряд идущих символов из регулярного выражения.
- Может удалить важные компоненты, такие как квантификаторы, скобки или символы `|`.
- Может сделать регулярное выражение недействительным.

### **Примеры мутаций:**
| Входные данные | Мутация | Изменения |
|--------|-----------|---------|
| `a+` | `a` | - `+` (Квантификатор удалён) |
| `[^a-z]` | `[^z]` | - `a-` (Диапазон полностью изменён) |
| `(abcdef)` | `(abc` | - `def)` (Группа "расформирована") |
