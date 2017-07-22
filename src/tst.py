from wiki_access import wa_communicate
from bs4 import BeautifulSoup   #use it to find table in complex html -
import time
import sys




'''
    methond to add to a table in format below col k+1 header and data based on time stamp
        +--------+--------+ ... +--------+
        |HEADER 1|HEADER 2| ... |HEADER k|
        +--------+--------+ ... +--------+
        |R1 C1   |R1 C2   | ... |R1 Ck   |
        +--------+--------+ ... +--------+

'''
def add_time_stamp_as_last_col_of_two_line_table(html_body):
    
    
    #this is dummy data added for testng - TODO update rela data later on
    header_k1 = "T HEADER " + (time.strftime("%H:%M:%S"))
    data_k1 = "T DATA " + (time.strftime("%H:%M:%S"))
    
    soup = BeautifulSoup(html_body)
    
    #find all the tables in html body
    tables = soup.findChildren('table')
    
    #TBD -for now assume one table only 
    first_table = tables[0]
    
    rows = first_table.findChildren(['tr'])
    
    headers = first_table.findChildren(['th'])
    col_count = headers.__len__()
    line_count = rows.__len__()
    #print "line count %s" % line_count
    
    #updated table
    new_table = "<table><tbody><tr>"
    
    for header in headers:
            value = header.string
            #print "The header in this cell is %s" % value
            new_table +="<th>" + value + "</th>"
    #add new header
    new_table +="<th>" + header_k1 + "</th></tr>"
    #print "The new header is %s" % header_k1
    #print new_table
    
    count=0
    
    for row in rows:
        count +=1
        #print "now processing raw %s" % count
        add_to_this_line = 0
        
        cells = row.findChildren('td')
        if (cells.__len__() > 0):
            new_table +="<tr>"
        for cell in cells:
            value = cell.string
            add_to_this_line = 1
            #print "The value in this cell is %s" % value
            new_table +="<td>" + value + "</td>"
        #add new data
        if (add_to_this_line == 1):
            new_table +="<td>" + data_k1 + "</td></tr>" 
            #print "the new value for this line is %s" % data_k1
    new_table +="</tbody></table>"
    
    return new_table
        
    
    
    
page_to_update = "Update Me"
space_key = "CT"
    
#get wiki object or space 
wiki = wa_communicate.wiki_space(space_key)


#get page data 
json_page_data = wiki.getPage(page_to_update)
print "\n\npage data read from wiki---------"
print json_page_data
print "\n\n"

#get page version (will need to update the version when updating the page)
page_version = wiki.extract_page_version(json_page_data)
print "\npage version %s --------" % page_version

#get page id
page_id = wiki.extract_page_id(json_page_data)

#get page parent name and id (will need parent info to ensure links are maintained on update)
(parent_name,parent_id) = wiki.extract_page_ancestor(json_page_data,page_to_update )
print "\nparent name %s  parent id %s ---------" % (parent_name,parent_id)

#get html of page 
page_body = wiki.extract_page_body(json_page_data)
print "\npage body\n%s--------" % page_body
''' 
TBD develope html parser based on spec of KPI pages - takl to vijay on spec"""
in this example the page Update Me have one table and each time we update the page
we add time stamp to the last col
'''

new_table  =  add_time_stamp_as_last_col_of_two_line_table(page_body)

print "\nnew data:\n%s -------" % new_table

wiki.update_page_body(space_key,parent_id,page_id,page_to_update, page_version+1, new_table)



#wiki.update_page_body(self,space_key,page_ancestor,page_title, version, new_body):








