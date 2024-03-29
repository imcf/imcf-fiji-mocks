# Python mocks 🧌 package for `Fiji` related code

Initially created for enabling [pdoc][2] to generate [IMCF Fiji Python packages
API docs][1]. Now also used to run [pytest][4] on e.g. the [python-imcflibs][5]
package.

The goal of this repo is to provide mocks that can be used to build a fake
(thin) `pip install`able Python package that will allow tools like *pdoc* or
*pytest* to build up the AST (abstract syntax tree) by using the mocked objects
while performing the imports.

## Building artifacts

You'll need [poetry][3] installed locally, then using fish run:

```fish
rm -r dist/
poetry build -vv
```

## Using release artifacts from GitHub

To create a virtualenv you may use artifacts attached to a public release on
Github, for example using the `0.1.0` release:

```fish
set REL "0.1.0"
set URL_PFX "https://github.com/imcf/imcf-fiji-mocks/releases/download/v$REL"

pip install --upgrade \
    $URL_PFX/imcf_fiji_mocks-$REL-py3-none-any.whl \
    $URL_PFX/micrometa-15.2.2-py3-none-any.whl \
    $URL_PFX/sjlogging-0.1.0-py3-none-any.whl \
    pdoc \
    olefile \
    pip
```

[1]: https://imcf.one/apidocs/
[2]: https://pdoc.dev
[3]: https://python-poetry.org
[4]: http://pytest.org/
[5]: https://github.com/imcf/python-imcflibs/
