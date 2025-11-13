import sys

import ldap
import ldapurl
from ldap.ldapobject import ReconnectLDAPObject

ldap_url = ldapurl.LDAPUrl(sys.argv[1])
ldap_url.applyDefaults(
    {"who": "", "cred": "", "filterstr": "(objectClass=*)", "scope": ldap.SCOPE_BASE}
)

ldap.trace_level = 1

ldap_conn = ReconnectLDAPObject(ldap_url.initializeUrl(), trace_level=ldap.trace_level)
ldap_conn.protocol_version = ldap.VERSION3

ldap_conn.simple_bind_s(ldap_url.who, ldap_url.cred)

while 1:
    ldap_conn.search_s(ldap_url.dn, ldap_url.scope, ldap_url.filterstr, ldap_url.attrs)
    sys.stdin.readline()
