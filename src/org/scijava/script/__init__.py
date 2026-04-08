"""Mocks for the "org.scijava.script" module."""

from ..module import ModuleItem


class ScriptInfo:
    """Mock for the "org.scijava.script.ScriptInfo" class."""

    def __init__(self, input_names):
        """ScriptInfo constructor.

        Parameters
        ----------
        input_names : list(str)
            FIXME: describe (see the ScriptModule class)
        """
        self.input_names = [ModuleItem(x) for x in input_names]

    def inputs(self):
        """Get the list of input-objects.

        Returns
        -------
        list(ModuleItem)
        """
        return self.input_names


class ScriptModule:
    """Mock for the "org.scijava.script.ScriptModule" class."""

    def __init__(self, input_names, inputs):
        """ScriptModule constructor.

        Parameters
        ----------
        input_names : list(str)
            The list of input names. FIXME: explain better.
        inputs : dict
            A dict having the `input_names` as keys. Values are representing the
            content of the respective script parameter.
        """
        self.info = ScriptInfo(input_names)
        self.inputs = inputs

    def getInfo(self):
        """Getter method for the "info" attribute.

        Returns
        -------
        ScriptInfo
        """
        return self.info

    def getInputs(self):
        """Getter method for the "inputs" attribute.

        Returns
        -------
        dict
        """
        return self.inputs
