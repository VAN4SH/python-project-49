install:
	poetry install

brain-games:
	poetry run brain-games

build:
	python3 setup.py sdist bdist_wheel

publish:
	poetry publish --dry-run

package-install:
	pip install .

lint:
	poetry run flake8 brain_games	

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime
