# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "sarel"
__date__ = "$Apr 12, 2015 1:19:15 PM$"


    
from wiki_access import wa_communicate
from kpi_update import kp_update_kpi

time_stamp = kp_update_kpi.kp_gen_current_time_stamp()

json4_TTS_Data_To_Playback = {
    'param_cnt' : 9,
    'Release Cycle' : 'RC1',
    'Sprint Cycle' :   'SC1',
    'S/W Version'  :'SV1',
    'Update Timestamp'  :time_stamp,
    'KPI Name': "TTS Data To Playback" ,
    'Number Of Iteration': 50,
    'Priority':'P0',
    'TP50%' :30,
    'TP90%' :20
}

    
kp_update_kpi.kp_update_kpi_page("TTS Data To Playback",json4_TTS_Data_To_Playback )

