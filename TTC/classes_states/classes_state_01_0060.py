import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0060: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_60 fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]\n")

        if not fsm.gl_state_debug_mode:
            if fsm.gl_debug_mode:
                print("\n===> State_60 fsm.gl_checked_applicants_code_list:[", fsm.gl_checked_applicants_code_list, "]")

            if not len(fsm.gl_checked_applicants_code_list):
                fsm.gl_event_code = "v_10" 

                return

            fsm.gl_event_code = "v_20" 

            return      