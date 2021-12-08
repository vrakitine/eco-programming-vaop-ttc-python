import sys
import json
import fileinput
# local classes
import fsm
import classes_data_appls
import classes_data_sites

class FsmMethods:
    def __init__(self):
        self.matrix_file_full_path = 'data/fsm/states_matrix_02.json'
        self.states_matrix = {}

    def getMatrix(self): 
        with open(self.matrix_file_full_path, 'r') as f:
            self.states_matrix = json.load(f)

        return self.states_matrix
            
    def checkDublicates(self):
        appls = classes_data_appls.Appls()
        #data_a = appls.getData()
        """
        for i in data_a:
            print("A-" + str(i) + " - " + str(data_a[i]))
        print("++++++++++++++++++++++++++")
        """
        temp_01 = appls.isApplicantHaveDuplicateSites()
        if len(temp_01):
            print("++++++")    
            print("appls", temp_01)    
            print("n=", len(temp_01))    
            print("++++++++++++++++++++++++++")

        sites = classes_data_sites.Sites()
        #data_s = sites.getData()
        """
        for i in data_s:
            print("S-" + str(i) + " - " + str(data_s[i]))
        print("++++++++++++++++++++++++++")

        """
        temp_02 = sites.isSiteHaveDuplicateApplicants()
        if len(temp_02):
            print("++++++")    
            print("sites", temp_02)    
            print("n=", len(temp_02))    
            print("++++++++++++++++++++++++++")

        temp_03 = appls.isDuplicateOrEmptyPriority()
        if len(temp_03):
            print("++++++")    
            print("isDuplicateOrEmptyPriority appls", temp_03)    
            print("n=", len(temp_03))    
            print("++++++++++++++++++++++++++")

        if len(temp_01) or len(temp_02) or len(temp_03):
            sys.exit("Stop temp_01 or temp_02 or temp_03")

    def finalStep(self):

        for appl_code in fsm.gl_data_a:
            if not appl_code in fsm.gl_result_a:
                fsm.gl_result_a.update({str(appl_code):"0"})

        with open('result_a.json', 'w') as fp:
            json.dump(fsm.gl_result_a, fp)
       
        with open('result_data_a.json', 'w') as fp:
            json.dump(fsm.gl_data_a, fp)
          
        with open('result_data_s.json', 'w') as fp:
            json.dump(fsm.gl_data_s, fp)

        self.convertToCsv()

    def convertToCsv(self):

        tempFile = open( 'result_a.csv', 'w' )
        tempFile.write( 'ApplicationPlacementRequestId,NMS_PlacedSchoolCode\n' )
        for appl in fsm.gl_result_a:
        
            #space = ''
            #max = 6 - len(str(appl))
            #i = 0
            #while i < max:
                #space = space + '-'

                #i = i + 1
            
            temp = appl + ',' + fsm.gl_result_a[appl] + '\n'
            tempFile.write( temp )

        tempFile.close()

    def log(self, log_msg):    
        fp = open('result_log.txt', 'a')
        fp.write(log_msg)
        fp.close()



