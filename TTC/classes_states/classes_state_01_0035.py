import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0035: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_35 fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]\n")

        if not fsm.gl_state_debug_mode:

            fsm.gl_jump = fsm.gl_jump + 1
            if fsm.gl_debug_mode:
                print("--jump-->", fsm.gl_jump, fsm.gl_max_jump)
                print("gl_taken_sites_capacity_dict:[",fsm.gl_taken_sites_capacity_dict, "]")
                print("gl_checked_applicants_code_list:[",fsm.gl_checked_applicants_code_list, "]")

            if fsm.gl_jump > fsm.gl_max_jump + 1:
                fsm.gl_event_code = "v_50" 

                return

            fsm.gl_checked_applicants_code_list.append(str(fsm.gl_appl_code_checked))
            
            appls = classes_data_appls.Appls()

            if appls.isRankListEmpty(fsm.gl_appl_code_checked):
                fsm.gl_event_code = "v_30" 

                return

            fsm.gl_site_code_checked = appls.getFirstSiteCode(fsm.gl_appl_code_checked)

            if not fsm.gl_site_code_checked in fsm.gl_data_s.keys():
                fsm.gl_event_code = "v_40" 

                return

            sites = classes_data_sites.Sites()
            site_capacity = sites.getCapacity(fsm.gl_site_code_checked)
            
            if fsm.gl_site_code_checked in fsm.gl_taken_sites_capacity_dict:
                site_capacity = site_capacity - float(fsm.gl_taken_sites_capacity_dict[str(fsm.gl_site_code_checked)])

            if fsm.gl_debug_mode:
                print("------------>>,fsm.gl_appl_code_i_priority, fsm.gl_appl_code_checked, fsm.gl_site_code_checked, appls.getApplWeight(fsm.gl_appl_code_checked),site_capacity")
                print("------------>>",fsm.gl_appl_code_i_priority, fsm.gl_appl_code_checked, fsm.gl_site_code_checked, appls.getApplWeight(fsm.gl_appl_code_checked),site_capacity)

            if appls.getApplWeight(fsm.gl_appl_code_checked) > site_capacity:
                fsm.gl_event_code = "v_20" 

                return

            if fsm.gl_site_code_checked in fsm.gl_taken_sites_capacity_dict:
                temp = float(fsm.gl_taken_sites_capacity_dict[str(fsm.gl_site_code_checked)]) + appls.getApplWeight(fsm.gl_appl_code_checked)
                fsm.gl_taken_sites_capacity_dict.update({str(fsm.gl_site_code_checked):str(temp)})
            if not fsm.gl_site_code_checked in fsm.gl_taken_sites_capacity_dict:
                fsm.gl_taken_sites_capacity_dict.update({str(fsm.gl_site_code_checked):str(appls.getApplWeight(fsm.gl_appl_code_checked))})

            fsm.gl_event_code = "v_10" 

            return
            