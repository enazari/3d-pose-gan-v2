from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def draw_pose(DATA, outputPath, outputName):
    #input : DATA is an array of 105 elements, elements with indices devidable by three inidicate
    #x positions, those having a remainder of 1 inidicate y positions
    # those having a remainder of 2 inidicate z positions of joints respetively.

    #output: image of the frame


    # a row of raw data is as follows:
    # x1,y1,z1,x2,y2,z2,......x35,y35,z35
    X = DATA[0::3]
    Y = DATA[1::3]
    Z = DATA[2::3]
    
    structure = [[2,22,29],[3],[4],[5,8,15],[6],[7],[],[9],[10],[11],[12],[13],[14],[],[16],[17]\
         ,[18],[19],[20],[21],[],[23],[24],[25],[26],[27],[28],[],[30],[31],[32],[33],\
         [34],[35],[]] 

#         from mpl_toolkits.mplot3d import Axes3D
#         import numpy as np
#         import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.view_init(45, 45)

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])

    for joint in range(35):
        if structure[joint]  == []:
            continue
        children = structure[joint]
        self_ID = joint
        for child_ID in children:
            child_ID -= 1
            
            x0 = X[self_ID]
            y0 = Y[self_ID]
            z0 = Z[self_ID]
            
            x1 = X[child_ID]
            y1 = Y[child_ID]
            z1 = Z[child_ID]
            
            plt.plot([x0,x1],[y0,y1],[z0,z1],marker = 'o')

    plt.savefig(outputPath+'/'+outputName)
    #plt.show() 
    plt.close()