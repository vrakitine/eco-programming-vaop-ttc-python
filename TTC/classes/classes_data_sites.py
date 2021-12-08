import sys
import json
# local classes
import classes_data_appls
import classes_data_sites
import fsm
import classes_fsm_methods 
class Sites:
    def __init__(self):
            #self.sites_data_file_full_path = 'data/____ISEP/2019-09__01/schoolranks.json'
            #self.sites_data_file_full_path = 'data/____ISEP/2020-02_001/schoolranks.json'
            self.sites_data_file_full_path = 'data/____ISEP/2020-02_002/schoolranks.json'
            
    def isSiteHaveDuplicateApplicants(self):
        list_of_sites_with_duplicated_applicants = []
        for site in fsm.gl_data_s.keys():
            rank_list = fsm.gl_data_s[site]['rank_list']
            temp_01 = len(rank_list)
            temp_02 = len(set(rank_list))
            if temp_01 != temp_02:
                list_of_sites_with_duplicated_applicants.append(site)

        return list_of_sites_with_duplicated_applicants
        
    def getData(self):
        
        with open(self.sites_data_file_full_path, 'r') as f:
            sites_data = json.load(f)

        return sites_data

    def isAllSiteCapacity0(self):
        temp = True
        for site_code in fsm.gl_data_s.keys():
            if self.getCapacity(site_code) > 0:
                temp = False

                break

        return temp     

    def getCapacity(self, site_code):

        return float(fsm.gl_data_s[site_code]["attributes"]["capacity"])

    def updateCapacity(self, site_code, capacity):

        fsm.gl_data_s[str(site_code)]["attributes"]["capacity"] = str(capacity)

    def getMaxSiteCode(self):
        
       return max([int(s) for s in fsm.gl_data_s.keys()])

    # Remove all applicant from all site lists where applicant in assigned",
    def removeAllApplFromAllSiteListWhereApplAssigned(self):
        temp_data_s = fsm.gl_data_s
        for site_code in temp_data_s.keys():
            appl_list = temp_data_s[str(site_code)]["rank_list"]
            temp_appl_list = []
            for appl_code in appl_list:
                temp_appl_list.append(str(appl_code))
            for appl_code in appl_list:
                if appl_code in fsm.gl_result_a:
                    temp_appl_list.remove(str(appl_code))

            fsm.gl_data_s[str(site_code)]["rank_list"] = temp_appl_list   

    # Remove all applicant from all site lists where applicant site list is empty",
    def removeAllApplFromAllSiteListWhereApplSiteListIsEmpty(self):
        temp_data_s = fsm.gl_data_s
        for site_code in temp_data_s.keys():
            appl_list = temp_data_s[str(site_code)]["rank_list"]
            temp_appl_list = []
            for appl_code in appl_list:
                temp_appl_list.append(str(appl_code))
            for appl_code in appl_list:
                if len(fsm.gl_data_a[str(appl_code)]["rank_list"]) == 0:
                    temp_appl_list.remove(str(appl_code))

            fsm.gl_data_s[str(site_code)]["rank_list"] = temp_appl_list   

    def getFirstApplCode(self, site_code):

        return fsm.gl_data_s[str(site_code)]["rank_list"][0]      

    def isRankListEmpty(self, site_code):
        temp = False

        if len(fsm.gl_data_s[str(site_code)]["rank_list"]) == 0:
            temp = True

        return temp