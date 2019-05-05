import scipy.io
import numpy as np

class data_loader():
    #loading frames of given actions
    def __init__(self, matlab_action_path='', actions_list=[1]):
        self.map = matlab_action_path
        self.actions_list = actions_list
        
    def __get_raw_action(self, no_action=1, twoD_true_or_threeD_false=False):
        data_all = scipy.io.loadmat(self.map+'action_'+str(no_action)+'_Data.mat')
        if twoD_true_or_threeD_false:
            data = data_all['TwoD_Trajectories']
        else:
            data = data_all['ThreeD_Trajectories']
        
        return data
    
    def person_repeat(self, data, no_person, no_repeat, twoD_true_or_threeD_false=False):
        if twoD_true_or_threeD_false:
            data = data[no_person][no_repeat][0][0]
        else:
            data = data[no_person][no_repeat]
        return data
    
    def person_all_repeats(self, data, no_person, twoD_true_or_threeD_false=False):
        flag = twoD_true_or_threeD_false
        mylist = []
        for repeatation in range(5):
            mylist.extend(self.person_repeat(data, no_person, repeatation,flag))
        return mylist
    
    def actions(self, list_of_actions, twoD_true_or_threeD_false=False):
        flag = twoD_true_or_threeD_false
        mylist = []
        for theaction in list_of_actions:
            data = self.__get_raw_action(theaction, flag)
            for person in range(10): 
                mylist.extend(self.person_all_repeats(data, person, flag))
        return mylist
    
    def actions_standardised(self, list_of_actions, twoD_true_or_threeD_false=False):
        threeD = self.actions( list_of_actions, twoD_true_or_threeD_false=False)
        npthreeD = np.array(threeD)
        threeD_mean = npthreeD.mean()
        threeD_std = npthreeD.std()
        npthreeD_standard = (npthreeD - threeD_mean) / threeD_std
        return npthreeD_standard, threeD_mean, threeD_std
    
    def actions_normalised(self, list_of_actions, twoD_true_or_threeD_false=False):
        threeD = self.actions( list_of_actions, twoD_true_or_threeD_false=False)
        npthreeD = np.array(threeD)
        threeD_min = npthreeD.min()
        threeD_max = npthreeD.max()
        npthreeD_normalised= np.interp(npthreeD, (threeD_min, threeD_max), (-1, +1))
        return npthreeD_normalised, threeD_min, threeD_max