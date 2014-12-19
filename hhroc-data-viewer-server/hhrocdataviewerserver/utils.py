
import csv
import json

import re

import uuid

from pyramid.response import Response

def make_response(resp_dict):

    #print "[DEBUG]"
    #print resp_dict
    #print '\n'

    resp = Response(json.dumps(resp_dict), content_type='application/json', charset='utf8')
    resp.headerlist.append(('Access-Control-Allow-Origin', '*'))

    return resp
    
def convert_csv_to_json(filename, csv_file, field_names):

    json_obj = {}

    if True:
    #try:

        fields = json.loads(field_names)
        
        # reset csv_file
        csv_file.seek(0)
        
        # read first line to get headers
        #headers = header_data.split(',')
        
        
        # configure our reader
        reader = csv.DictReader( csv_file )
        
        entries = []
        
        for row in reader:
            entry = {}
            for field in fields:
                entry[field] = row[field]
            entries.append(entry)
        
       
        
    #except:
    #    pass
        
    return entries