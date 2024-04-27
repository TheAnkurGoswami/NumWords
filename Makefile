help:
	@echo "The following make targets are available:"
	@echo "lint-all	run all lint steps"
	@echo "next-version get next version"
	@echo "publish-pypi	publish the library on pypi"

ENV ?= venv
VERSION=`echo "from NumWords import __version__;import sys;out = sys.stdout;out.write(__version__);out.flush();" | python3 2>/dev/null`

next-version:
	chmod +x version.sh
	./version.sh

lint-all: 
	isort .
	black .

publish-pypi:
	rm -r dist build numwords.egg-info || echo "no files to delete"
	python3 -m pip install -U setuptools twine wheel
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/numwords-$(VERSION)-py3-none-any.whl dist/numwords-$(VERSION).tar.gz
	git tag "v$(VERSION)"
	git push origin "v$(VERSION)"
	@echo "succesfully deployed $(VERSION)"
