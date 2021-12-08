import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0080: 
    def __init__(self):
        if fsm.gl_state_debug_mode:
            print("\n===> State_60")

        if not fsm.gl_state_debug_mode:
            print("\n===> State_80")
            print("reached max_m")

            methods = classes_fsm_methods.FsmMethods()
            methods.finalStep()


            
            print("Done!")
