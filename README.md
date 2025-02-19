# FuzzingTask

1. Follow the steps in `ugrep_install.sh` (It does not work on its own!!!)
2. Get some `text` samples:
```shell
	python3 get_invalid_text.py
	python3 get_valid_ascii.py
	python3 get_valid_text.py
```
Get code_samples:
```shell
	# https://github.com/TheRenegadeCoder/sample-programs/tree/main/archive
	cd ..
	git clone https://github.com/TheRenegadeCoder/sample-programs.git
	cp sample-programs/archive FuzzingTask/input_texts/code_samples
	cd FuzzingTask
```
3. Get `regexes`
```shell
	# https://github.com/SBULeeLab/LinguaFranca-FSE19/tree/master/data/production-regexes
	cd ..
	git clone https://github.com/SBULeeLab/LinguaFranca-FSE19.git
	cp LinguaFranca-FSE19/data/production-regexes/uniq-regexes-8.json FuzzingTask/
	cd FuzzingTask
``` 
```shell
	python3 get_some_regexes_1.py
```
`Minimize` regexes corpus:
```shell
	afl-cmin -i some_regexes -o unique_regexes -T all -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts
```
4. In different terminals, run:
```shell
	bash run_without_mutations_1.sh
	bash run_without_mutations_2.sh
	bash run_without_mutations_3.sh
	bash run_without_mutations_4.sh
```
```shell
	bash run_with_mutations_1.sh
	bash run_with_mutations_2.sh
	bash run_with_mutations_3.sh
	bash run_with_mutations_4.sh
```
