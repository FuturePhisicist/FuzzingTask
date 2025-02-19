# FuzzingTask

1. ugrep_install.sh
2. Get some text samples:
```shell
python3 get_invalid_text.py
python3 get_valid_ascii.py
python3 get_valid_text.py
```
2. Run 
```shell
	python3 get_some_regexes_1.py
```
3. Run
```shell
	afl-cmin -i some_regexes -o unique_regexes -T all -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts
```
3. !!! run python generators, collect files, get regexes !!!
4. ugrep_fuzz_no_mutator.sh