# Python mocks 🧌 package for `Fiji` related code

Initially created for enabling [pdoc][2] to generate [IMCF Fiji Python packages
API docs][1]. Now also used to run [pytest][4] on e.g. the [python-imcflibs][5]
package.

The goal of this project is to provide mocks that can be used to build a fake
(thin) `pip install`able Python package that will allow tools like *pdoc* or
*pytest* to build up the AST (abstract syntax tree) by using the mocked objects
while performing the imports.

## 🚫 WARNING 🚫

This project and its packages do **not** contain any functional code that is
useful in situations other than the ones described above!

## Building artifacts

You'll need [poetry][3] installed locally, then using `fish` run:

```fish
rm -r dist/
poetry build -vv
```

## Installing / Creating a venv

To create a virtualenv for e.g. running `pdoc`, you can now simply use the
packages from [PyPI][6]:

```fish
python -m venv venv
venv/bin/pip install --upgrade \
    imcf-fiji-mocks \
    "imcflibs>=1.5.0a1" \
    python-micrometa \
    pdoc
```

[1]: https://imcf.one/apidocs/
[2]: https://pdoc.dev
[3]: https://python-poetry.org
[4]: http://pytest.org/
[5]: https://github.com/imcf/python-imcflibs/
[6]: https://pypi.org/
