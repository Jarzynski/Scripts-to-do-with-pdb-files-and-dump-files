#!/usr/bin/env python
# coding: utf-8
import ovito
from ovito import scene
from ovito.io import *
from ovito.modifiers import *
from ovito.pipeline import *
from ovito.vis import *
import numpy as np
from copy import deepcopy
import sys,os
from scipy.optimize import fsolve
import datetime
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
# plt.style.use(['science'])


# trjfilename=sys.argv[1]
epsi0='E:/wukai/openmm/ice_growth/250growth.dump'
epsi1='E:/wukai/openmm/ice_growth/260growth.dump'
# epsi2='E:/wukai/openmm/lamda_1.05/epsi_2_anneal.dump'

def get_max_cluster(trjfilename):
    pipeline = import_file(trjfilename)
    pipeline.modifiers.append(ChillPlusModifier())
    pipeline.modifiers.append(SelectTypeModifier(
        operate_on = "particles",
        property = "Structure Type",
        types = { 0,3,4,5 }
        # types = { 1,2 }
    ))
    pipeline.modifiers.append(DeleteSelectedModifier())

    pipeline.modifiers.append(ClusterAnalysisModifier(
        cutoff=3.5, 
        sort_by_size=True, 
        compute_com=True))
    pipeline.modifiers.append(ExpressionSelectionModifier(expression="Cluster!=1"))
    pipeline.modifiers.append(DeleteSelectedModifier())

    file_out=open('cluster_size.xvg','w')
    file_out.write('#frame, pureice_num')

#write data in every frame to txt file
    for nframe in range(pipeline.source.num_frames):
        if nframe %100==0:
            print('  frame='+str(nframe))
        data = pipeline.compute(nframe)
        # 
        ctime=data.attributes['Timestep']
        file_out.write('%d %f %d \n'%(nframe,ctime,data.particles.count))  
    #    print(data.particles)    
        # file_out.write('%d %f \n'%(nframe,ctime))  
        # break
    file_out.close()  
        
    data=np.loadtxt('cluster_size.xvg')
    return data

matplotlib.use('Agg')

a0=get_max_cluster(epsi0)[:,]
x0,y0=a0[:,0],a0[:,2]
time0=x0*0.15
plot(time0,y0,label="Temp=250")

a1=get_max_cluster(epsi1)[:,]
x1,y1=a1[:,0],a1[:,2]
time1=x1*0.15
plot(time1,y1,label="temp=260")

# a2=get_max_cluster(epsi0)[:,]
# x2,y2=a2[:,0],a2[:,2]
# time2=x2*0.15
# plot(time2,y2,label=r"$\epsilon$=0.2")

xlabel('time (ns)')
ylabel('Number of max cluster')
title('new potential energy')
legend()
show()
savefig('E:/wukai/openmm/ice_growth/0.png',dpi=300)

close()








