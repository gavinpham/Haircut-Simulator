#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode. IDK IF THIS IS NEEDED OR NOT
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()                 # parse form data
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('./files/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
	message = 'No file was uploaded'

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)


# print('Content-type: text/html\n')        # hdr plus blank line
# print('<title>Reply Page</title>')        # html reply page
# if not 'user' in form:
#     print('<h1>Who are you?</h1>')
# else:
#     print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

