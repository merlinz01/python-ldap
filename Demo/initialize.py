"""
Various examples how to connect to a LDAP host with the new
factory function ldap.initialize() introduced in OpenLDAP 2 API.

Assuming you have LDAP servers running on
ldap://localhost:1390 (LDAP with StartTLS)
ldaps://localhost:1391 (LDAP over SSL)
ldapi://%2ftmp%2fopenldap2 (domain socket /tmp/openldap2)
"""

import os
import sys

import ldap

# Switch off processing .ldaprc or ldap.conf
os.environ["LDAPNOINIT"] = "1"

# Set debugging level
# ldap.set_option(ldap.OPT_DEBUG_LEVEL,255)
ldapmodule_trace_level = 1
ldapmodule_trace_file = sys.stderr

ldap._trace_level = ldapmodule_trace_level

# Complete path name of the file containing all trusted CA certs
CACERTFILE = "/etc/ssl/ca-bundle.pem"

print("""##################################################################
# LDAPv3 connection with StartTLS ext. op.
##################################################################
""")

# Create LDAPObject instance
ldap_conn = ldap.initialize(
    "ldap://localhost:1390",
    trace_level=ldapmodule_trace_level,
    trace_file=ldapmodule_trace_file,
)

# Set LDAP protocol version used
ldap_conn.protocol_version = ldap.VERSION3

# Force cert validation
ldap_conn.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_DEMAND)
# Set path name of file containing all trusted CA certificates
ldap_conn.set_option(ldap.OPT_X_TLS_CACERTFILE, CACERTFILE)
# Force libldap to create a new SSL context (must be last TLS option!)
ldap_conn.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

# Now try StartTLS extended operation
ldap_conn.start_tls_s()

print("***ldap.OPT_X_TLS_VERSION", ldap_conn.get_option(ldap.OPT_X_TLS_VERSION))
print("***ldap.OPT_X_TLS_CIPHER", ldap_conn.get_option(ldap.OPT_X_TLS_CIPHER))

# Try an explicit anon bind to provoke failure
ldap_conn.simple_bind_s("", "")

# Close connection
ldap_conn.unbind_s()

print("""##################################################################
# LDAPv3 connection over SSL
##################################################################
""")

# Create LDAPObject instance
ldap_conn = ldap.initialize(
    "ldaps://localhost:1391",
    trace_level=ldapmodule_trace_level,
    trace_file=ldapmodule_trace_file,
)

# Set LDAP protocol version used
ldap_conn.protocol_version = ldap.VERSION3

# Force cert validation
ldap_conn.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_DEMAND)
# Set path name of file containing all trusted CA certificates
ldap_conn.set_option(ldap.OPT_X_TLS_CACERTFILE, CACERTFILE)
# Force libldap to create a new SSL context (must be last TLS option!)
ldap_conn.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

# Try an explicit anon bind to provoke failure
ldap_conn.simple_bind_s("", "")

print("***ldap.OPT_X_TLS_VERSION", ldap_conn.get_option(ldap.OPT_X_TLS_VERSION))
print("***ldap.OPT_X_TLS_CIPHER", ldap_conn.get_option(ldap.OPT_X_TLS_CIPHER))

# Close connection
ldap_conn.unbind_s()

print("""##################################################################
# LDAPv3 connection over Unix domain socket
##################################################################
""")

# Create LDAPObject instance
ldap_conn = ldap.initialize(
    "ldapi://%2ftmp%2fopenldap-socket",
    trace_level=ldapmodule_trace_level,
    trace_file=ldapmodule_trace_file,
)
# Set LDAP protocol version used
ldap_conn.protocol_version = ldap.VERSION3
# Try an explicit anon bind to provoke failure
ldap_conn.simple_bind_s("", "")
# Close connection
ldap_conn.unbind_s()
