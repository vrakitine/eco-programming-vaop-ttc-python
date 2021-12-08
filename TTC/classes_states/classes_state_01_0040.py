import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0040: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_40 fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]\n")

        if not fsm.gl_state_debug_mode:
            sites = classes_data_sites.Sites()

            if sites.isRankListEmpty(fsm.gl_site_code_checked):
                fsm.gl_event_code = "v_20" 

                return

            fsm.gl_appl_code_checked = sites.getFirstApplCode(fsm.gl_site_code_checked)

            if not fsm.gl_appl_code_checked in fsm.gl_data_a.keys():
                fsm.gl_event_code = "v_30" 

                return

            fsm.gl_event_code = "v_10" 

            return

