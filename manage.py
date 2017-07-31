__author__ = 'kidozh'
# -*- coding: UTF-8 -*-
import os
from conf import ENVIRONMENT_VARIABLE
os.environ[ENVIRONMENT_VARIABLE] = 'setting'

from contrib.admin.appModel import modelFinder
from db import database

import sys

if len(sys.argv) != 2:
    print('''Only one argv is supported''')
else:
    if sys.argv[1] == 'migrate':
        modelsFinder = modelFinder()
        # a tuple containing three element : app,className,class
        modelsList = modelsFinder.getInstalledModel()
        models = [model for name,package in modelsList for dname,model in package if model!= []]
        print 'These models are searched : ', models
        print database.create_tables(models,safe=True)
    elif sys.argv[1] == 'createsuperuser':
        from db import database
        from contrib.admin.models import admin

        database.connect()
        try:
            database.create_tables([admin])
        except:
            pass
        print '''  TJANGO Create administrator '''

        username = raw_input('Please input your username : ')
        password = raw_input('Please input your password : ')
        new_adminUser = admin(username=username, password=password,isStaff=True,isAdmin=True)
        new_adminUser.save()
    else :
        print '''
        Currently, only 'migrate' and 'createsuperuser' is supported
        '''
        print 'Your argv  is : %s' % sys.argv[1]