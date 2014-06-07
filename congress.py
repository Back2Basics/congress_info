
# In[32]:

import json
import requests
import networkx as nx


req = requests.get("http://api.opencongress.org/people?last_name=Kerry&format=json")
jk = json.loads(req.text)
# jk['people'][0]['person']['religion']

# all_congress= json.loads(requests.get("http://api.opencongress.org/people?format=json").text)

# len(all_congress['people'])

# [x['person']['firstname']+' '+ x['person']['lastname'] for x in all_congress['people']]

# all_congress=[]
# my_str ="http://api.opencongress.org/people?format=json&page="
# for x in range(1,15):
#     new_var = json.loads(requests.get(my_str+str(x)).text)
#     all_congress.extend(new_var['people'])
    
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
    result = {}
    for x , i in zip(con_artists, range(len(con_artists))):
        #print i
        firstname = x['person']['firstname']
        lastname  = x['person']['lastname']
        attr =  find_person_attr(x,search_str)
        if attr:
            result[firstname + ' ' + lastname] = attr
    return result

