install:
	uv sync
	

brain-games:
    uv add prompt
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl.
	

