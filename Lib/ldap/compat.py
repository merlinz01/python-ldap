"""Compatibility wrappers for Py2/Py3."""

import warnings
from collections import UserDict

warnings.warn(
    "The ldap.compat module is deprecated and will be removed in the future",
    DeprecationWarning,
    stacklevel=2,
)


IterableUserDict = UserDict


def reraise(exc_type, exc_value, exc_traceback):
    """Re-raise an exception given information from sys.exc_info()

    Note that unlike six.reraise, this does not support replacing the
    traceback. All arguments must come from a single sys.exc_info() call.
    """
    # In Python 3, all exception info is contained in one object.
    raise exc_value
