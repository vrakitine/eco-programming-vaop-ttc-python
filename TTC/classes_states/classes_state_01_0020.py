import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0020: 
    def __init__(self):
    
        if fsm.gl_state_debug_mode:
            print("\n===> State_20 fsm.gl_max_appl_code_i_priority:[", fsm.fsm.gl_max_appl_code_i_priority, "]")
            print("\n===> State_20 gl_max_site_code_i:[", fsm.gl_max_site_code_i, "]")
        
            test = input("=======> test 20: ")
            print("\n===> State_20 test:[", test, "]")
    
            fsm.gl_event_code = "v_30"      

        if not fsm.gl_state_debug_mode:

            appls = classes_data_appls.Appls()
            appls.removeAllSitesFromAllApplicantLists()
            sites = classes_data_sites.Sites()
            sites.removeAllApplFromAllSiteListWhereApplAssigned()
            sites.removeAllApplFromAllSiteListWhereApplSiteListIsEmpty()

            i = fsm.gl_appl_code_i_priority + 1
            appls = classes_data_appls.Appls()
            while i <= fsm.gl_max_appl_code_i_priority + 1:
                fsm.gl_appl_code_i_priority = i

                #print("gl_appls_checked_in_m_list:[", fsm.gl_appls_checked_in_m_list, "]")

                if appls.isApplCodeInApplData() and (not str(appls.getApplCodeByPriority(fsm.gl_appl_code_i_priority)) in fsm.gl_appls_checked_in_m_list):

                    fsm.gl_appls_checked_in_m_list.append(str(appls.getApplCodeByPriority(fsm.gl_appl_code_i_priority)))

                    print("\n\n================>fsm.gl_appl_code_i_priority:[", fsm.gl_appl_code_i_priority, "]  gl_m:[",fsm.gl_m,"] gl_max_m", fsm.gl_max_m, "]")
                    print("len(fsm.gl_result_a:[", len(fsm.gl_result_a.keys()), "]")
                    #print("fsm.gl_result_a:", fsm.gl_result_a, "]")
                    #print("\nfsm.gl_data_a:[", fsm.gl_data_a, "]")
                    #print("\nfsm.gl_data_s:[", fsm.gl_data_s, "]")

                    fsm.gl_jump = 0

                    fsm.gl_max_jump = len(fsm.gl_data_a.keys()) - len(fsm.gl_appls_checked_in_m_list)

                    fsm.gl_appl_code_checked = appls.getApplCodeByPriority(fsm.gl_appl_code_i_priority)

                    fsm.gl_taken_sites_capacity_dict = dict()

                    fsm.gl_checked_applicants_code_list = []

                    fsm.gl_event_code = "v_20"

                    return
                    
                if not appls.isApplCodeInApplData():
                    i = i + 1

                    continue

            fsm.gl_event_code = "v_10" 
