import os
from datetime import timedelta

DEBUG = os.environ["DEBUG"]
HOST = os.environ["HOST"]
PORT = int(os.environ["PORT"])
SECRET_KEY = os.environ["SECRET_KEY"]
PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(os.environ["SESSION_LIFETIME"]))

LDAP_HOST = os.environ["LDAP_HOST"]
LDAP_BASE_DN = os.environ["LDAP_BASE_DN"]
LDAP_USER_DN = os.environ["LDAP_USER_DN"]
LDAP_USER_RDN_ATTR = os.environ["LDAP_USER_RDN_ATTR"]
LDAP_GROUP_OBJECT_FILTER = os.environ["LDAP_GROUP_OBJECT_FILTER"]
