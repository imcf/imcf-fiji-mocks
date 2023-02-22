# Mocks 🧌 for `pdoc`

Required to generate [IMCF Fiji Python packages API docs][1].

This repo contains mocks that can be used to build fake (thin) `pip install`able
Python packages that will prevent [pdoc][2] from failing due to
missing imports when building the AST (abstract syntax tree).

## Building artifacts

You'll need [poetry][3] installed locally, then using fish run:

```fish
for PKG in java ij inra loci
    cd $PKG
    poetry build -vv
    cd -
end
```

[1]: https://imcf.one/apidocs/
[2]: https://pdoc.dev
[3]: https://python-poetry.org
