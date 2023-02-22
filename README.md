# Mocks for having `pdoc` generate Fiji Python packages API docs

This repo contains mocks that can be used to build fake (thin) `pip install`able
Python packages that will prevent [pdoc](https://pdoc.dev) from failing due to
missing imports when building the abstract syntax tree.
