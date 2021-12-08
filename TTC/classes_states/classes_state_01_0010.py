import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0010: 
    def __init__(self):
        if fsm.gl_state_debug_mode:
            print("\nState_10: fsm.gl_test:[", fsm.gl_test, "]")

            fsm.gl_test = input("=======> test 10: ")
            print("\n===> State_10 fsm.gl_max_appl_code_i_priority:[", fsm.gl_max_appl_code_i_priority, "]")
    
            fsm.gl_event_code = "v_60"

        if not fsm.gl_state_debug_mode:
            fsm.gl_m = fsm.gl_m + 1

            fsm.gl_appls_checked_in_m_list = []


            print("gl_m:[", fsm.gl_m, "] from [", fsm.gl_max_m, "]")

            if fsm.gl_m > fsm.gl_max_m:

                fsm.gl_event_code = "v_20"

                return

            if fsm.gl_result_a_previous_len == len(fsm.gl_result_a.keys()) and fsm.gl_m > 1:

                fsm.gl_event_code = "v_20"

                print("len(fsm.gl_result_a:[", len(fsm.gl_result_a.keys()), "]")
                print("fsm.gl_result_a:", fsm.gl_result_a, "]")


                return
            
            
            #appls = classes_data_appls.Appls()
            if len(fsm.gl_data_a) == len(fsm.gl_result_a):
                fsm.gl_event_code = "v_30"

                return

            sites = classes_data_sites.Sites()
            if sites.isAllSiteCapacity0():
                fsm.gl_event_code = "v_40"

                return

            fsm.gl_result_a_previous_len = len(fsm.gl_result_a.keys()) 

            fsm.gl_appl_code_i_priority = 0

            fsm.gl_event_code = "v_10"