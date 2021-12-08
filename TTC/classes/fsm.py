import os
import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import classes_fsm_methods
# states
import classes_state_01_0000
import classes_state_01_0010
import classes_state_01_0020
import classes_state_01_0035
import classes_state_01_0040
import classes_state_01_0050
import classes_state_01_0060
import classes_state_01_0070
import classes_state_01_0080 # Final
import classes_state_01_0081 # Final
import classes_state_01_0082 # Final

class FsmStates():

    def __init__(self):
    # system var
        global gl_debug_mode
        #gl_debug_mode = True
        gl_debug_mode = False

        global gl_state_debug_mode
        #gl_state_debug_mode = True
        gl_state_debug_mode = False
    # fsm var
        global gl_test
        gl_test = "start 1"

        global gl_event_code
        gl_event_code = "v_00"

        global gl_previous_state_code
        gl_previous_state_code = "s_01_0000"

        global gl_current_state_code
        gl_current_state_code = "s_01_0000"
      
        fsm_methods = classes_fsm_methods.FsmMethods()   
        
        global gl_states_matrix
        gl_states_matrix = fsm_methods.getMatrix()

    # task var
        global gl_data_a
        global gl_data_s

        global gl_priority_to_appl_code

        global gl_result_a
        global gl_result_a_previous_len
        global gl_result_s

        

        global gl_max_m 
        global gl_m
        global gl_appls_checked_in_m_list

        global gl_max_jump
        global gl_jump

        global gl_max_appl_code_i_priority
        global gl_appl_code_i_priority
        global gl_appl_code_checked

        global gl_max_site_code_i
        global gl_site_code_i
        global gl_site_code_checked

        global gl_taken_sites_capacity_dict

        global gl_checked_applicants_code_list

        gl_data_a = dict()

        gl_data_s = dict()

        gl_priority_to_appl_code = dict()

        gl_result_a = dict()

        gl_result_a_previous_len = 0

        gl_result_s = dict()

        gl_max_m = 0
        gl_m = 0
        gl_appls_checked_in_m_list = []

        gl_max_jump = 0
        gl_jump = 0

        gl_max_appl_code_i_priority = 0
        gl_appl_code_i_priority = 0
        gl_appl_code_checked = 0

        gl_max_site_code_i = 0
        gl_site_code_i = 0
        gl_site_code_checked = 0

        gl_taken_sites_capacity_dict = dict()

        gl_checked_applicants_code_list = []

  
        self.start()

    def start(self):

        while True:

            self.getCurrentState()

            
            
            if gl_current_state_code == "s_01_0000":
                classes_state_01_0000.State_0000()
                continue

            if gl_current_state_code == "s_01_0010":
                classes_state_01_0010.State_0010()
                continue

            if gl_current_state_code == "s_01_0020":
                classes_state_01_0020.State_0020()
                continue

            if gl_current_state_code == "s_01_0035":
                classes_state_01_0035.State_0035()
                continue

            if gl_current_state_code == "Err_0035_030": # Err_0035_030
                self.errorState()

            if gl_current_state_code == "Err_0035_040": # Err_0035_040
                self.errorState()

            if gl_current_state_code == "s_01_0040":
                classes_state_01_0040.State_0040()
                continue

            if gl_current_state_code == "s_01_0050":
                classes_state_01_0050.State_0050()
                continue

            if gl_current_state_code == "s_01_0060":
                classes_state_01_0060.State_0060()
                continue

            if gl_current_state_code == "s_01_0070":
                classes_state_01_0070.State_0070()
                continue

            if gl_current_state_code == "s_01_0080":
                classes_state_01_0080.State_0080()
                self.finalStateDone()

            if gl_current_state_code == "s_01_0081":
                classes_state_01_0081.State_0081()
                self.finalStateDone()

            if gl_current_state_code == "s_01_0082":
                classes_state_01_0082.State_0082()
                self.finalStateDone()
                
            sys.exit("\n\nError: Unknown state:[" + gl_current_state_code + "]\n")

    def getCurrentState(self):
        
        global gl_event_code
        global gl_previous_event_code

        global gl_previous_state_code
        global gl_current_state_code
        
        global gl_states_matrix
        
        temp = gl_current_state_code
        gl_current_state_code = gl_states_matrix[gl_current_state_code][gl_event_code]
        gl_previous_state_code = temp

        self.stateLog()

        gl_previous_event_code = gl_event_code
        gl_event_code = "v_undefined"


    def stateLog(self):
        log_msg = "\n ==>>> stateLog -> " + str(gl_previous_state_code) + " | " + str(gl_event_code) + " | " + str(gl_current_state_code)
        if gl_debug_mode:
            print(log_msg)

        fsm_methods = classes_fsm_methods.FsmMethods()
        fsm_methods.log(log_msg)

    def finalStateDone(self):
        sys.exit("\n\nDone in final state:[" + gl_current_state_code + "]\n")

    def errorState(self):
        sys.exit("\n\nError state:[" + gl_current_state_code + "]\n")
