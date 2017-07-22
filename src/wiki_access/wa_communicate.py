# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "sarel"
__date__ = "$Mar 3, 2015 5:56:37 PM$"

if __name__ == "__main__":
    print "running from %s"%__name__

import requests
import json
import logging
from toolbox.tb_logger import tb_logger


class wiki_space(tb_logger):
    """Wiki Space have followng properties:

    Attributes:
        name: string, confluence space name
        acl:  access control uid/pswd
        REST_API_URL: url for REST API
    """

    def __init__(self, 
                name="TODO-REPLACE-ME-WITH-CONFLUENCE-SPACE-NAME", 
                pswd = 'TODO-REPLACE-ME-WITH-CONFLUENCE-PSWD',
                uid='TODO-REPLACE-ME-WITH-CONFLUECE-UID'):
                    
        """constructor - Return an initialized object """
        
        tb_logger.__init__(self)
        
        """ init this object """
        self.SpaceName = name
        self.UID = uid
        self.PSWD = pswd
        self.REST_API_URL = 'https:<YOUR-ORG-ONFLUENCE-SERVER>/confluence/rest/api/content'
        self.expandProperites='body.storage,version,ancestors'
        #expand space will show all space 
        
        
    def getPage(self,page):
        """ page - name of the page in the SpaceName
           return json struct representing page data 
        """
        
        r = requests.get(
                            self.REST_API_URL,
                            verify=False,
                                params={ 
                                        'spaceKey':self.SpaceName,
                                        'title':page, 
                                        'expand':self.expandProperites
                                        },
                                auth=(self.UID, self.PSWD),
                            
                        )
        self.logger.debug(">>>>>>> in getPage")
        json_st =  json.dumps(r.json(), sort_keys=True, indent=2)
        return json_st
    
       

        
    def extract_page_version(self,json_page_data):
        self.logger.debug(">>>>>>> in extract_page_version")
        data = json.loads(json_page_data)
        ver_num = data['results'][0]['version']['number']
        return ver_num
    
    def extract_page_id(self,json_page_data):
        self.logger.debug(">>>>>>> in extract_page_version")
        data = json.loads(json_page_data)
        page_id = data['results'][0]['id']
        return page_id
    
    def extract_page_ancestor(self,json_page_data,page_name):
        data = json.loads(json_page_data)
        
        #verify page_name match data read from json
        read_page_id = data['results'][0]['id']
        read_page_name = data['results'][0]['title']
        #print "page name " + page_name  +" read info is,  page name " + read_page_name + " id " + read_page_id 
        
        #get last element in json ancestor array (this is parent of page)
        ancestor_list = data['results'][0]['ancestors']
        parent_info = ancestor_list.pop()
        
        parent_id = parent_info['id']
        parent_name = parent_info['title']
        
        #print "parent name " + parent_name  + " id " + parent_id
        return (parent_name,parent_id)
        
        
    def extract_page_body(self,json_page_data):
        data = json.loads(json_page_data)
        
        #verify page_name match data read from json
        page_body = data['results'][0]['body']['storage']['value']
        
        print page_body
        return page_body
        
        
    def update_page_body(self,space_key,ancestor_id,page_id,page_title, version, new_body):
        self.logger.debug(">>>>>>> in update_page_body")  
        
        url = self.REST_API_URL + "/" + page_id
        
        data = json.dumps(
            {
                'id' : page_id,
                'type' : 'page',
                "ancestors":[{"type":"page","id":ancestor_id}],
                'title' : page_title,
                'space' : {'key' : space_key},
                'body' :
                {
                    'storage' :
                    {
                        'representation' : 'storage',
                        'value' :new_body
                    }
                },
                'version' : {"number":version}
            })

            
        r = requests.put(
            url,
            verify=False,
            data = data,
            auth = (self.UID, self.PSWD),
            headers = {
                'Content-Type' : 'application/json',
                'Accept' : 'application/json'
                }
        )
        json_st =  json.dumps(r.json(), sort_keys=True, indent=2)
        print json_st
        return json_st
        
        
        
    
