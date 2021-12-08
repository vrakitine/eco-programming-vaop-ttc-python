import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0050: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_50 fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]\n")

        if not fsm.gl_state_debug_mode:

            appls = classes_data_appls.Appls()

            if str(appls.getApplCodeByPriority(fsm.gl_appl_code_i_priority)) == str(fsm.gl_appl_code_checked): # loop

                print("\n loop :fsm.gl_appl_code_i_priority[", fsm.gl_appl_code_i_priority, "]")

                fsm.gl_event_code = "v_10" 

                return

            fsm.gl_event_code = "v_20" 

            return

