"""
Demo for using ldap.resiter.ResultProcessor
written by Michael Stroeder <michael@stroeder.com>

See https://www.python-ldap.org for details.
"""

import ldap
import ldap.resiter


class LDAPObject(ldap.ldapobject.LDAPObject, ldap.resiter.ResultProcessor):
    pass


ldap_conn = LDAPObject("ldap://localhost:1390", trace_level=1)
ldap_conn.protocol_version = 3
msgid = ldap_conn.search("dc=stroeder,dc=de", ldap.SCOPE_SUBTREE, "(cn=m*)")

result_iter = ldap_conn.allresults(msgid)
for result_type, result_list, result_msgid, result_serverctrls in result_iter:
    print(result_type, result_list, result_msgid, result_serverctrls)

ldap_conn.unbind_s()
