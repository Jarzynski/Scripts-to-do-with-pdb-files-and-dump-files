# This is a script to write a PDB file from a OPEN-mm pdb file
# the script is written by me to make a pdb file for tip4p-ice water

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
    mw = np.loadtxt('mw.xyz')
    size_a = (int(np.floor(len(mw)/3)),3)
    mm = np.zeros(size_a)
    # 生成tip4p水模型的pdb文件
    with open('tip4p.pdb', 'w') as f:
        for i in range(int(np.floor(len(mw)/3))):
            # 定义变量count_1为i除以9999的余数
            count_1 = i%9999

            # 根据氧原子位置，及氢原子位置，计算虚拟点坐标
            # 氧原子坐标
            o_cord = np.array([mw[3*i,0],mw[3*i,1],mw[3*i,2]])
            # 氢原子坐标
            h1_cord = np.array([mw[3*i+1,0],mw[3*i+1,1],mw[3*i+1,2]])
            h2_cord = np.array([mw[3*i+2,0],mw[3*i+2,1],mw[3*i+2,2]])
            # 虚拟点坐标
            mm_cord = ((h2_cord+h1_cord)/2-o_cord)/np.linalg.norm((h2_cord+h1_cord)/2-o_cord)*0.1577+o_cord

            mm[i,0] = mm_cord[0]
            mm[i,1] = mm_cord[1]
            mm[i,2] = mm_cord[2]
          # f.write('HETATM{:5d}  MW{:3d} MW    1{:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(i+1, i+1, mw[i,0], mw[i,1], mw[i,2]))
            f.write('HETATM{:5d}  O   HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           O \n'.format(4*i+1, count_1+1, mw[3*i,0], mw[3*i,1], mw[3*i,2]))
            f.write('HETATM{:5d}  H1  HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(4*i+2, count_1+1, mw[3*i+1,0], mw[3*i+1,1], mw[3*i+1,2]))
            f.write('HETATM{:5d}  H2  HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           H \n'.format(4*i+3, count_1+1, mw[3*i+2,0], mw[3*i+2,1], mw[3*i+2,2]))
            f.write('HETATM{:5d}  M   HOH A{:4d} {:11.3f}{:8.3f}{:8.3f}  1.00  0.00           M \n'.format(4*i+4, count_1+1, mm[i,0], mm[i,1], mm[i,2]))
        f.write('END\n')    

# 生成tip3p水模型的xyz文件
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
    with open('mw.xyz', 'w') as f:
        # 输出水的个数
        # f.write(str(nx*ny*nz))
        # 输出原子类型数目

        for i in range(nx):
            for j in range(ny):
                for k in range(nz):
                    f.write('{:11.3f}{:8.3f}{:8.3f}\n'.format(i*3.0, j*3.0, k*3.0))

# 主程序
# mw_xyz_1(50,50,50)
tip4pdb()
