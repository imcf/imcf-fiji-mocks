# Changelog 🧾 for `imcf-fiji-mocks`

## 0.5.0

Added mocks:

- `ch.epfl.biop`

## 0.4.0

Added mocks:

- `java.lang.Long`
- `fr.igred.omero`

## 0.3.0

Added mocks:

- `fiji.plugin.trackmate` (quite a bunch)
- `java.lang.Double`

## 0.2.1

Some more mocks:

- `loci.formats.MetadataTools`
- `ij.plugin.Concatenator`
- `ij.process.StackStatistics`

## 0.2.0

Provide an actual `ij.IJ` class having a `run()` method that will issue a log
message with the parameters handed over, to allow for pytest and caplog setups
to (pseudo) test code that issues the famous `IJ.run()` calls.

## 0.1.1

Allow the package to be built on / for Python 2.7 - no functional modifications.
