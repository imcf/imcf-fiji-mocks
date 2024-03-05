from __future__ import print_function

import logging

ImageStack = None
Prefs = None
ImagePlus = None


_log = logging.getLogger()
_log.setLevel(logging.DEBUG)


class IJ(object):

    """Dummy class providing a way to call `IJ.run()`.

    The sole purpose of this is to be used with pytest by simply printing the
    command and its parameters to stdout."""

    @staticmethod
    def run(cmd, params):
        _log.warning("IJ.run(cmd=[%s], params=[%s])", cmd, params)