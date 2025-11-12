# modules without any tests

import os

# Switch off processing .ldaprc or ldap.conf before importing _ldap
os.environ["LDAPNOINIT"] = "1"
