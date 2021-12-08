import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0070: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_70 fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]\n")

        if not fsm.gl_state_debug_mode:

            if not len(fsm.gl_checked_applicants_code_list):
                sys.exit("Error: fsm.gl_checked_applicants_code_list is empty")

            appls = classes_data_appls.Appls()
            appl_code = fsm.gl_checked_applicants_code_list[0]
            site_code = appls.getFirstSiteCode(appl_code)

            sites = classes_data_sites.Sites()
            site_capacity = sites.getCapacity(site_code)
            appl_weight = appls.getApplWeight(appl_code)
            site_capacity_new = site_capacity - appl_weight

            sites.updateCapacity(site_code, site_capacity_new)

            if site_capacity_new < 0:
                sys.exit("Error: site_capacity_new < 0")

            fsm.gl_result_a.update({str(appl_code):str(site_code)})

            del fsm.gl_checked_applicants_code_list[0]

            fsm.gl_event_code = "v_10" 

            return