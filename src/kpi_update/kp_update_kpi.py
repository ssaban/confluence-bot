# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "sarel"
__date__ = "$Apr 12, 2015 11:31:05 AM$"

if __name__ == "__main__":
    print "running from %s"%__name__

from wiki_access import wa_communicate
from bs4 import BeautifulSoup   #use it to find table in complex html -
import time
import sys
import re


''' 
g_kpi_map - for each kpi, include the data needed to update the relevant 
confluence page

'''




g_kpi_map = {
    'TTS Data To Playback' : {
    'jira_space_key' : "TODO-CHANGE-TO-CONFLUENCE-SPACE-NAME",
    'kpi_page_name'  : "TODO-CHANGE-TO-CONFLUENCE-PAGE-TO-UPDATE",  #replace with confluence page name
    'table_id'       : 0,
    'update'         : "row",
    'data_headers'   : ['Release Cycle','Sprint Cycle','S/W Version',
                            'Update Timestamp','KPI Name','Number Of Iteration',
                            'Priority','TP50%','TP90%']
    }
}

def kp_gen_current_time_stamp():
    return time.strftime("%b %d %Y %H:%M:%S")

#generate an html table line 
#extract the order of the table coloumn based on data headers (frpom g_kpi map for a given kpi)
#extract the value from the json_data (passed by the acutal test)
def kp_gen_html_table_line(data_headers, json_data):
    
    line = "<tr>"
    col_count = len(data_headers)
    
    print "\n %s col_count" % col_count
    
    if col_count <> json_data['param_cnt']:
        print "mismatch between col count expected %s and received %s" %(col_count,json_data['param_cnt'])
    else:
        for i in range (0,col_count):
            line += '<td colspan="1">' + str(json_data[data_headers[i]]) + '</td>' 
    line +="</tr>"
    return line
            
            

def kp_update_TTS_Data_To_Playback(kpi,json_data):
    
    jira_space = g_kpi_map[kpi]['jira_space_key']
    page_to_update = g_kpi_map[kpi]['kpi_page_name']
    table_id = g_kpi_map[kpi]['table_id']
    data_headers = g_kpi_map[kpi]['data_headers']

    wiki = wa_communicate.wiki_space(jira_space)
    
    #get page data 
    json_page_data = wiki.getPage(page_to_update)
    #print "1 json_page_data %s "% json_page_data
    
    #get page version (will need to update the version when updating the page)
    page_version = wiki.extract_page_version(json_page_data)
    
    #get page id
    page_id = wiki.extract_page_id(json_page_data)

    #get page parent name and id (will need parent info to ensure links are maintained on update)
    (parent_name,parent_id) = wiki.extract_page_ancestor(json_page_data,page_to_update )
    
    #get html of page 
    page_body = wiki.extract_page_body(json_page_data)
    print "\n====2 page body %s\n\n======\n" % page_body
    
    
    
    result_line = kp_gen_html_table_line(data_headers, json_data)
    
    print "\n====3 line to add to table %s\n=====\n" % result_line
 

    #add a line to the relevant table
    new_table = kp_add_line_to_table(page_body,table_id, result_line)
    
    print "\n===4 new html %s \n=====" % new_table
    
    
    
    wiki.update_page_body(jira_space,parent_id,page_id,page_to_update, page_version+1, new_table)
    
    
    
    
    
    print "update_TTS_Data_To_Playback called"
    return
    




''' get an html body extract the table id, add to it result_line and return the 
    updated table
    TBD - handle also pages that has more then table content
'''
def kp_add_line_to_table(html_body,table_id,result_line):
    
    soup = BeautifulSoup(html_body)
    
    #find all the tables in html body
    tables = soup.findChildren('table')
    
    #find the table to modify based on table id ( id 0 for first table on page etc)

    table2modify = tables[table_id]
    
    rows = table2modify.findChildren(['tr'])
    
    rows.append(result_line)
    
    new_table = "<table><tbody>" 
    for r in rows:
        new_table += str(r)

    new_table +="</tbody></table>"
    
    return new_table
    
    
    
    
''' generic method to update tables'''
    
def kp_update_kpi_page(kpi,json_data):
    update_lut = {
        'TTS Data To Playback':kp_update_TTS_Data_To_Playback
    }
        
        
    if update_lut.has_key(kpi):
        update_lut[kpi](kpi,json_data)
    else:
        print "TBD update method for %s" % kpi
    



