"""
ldap.controls.paged - classes for Simple Paged control
(see RFC 2696)

See https://www.python-ldap.org/ for project details.
"""

__all__ = ["SimplePagedResultsControl"]

# Imports from python-ldap 2.4+
from pyasn1_modules.rfc2251 import LDAPString

from ldap.controls import KNOWN_RESPONSE_CONTROLS, RequestControl, ResponseControl
from pyasn1.codec.ber import decoder, encoder

# Imports from pyasn1
from pyasn1.type import namedtype, univ


class PagedResultsControlValue(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType("size", univ.Integer()),
        namedtype.NamedType("cookie", LDAPString()),
    )


class SimplePagedResultsControl(RequestControl, ResponseControl):
    controlType = "1.2.840.113556.1.4.319"

    def __init__(self, criticality=False, size=10, cookie=""):
        self.criticality = criticality
        self.size = size
        self.cookie = cookie or ""

    def encodeControlValue(self):
        pc = PagedResultsControlValue()
        pc.setComponentByName("size", univ.Integer(self.size))
        pc.setComponentByName("cookie", LDAPString(self.cookie))
        return encoder.encode(pc)

    def decodeControlValue(self, encodedControlValue):
        decodedValue, _ = decoder.decode(
            encodedControlValue, asn1Spec=PagedResultsControlValue()
        )
        self.size = int(decodedValue.getComponentByName("size"))
        self.cookie = bytes(decodedValue.getComponentByName("cookie"))


KNOWN_RESPONSE_CONTROLS[SimplePagedResultsControl.controlType] = (
    SimplePagedResultsControl
)
