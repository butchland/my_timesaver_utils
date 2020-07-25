SRC = $(wildcard nbs/*.ipynb)

all: my_timesaver_utils docs

my_timesaver_utils: $(SRC)
	nbdev_build_lib
	touch my_timesaver_utils

docs_serve: docs
	cd docs && bundle exec jekyll serve

butch-run: .FORCE
	docker-compose down --remove-orphans || true;
	docker-compose up butch-jekyll-run
docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

.FORCE:
