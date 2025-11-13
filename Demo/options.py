import ldap

host = "localhost:1390"

print("API info:", ldap.get_option(ldap.OPT_API_INFO))
print("debug level:", ldap.get_option(ldap.OPT_DEBUG_LEVEL))
# print("Setting debug level to 255...")
# ldap.set_option(ldap.OPT_DEBUG_LEVEL,255)
# print("debug level:",ldap.get_option(ldap.OPT_DEBUG_LEVEL))
print("default size limit:", ldap.get_option(ldap.OPT_SIZELIMIT))
print("Setting default size limit to 10...")
ldap.set_option(ldap.OPT_SIZELIMIT, 10)
print("default size limit:", ldap.get_option(ldap.OPT_SIZELIMIT))
print("Creating connection to", host, "...")
ldap_conn = ldap.init(host)
print("size limit:", ldap_conn.get_option(ldap.OPT_SIZELIMIT))
print("Setting connection size limit to 20...")
ldap_conn.set_option(ldap.OPT_SIZELIMIT, 20)
print("size limit:", ldap_conn.get_option(ldap.OPT_SIZELIMIT))
# print("Setting time limit to 60 secs...")
ldap_conn.set_option(ldap.OPT_TIMELIMIT, 60)
# print("time limit:",ldap_conn.get_option(ldap.OPT_TIMELIMIT))
print("Binding...")
ldap_conn.simple_bind_s("", "")
