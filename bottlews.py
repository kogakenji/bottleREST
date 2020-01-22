from bottle import request, response
from bottle import route, run, post
import json
import sys

def skills_assessment(customer):
    ''' Make the skill assessment'''
    # print(customer)
    skill = 'S004'
    has_provider = int(customer['has_provider'])
    postcode = int(customer['postcode'])
    # print('postcode: {}'.format(postcode))
    cover_type = customer['cover_type']
    # print('cover_type: {}'.format(cover_type))
    has_children = int(customer['has_children'])
    # print('has_children: {}'.format(has_children))

    #does not have a provider
    if has_provider != 1:
        skill = 'S001'
    # VIC, NSW or QLD
    if postcode >= 2000 and postcode <=4999:
        #require combined health cover means cover_type is different of combined
        if customer['cover_type'] != 'combined':
            skill = 'S002'
        if customer['marital_status'] != 'single' and has_children == 1:
            skill = 'S001'

    #single parent
    if customer['marital_status'] == 'single' and has_children == 1:
        skill = 'S003'
    return skill

@post('/skill/health')
def skills_handler():
    '''Handles skills requests'''
    
    try:
        # get input data
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError

    except ValueError as err:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return

    response.content_type = 'application/json'
    return json.dumps({'skill': skills_assessment(data)})


run(host='localhost', port=8080, debug=True, reloader=True)