import maya.mel as mel
import maya.cmds as cmds
import ast

# import alembic

def import_alembic(groupName, pathFile):


    mel.eval('AbcImport -mode import -reparent "{0}" "{1}";'.format(groupName, pathFile))
    cmds.select
# use extra attribute information to assign material

def assign_material():

    # list all extra attributes

    # {'shd': u'pSphereShape1_blinn1SG_2017170704144259', 'faces': []}
    # {'shd': u'pSphereShape1_phongE1SG_2017170705125735', 'faces': [u'264-270', u'280-359', u'380-399']}

    # {mat001:[faces] , mat002:[faces] }

    mat_att = {}

    for i in cmds.listAttr('pSphereShape1'):
        if i[:3] == 'mat' and i[-3:].isdigit()==True :
            dictionary = cmds.getAttr('pSphereShape1.' + i)
            material = ast.literal_eval(dictionary)
            mat_att[material['shd']] = material['faces']

    print mat_att


