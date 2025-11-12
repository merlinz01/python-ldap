"""
ldap.schema -  LDAPv3 schema handling

See https://www.python-ldap.org/ for details.
"""

from ldap import __version__
from ldap.schema.models import (
    AttributeType,
    DITContentRule,
    DITStructureRule,
    LDAPSyntax,
    MatchingRule,
    MatchingRuleUse,
    NameForm,
    ObjectClass,
    extract_tokens,
    split_tokens,
)
from ldap.schema.subentry import (
    SCHEMA_ATTR_MAPPING,
    SCHEMA_ATTRS,
    SCHEMA_CLASS_MAPPING,
    SubSchema,
    urlfetch,
)

__all__ = [
    "SCHEMA_ATTRS",
    "SCHEMA_ATTR_MAPPING",
    "SCHEMA_CLASS_MAPPING",
    "AttributeType",
    "DITContentRule",
    "DITStructureRule",
    "LDAPSyntax",
    "MatchingRule",
    "MatchingRuleUse",
    "NameForm",
    "ObjectClass",
    "SubSchema",
    "__version__",
    "extract_tokens",
    "split_tokens",
    "urlfetch",
]
