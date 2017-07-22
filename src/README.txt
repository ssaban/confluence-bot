General
=======
Code to update Confluence Wiki pages & Test KPI

from your test infrastructure - when you have the data to update 
in format 'json_struct_with_test_results' for a KPI kpi_name
call kp_update_kpi.kp_update_kpi_page(kpi_name,json_struct_with_test_results )
to update the relevant confluence table for kpi_name.

a working example exists for 'TTS Data To Playback' KPI

the work flow for a KPI is:

for each KPI ensure you have the following: 
1. kp_update_kpi.py:   
        g_kpi_map - include records for all supported KPI, 
        record contain the page to update, the table headers etc

2. kp_update_kpi.py:    
        kp_update_kpi_page(kpi,json_data) contain a map of function pointers to
        relevant KPI update.  
        ensure map include handlers for the KPIs you are interested to update

3.from the test environment, when you have all the data need to update a 
        KPI confluence page, format the data as a json struct and call 
        kp_update_kpi_page(kpi,json_data)


tst_TTS_Data_To_Playback.py provide a working example of above for the 
'TTS Data To Playback' KPI
Note: integrate this code from the test system and ensure you generate actual
data (in example dummy data is generated)



Activation Instruction
=====================

Pre Conditions
--------------
1. ensure you have the python module in sectioin 'Modules used'
2. ensure you have access to 
< https://YOUR-ORG-SERVER/confluence/display/SAND-BOX-DOMAIN > 
(this is sand box to test this code)

code structure
==============
include 3 packages and test code

packages
--------
1. toolbox - general utilities (for example logging class)
2. wiki_access - uses REST API to interact with confluence
3. kpi_update  - logic to collect and format kpi data from external environment
                 and update the proper confluence table for the kpi.


Test code
---------
tst.py - auto add a time stamped header and column to table at 
location <ADD HERE CONFLUENCE PAGE USED AS TARGET FOR THE TEST test.py>

tst_TTS_Data_To_Playback.py - test the generic kp_update_kpi_page method to 
update the 'TTS Data To Playback' KPI under 
<ADD HERE CONFLUENCE PAGE USED AS TARGET FOR THE TEST tst_TTS_Data_To_Playback.py>


Extenral Packages you need to install 
=====================================
(v-bot)5cf938ae18fa:src sarel$ yolk -l
Pygments        - 2.0.2        - active 
Python          - 2.7.8        - active development 
beautifulsoup4  - 4.3.2        - active 
httpie          - 0.9.2        - active 
jason           - 0.1.7        - active 
pip 6.0.8 has no metadata
requests        - 2.5.3        - active 
setuptools 12.0.5 has no metadata
wsgiref         - 0.1.2        - active development (/usr/local/Cellar/python/2.7.8_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7)
yolk            - 0.4.3        - active
