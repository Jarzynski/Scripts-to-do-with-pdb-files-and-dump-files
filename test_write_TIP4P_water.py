# This is a script to write a PDB file from a OPEN-mm pdb file
# the script is written by me to make a pdb file for tip4pew water

import sys
import numpy as np

# read the coordinates from the txt file
# the txt file is the coordinates of an sigle tip4pew water
# the coordinates are in the order of O, H1, H2, M
# the coordinates are in the unit of nm
# the coordinates are in the order of x, y, z



# 2023年12月27日
# 作者：吴凯
# 用法：python3 tip4p.py
# 依赖：numpy
# 说明：该脚本用于生成tip4p水模型的pdb文件，该脚本的输出文件为tip4p.pdb

import numpy as np

# 生成mw水模型的pdb文件
def tip4pdb():

    # 读取tip4p水模型的氧原子的坐标
    mw = np.loadtxt('E:/wukai/mw.xyz')

    # 在ice.pdb文件的末尾写入mw水模型的pdb文

    with open('E:/wukai/openmm/coexistence/tip4p.pdb', 'w') as f:
        for i in range(len(mw)):
            # 定义变量count_1为i除以9999的余数
            count_1 = i%9999
            # 根据模板文件中tip4p水模型的坐标，平移计算得到其他水分子具体原子的坐标
            # tip4p水模型的坐标为：O, H1, H2, M
            # O的坐标为：  5.558  19.020  12.139
            # H1的坐标为： 4.860  19.198  12.769
            # H2的坐标为： 5.800  19.881  11.799
            # M的坐标为：  5.498  19.157  12.177 %for tip4p-2005
            # M的坐标为：  5.497  19.160  12.178 %for tip4p-ice
          # f.write('HETATM{:5d}  MW{:3d} MW    1{:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(i+1, i+1, mw[i,0], mw[i,1], mw[i,2]))
            f.write('HETATM{:5d}  O   HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           O \n'.format(4*i+1, count_1+1, mw[i,0], mw[i,1], mw[i,2]))
            f.write('HETATM{:5d}  H1  HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(4*i+2, count_1+1, mw[i,0]-5.558+4.860, mw[i,1]-19.020+19.198, mw[i,2]-12.139+12.769))
            f.write('HETATM{:5d}  H2  HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(4*i+3, count_1+1, mw[i,0]-5.558+5.800, mw[i,1]-19.020+19.881, mw[i,2]-12.139+11.799))
            f.write('HETATM{:5d}  M   HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           M \n'.format(4*i+4, count_1+1, mw[i,0]-5.558+5.498, mw[i,1]-19.020+19.157, mw[i,2]-12.139+12.177))
        f.write('END\n')    

# 生成mw水模型的xyz文件
def mw_xyz():
    
        # 读取mw水模型的坐标
        mw = np.loadtxt('mw.xyz')
    
        # 生成mw水模型的xyz文件
        with open('mw.xyz', 'w') as f:
            for i in range(len(mw)):
                f.write('{:11.3f}{:8.3f}{:8.3f}'.format(mw[i,0], mw[i,1], mw[i,2]))

# 生成mw水模型的坐标位置文件
# 水的坐标为间隔0.3nm的点
# 给出要求的体积
# 从原点开始填充水的坐标，间隔为3，单位为angstrom
# 定义子函数，输入x，y，z的长度，输出坐标
def mw_xyz_1(x,y,z):
        

    # 计算水在x，y，z方向上的个数
    nx = int(x/3.0)
    ny = int(y/3.0)
    nz = int(z/3.0)
        
    # 生成mw水模型的坐标位置文件
    with open('E:/wukai/mw.xyz', 'w') as f:
        # 输出水的个数
        # f.write(str(nx*ny*nz))
        # 输出原子类型数目

        for i in range(nx):
            for j in range(ny):
                for k in range(nz):
                    f.write('{:11.3f}{:8.3f}{:8.3f}\n'.format(i*3.0, j*3.0, k*3.0+39))

# 主程序
mw_xyz_1(48,46,35)
tip4pdb()
