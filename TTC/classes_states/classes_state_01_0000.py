import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0000:
    def __init__(self):
        if fsm.gl_state_debug_mode:

            fsm.gl_test = fsm.gl_test + "22222"
            print("\nState_00: fsm.gl_test:[", fsm.gl_test, "]")
            fsm.gl_event_code = "v_10"

        if not fsm.gl_state_debug_mode:

            fsm.gl_max_m = 200
            fsm.gl_m = 0
            
            appls = classes_data_appls.Appls()
            fsm.gl_data_a = appls.getData()

        
            #fsm.gl_max_appl_code_i = appls.getMaxApplCode()
            #fsm.gl_appl_code_i = 0

            sites = classes_data_sites.Sites()
            fsm.gl_data_s = sites.getData()
            fsm.gl_max_site_code_i = sites.getMaxSiteCode()
            fsm.gl_site_code_i = 0
            
            fsm_methods = classes_fsm_methods.FsmMethods()
            fsm_methods.checkDublicates()

            fsm.gl_priority_to_appl_code = appls.getPriorityToApplCode()

            print("gl_priority_to_appl_code is: ", fsm.gl_priority_to_appl_code) 

            fsm.gl_max_appl_code_i_priority = appls.getMaxApplPriorityCode()
            fsm.gl_appl_code_i_priority = 0

            fsm.gl_event_code = "v_10"
       