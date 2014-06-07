import json
import requests
import networkx as nx

def find_person_attr(d, search_str):
  """ d = the congress person record,
      search_str is the person or attribute you are looking for
  """
  result = []
  for k, v in d.iteritems():
    if isinstance(v, dict):
        result.extend(find_person_attr(v,search_str))
    else:
        v = unicode(v)
        if search_str.lower() in v.lower():
            #print(k,v)
            result.append(k + " : " + v)
  return result

def find_congress_attr(con_artists,search_str):
    """ find congress person by search string"""
    result = {}
    for x , i in zip(con_artists, range(len(con_artists))):
        firstname = x['person']['firstname']
        lastname  = x['person']['lastname']
        attr =  find_person_attr(x,search_str)
        if attr:
            result[firstname + ' ' + lastname] = attr
    return result

def get_all_congress():
    all_congress=[]
    my_str ="http://api.opencongress.org/people?format=json&page="
    for x in range(1,419):
        new_var = json.loads(requests.get(my_str+str(x)).text)
        all_congress.extend(new_var['people'])
    return all_congress

# test
j_kerry_req = requests.get("http://api.opencongress.org/people?last_name=Kerry&format=json")
j_kerry_response = json.loads(j_kerry_req.text)

# examples
all_congress = get_all_congress()
result = find_congress_attr(all_congress, "Napoleon")
