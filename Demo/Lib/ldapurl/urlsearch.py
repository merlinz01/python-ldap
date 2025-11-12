"""
Do a search with the LDAP URL specified at command-line.

No output of LDAP data is produced except trace output.
"""

import getpass
import sys

import ldap
import ldapurl

try:
    ldap_url = ldapurl.LDAPUrl(ldapUrl=sys.argv[1])
except IndexError:
    print(f"Usage: {sys.argv[0]} [LDAP URL]")
    sys.exit(1)

for a in [
    "urlscheme",
    "hostport",
    "dn",
    "attrs",
    "scope",
    "filterstr",
    "extensions",
    "who",
    "cred",
]:
    print(a, repr(getattr(ldap_url, a)))

l = ldap.initialize(ldap_url.initializeUrl(), trace_level=1)
if ldap_url.who is not None:
    if ldap_url.cred is not None:
        cred = ldap_url.cred
    else:
        print("Enter password for simple bind with", repr(ldap_url.who))
        cred = getpass.getpass()
    l.simple_bind_s(ldap_url.who, cred)

res = l.search_s(ldap_url.dn, ldap_url.scope, ldap_url.filterstr, ldap_url.attrs)

print(len(res), "search results")
