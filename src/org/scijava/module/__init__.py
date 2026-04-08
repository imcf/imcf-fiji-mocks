"""Mocks for the "org.scijava.module" module."""


class ModuleItem:
    """Mock for the "org.scijava.module.ModuleItem" interface."""

    def __init__(self, input_name):
        """ModuleItem constructor.

        Parameters
        ----------
        input_name : str
            FIXME: describe (see the ScriptModule class)
        """
        self.input_name = input_name

    def getName(self):
        """Getter method for the "input_name" attribute.

        Returns
        -------
        str
        """
        return self.input_name
