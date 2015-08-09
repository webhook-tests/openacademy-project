import functools
import xmlrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
model = 'openacademy.session'
domain = []
method_name = 'search_read'
sessions = call(model, method_name, domain, ['name', 'seats', 'taken_seats'])
print "sessions", sessions

for session in sessions:
    print "Session %s (%s seats), taken seats %d" % (session['name'],
                                                     session['seats'],
                                                     session['taken_seats'])

method_name = 'create'
# 3. Create a new session
session_id = call(model, method_name, {'name': 'Session from ws',
                                       'course_id': 2})
print "new session id", session_id
