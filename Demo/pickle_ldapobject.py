import os
import pickle

import ldap
import ldap.ldapobject

temp_file_name = os.path.join(
    os.environ.get("TMP", "/tmp"), f"pickle_ldap-{os.getpid()}"
)

l1 = ldap.ldapobject.ReconnectLDAPObject("ldap://localhost:1390", trace_level=1)
l1.protocol_version = 3
l1.search_s("", ldap.SCOPE_BASE, "(objectClass=*)")

with open(temp_file_name, "wb") as f:
    pickle.dump(l1, f)

with open(temp_file_name, "rb") as f:
    l2 = pickle.load(f)
l2.search_s("", ldap.SCOPE_BASE, "(objectClass=*)")
