import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods
class Appls:
    def __init__(self):
            #self.applicants_data_file_full_path = 'data/____ISEP/2019-09__01/studentranks.json'
            #self.applicants_data_file_full_path = 'data/____ISEP/2020-02_001/studentranks.json'
            self.applicants_data_file_full_path = 'data/____ISEP/2020-02_002/studentranks.json'

    def getPriorityToApplCode(self):
        temp = {}
        for appl_code in fsm.gl_data_a.keys():
            priority = fsm.gl_data_a[appl_code]['attributes']['sequence']
            temp[priority] = appl_code

        return temp

    def getApplCodeByPriority(self, priority):

        return fsm.gl_priority_to_appl_code[str(priority)]

    def isDuplicateOrEmptyPriority(self):
        list_of_applicants_with_duplicated_or_empty_priority = []
        temp_dict = {}
        for appl_code in fsm.gl_data_a.keys():
            priority = fsm.gl_data_a[appl_code]['attributes']['sequence']
            if priority == '':
                list_of_applicants_with_duplicated_or_empty_priority.append(appl_code)

                continue
            if priority in temp_dict.keys():   
                list_of_applicants_with_duplicated_or_empty_priority.append(appl_code)

                continue

            temp_dict[priority] = appl_code
        
        return list_of_applicants_with_duplicated_or_empty_priority

    def isApplicantHaveDuplicateSites(self):
        list_of_applicants_with_duplicated_sites = []
        for appl in fsm.gl_data_a.keys():
            rank_list = fsm.gl_data_a[appl]['rank_list']
            temp_01 = len(rank_list)
            temp_02 = len(set(rank_list))
            if temp_01 != temp_02:
                list_of_applicants_with_duplicated_sites.append(appl)

        return list_of_applicants_with_duplicated_sites
       
    def getData(self):
        
        with open(self.applicants_data_file_full_path, 'r') as f:
            applicants_data = json.load(f)

        return applicants_data

    def isUnassignedAppsArrayEmpty(self):
        temp = True
        if len(fsm.gl_data_a.keys()) > 0:
            temp = False

        return temp

    def getMaxApplCode(self):
        
        return max([int(s) for s in fsm.gl_data_a.keys()])

    def getMaxApplPriorityCode(self):
        
        return max([int(s) for s in fsm.gl_priority_to_appl_code.keys()])

    def getApplWeight(self, appl_code):

        return float(fsm.gl_data_a[str(appl_code)]["attributes"]["weight"])

    def isApplCodeInApplData(self):
        temp = False
        #if str(fsm.gl_appl_code_i_priority) in fsm.gl_data_a:
        if str(fsm.gl_appl_code_i_priority) in fsm.gl_priority_to_appl_code:
            temp = True

        return temp

    #Remove all sites from all applicant lists where applicant weight > capacity
    def removeAllSitesFromAllApplicantLists(self):
        sites = classes_data_sites.Sites()
        temp_data_a = fsm.gl_data_a
        for appl_code in temp_data_a.keys():
            site_list = temp_data_a[str(appl_code)]["rank_list"]
            temp_site_list = []
            for site_code in site_list:
                temp_site_list.append(str(site_code))
            for site_code in site_list:
                if sites.getCapacity(site_code) < self.getApplWeight(appl_code):
                    #fsm.gl_data_a[str(appl_code)]["rank_list"].remove(site_code)
                    temp_site_list.remove(site_code)

            fsm.gl_data_a[str(appl_code)]["rank_list"] = temp_site_list

    def getFirstSiteCode(self, appl_code):

        return fsm.gl_data_a[str(appl_code)]["rank_list"][0]      

    def isRankListEmpty(self, appl_code):
        temp = False

        if len(fsm.gl_data_a[str(appl_code)]["rank_list"]) == 0:
            temp = True

        return temp

        

