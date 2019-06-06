#coding = utf-8
'''
    @name:
    @function:
    @author:Mr.Zheng
    @date:'2018-12-12 17:58'
'''
import random
'''

'''
if __name__ == '__main__':
    project = ["bug管理系统","教务管理系统","餐饮管理系统","医院管理系统"]
    group = [1,2,3]
    for i in range(3):
        p_r = random.choice(project)
        g_r = random.choice(group)
        res = "结果:第{0}组 项目{1}".format(g_r, p_r)
        print(res)
        project.remove(p_r)
        group.remove(g_r)
    pass