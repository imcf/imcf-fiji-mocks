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

## Using release artifacts from GitHub

To create a virtualenv you may use artifacts attached to a public release on
Github, for example using the `2023-02-22` release:

```fish
set URL_PFX "https://github.com/imcf/imcf-fiji-pdoc-mocks/releases/download/2023-02-22"

pip install --upgrade \
    $URL_PFX/inra-0.1.1-py3-none-any.whl \
    $URL_PFX/java-0.1.0-py3-none-any.whl \
    $URL_PFX/loci-0.1.1-py3-none-any.whl \
    $URL_PFX/ij-0.1.19-py3-none-any.whl \
    $URL_PFX/micrometa-15.2.2-py3-none-any.whl \
    $URL_PFX/sjlogging-0.1.0-py3-none-any.whl \
    pdoc \
    olefile \
    pip
```

[1]: https://imcf.one/apidocs/
[2]: https://pdoc.dev
[3]: https://python-poetry.org
