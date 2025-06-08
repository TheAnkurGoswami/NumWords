.PHONY: help lint-all lint test release version-check publish-pypi

help:
	@echo "The following make targets are available:"
	@echo "lint-all	run all lint steps (isort, black)"
	@echo "lint		run ruff linter"
	@echo "test		run unit tests"
	@echo "release	run semantic-release publish"
	@echo "version-check	check current and next version with semantic-release"
	@echo "publish-pypi	publish the library on pypi (Note: versioning now handled by semantic-release)"

ENV ?= venv
# VERSION variable removed - handled by semantic-release

# next-version target removed - superseded by semantic-release

lint-all: 
	isort .
	black .

# New lint target for Ruff
lint:
	@echo "Running linter (ruff)..."
	python -m ruff check .

# Target to run unit tests
test:
	@echo "Running unit tests..."
	python -m unittest discover -s tests -p 'test_*.py'

# Target for semantic-release
release:
	@echo "Running semantic-release publish (version, changelog, tag, build, release)..."
	semantic-release publish

version-check:
	@echo "Checking current version and next version with semantic-release..."
	semantic-release version --print

publish-pypi:
	# This target needs to be updated or used carefully, as VERSION is no longer defined in this Makefile.
	# Semantic-release handles versioning, tagging, and creating GitHub releases.
	# PyPI upload should ideally be part of a CD pipeline triggered by new tags/releases.
	# If running manually, ensure VERSION is set, e.g. VERSION=$$(semantic-release version --print | grep current | awk '{print $$NF}')
	@echo "Manual PyPI publish target. Ensure version is correctly set and artifacts exist."
	@echo "VERSION for build is: $${VERSION_TO_PUBLISH}"
	@echo "If VERSION_TO_PUBLISH is empty, this will likely fail or use a placeholder."
	rm -r dist build numwords.egg-info || echo "no files to delete"
	python3 -m pip install -U setuptools twine wheel
	python3 setup.py sdist bdist_wheel
	# The following line assumes VERSION_TO_PUBLISH is set in the environment
	python3 -m twine upload dist/numwords-$${VERSION_TO_PUBLISH:-0.0.0}-py3-none-any.whl dist/numwords-$${VERSION_TO_PUBLISH:-0.0.0}.tar.gz
	# Git tagging is now handled by semantic-release
	# git tag "v$(VERSION)"
	# git push origin "v$(VERSION)"
	@echo "Successfully attempted to publish version $${VERSION_TO_PUBLISH}"
