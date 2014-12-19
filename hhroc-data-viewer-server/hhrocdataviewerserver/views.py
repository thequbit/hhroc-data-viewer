from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
)

from utils import (

    make_response,

    convert_csv_to_json,
)

import json

@view_config(route_name='upload_csv.json')
def web_uplaod_csv_json(request):
    
    response = {'success': False}
    
    if True:
    #try:
    
        filename = request.POST['csv_file'].filename
        csv_file = request.POST['csv_file'].file
        field_names = request.POST['field_names']
    
        entries = convert_csv_to_json(filename, csv_file, field_names)
     
        response['entries'] = entries
        response['success'] = True
    
    #except:
    #    pass
    
    return make_response(response)
    

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    try:
#        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#    except DBAPIError:
#        return Response(conn_err_msg, content_type='text/plain', status_int=500)
#    return {'one': one, 'project': 'hhroc-data-viewer-server'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_hhroc-data-viewer-server_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

