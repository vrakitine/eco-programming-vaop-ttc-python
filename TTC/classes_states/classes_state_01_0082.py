import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods

class State_0082: 
    def __init__(self):
        if fsm.gl_state_debug_mode:
            print("isAllSiteCapacity0() = True")
            print("Done!")

        if not fsm.gl_state_debug_mode:
            print("isAllSiteCapacity0() = True")

            methods = classes_fsm_methods.FsmMethods()
            methods.finalStep()

            print("Done!")