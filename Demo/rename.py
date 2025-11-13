from getpass import getpass

import ldap

# Create LDAPObject instance
ldap_conn = ldap.initialize("ldap://localhost:1389", trace_level=1)

print("Password:")
cred = getpass()

try:
    # Set LDAP protocol version used
    ldap_conn.set_option(ldap.OPT_PROTOCOL_VERSION, 3)

    # Try a bind to provoke failure if protocol version is not supported
    ldap_conn.bind_s("cn=root,dc=stroeder,dc=com", cred, ldap.AUTH_SIMPLE)

    print("Using rename_s():")

    ldap_conn.rename_s(
        "uid=fred,ou=Unstructured testing tree,dc=stroeder,dc=com",
        "cn=Fred Feuerstein",
        "dc=stroeder,dc=com",
        0,
    )

    ldap_conn.rename_s(
        "cn=Fred Feuerstein,dc=stroeder,dc=com",
        "uid=fred",
        "ou=Unstructured testing tree,dc=stroeder,dc=com",
        0,
    )

    m = ldap_conn.rename(
        "uid=fred,ou=Unstructured testing tree,dc=stroeder,dc=com",
        "cn=Fred Feuerstein",
        "dc=stroeder,dc=com",
        0,
    )
    r = ldap_conn.result(m, 1)

    m = ldap_conn.rename(
        "cn=Fred Feuerstein,dc=stroeder,dc=com",
        "uid=fred",
        "ou=Unstructured testing tree,dc=stroeder,dc=com",
        0,
    )
    r = ldap_conn.result(m, 1)

finally:
    ldap_conn.unbind_s()
