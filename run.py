import datetime
from subprocess import call
#import ticketmaster_eventsfetcher
import os

if __name__=='__main__':
    classifiler_list=['Family','Film','Arts','Concerts','Sports','Music','Miscellaneous']
    for classifier in classifiler_list:

        try:
            call(['python','ticketmaster_eventsfetcher.py', str(classifier) ,'2019-01-14T00:00:00Z', '2019-01-20T23:59:00Z','jan1'],shell=True)
        #exec(ticketmaster_eventsfetcher)
        #call("python ticketmaster_eventsfetcher.py 'Music' '2019-01-10T00:00:00Z' '2019-01-15T23:59:00Z'",shell=True)
        #EventFiner('Music','2019-01-10T00:00:00Z','2019-01-15T23:59:00Z')
        #os.system("python ticketmaster_eventsfetcher.py 'Music' '2019-01-10T00:00:00Z' '2019-01-15T23:59:00Z' ")
        except:
            print('Jan skipped')
        try:
            call(['python','ticketmaster_eventsfetcher.py', str(classifier) ,'2019-01-20T00:00:00Z', '2019-01-31T23:59:00Z','jan2'],shell=True)
        #exec(ticketmaster_eventsfetcher)
        #call("python ticketmaster_eventsfetcher.py 'Music' '2019-01-10T00:00:00Z' '2019-01-15T23:59:00Z'",shell=True)
        #EventFiner('Music','2019-01-10T00:00:00Z','2019-01-15T23:59:00Z')
        #os.system("python ticketmaster_eventsfetcher.py 'Music' '2019-01-10T00:00:00Z' '2019-01-15T23:59:00Z' ")
        except:
            print('Jan skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier) ,'2019-02-01T00:00:00Z' ,'2019-02-14T23:59:00Z','Feb1'],shell=True)
        except:
            print('feb1 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier) ,'2019-02-14T00:00:00Z' ,'2019-02-21T23:59:00Z','Feb2'],shell=True)
        except:
            print('feb2 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier) ,'2019-02-21T00:00:00Z' ,'2019-02-28T23:59:00Z','Feb3'],shell=True)
        except:
            print('feb3 skipped')

        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-03-01T00:00:00Z' ,'2019-03-10T23:59:00Z','Mar1'],shell=True)
        except:
            print('mar1 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-03-10T00:00:00Z' ,'2019-03-20T23:59:00Z','Mar2'],shell=True)
        except:
            print('mar2 skipped')

        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-03-20T00:00:00Z' ,'2019-03-31T23:59:00Z','Mar3'],shell=True)
        except:
            print('mar3 skipped')


        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-04-01T00:00:00Z' ,'2019-04-10T23:59:00Z','Apr1'],shell=True)
        except:
            print('apr1 skipped')

        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-04-10T00:00:00Z' ,'2019-04-20T23:59:00Z','Apr2'],shell=True)
        except:
            print('apr2 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-04-20T00:00:00Z' ,'2019-04-30T23:59:00Z','Apr3'],shell=True)
        except:
            print('apr3 skipped')

        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-05-01T00:00:00Z', '2019-05-10T23:59:00Z','May1'],shell=True)
        except:
            print('may1 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-05-10T00:00:00Z', '2019-05-20T23:59:00Z','May2'],shell=True)
        except:
            print('may2 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-05-21T00:00:00Z', '2019-05-31T23:59:00Z','May3'],shell=True)
        except:
            print('may3 skipped')

        '''try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-06-01T00:00:00Z' ,'2019-06-10T23:59:00Z','June1'],shell=True)
        except:
            print('June1 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-06-10T00:00:00Z' ,'2019-06-20T23:59:00Z','June2'],shell=True)
        except:
            print('June2 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py' ,str(classifier), '2019-06-20T00:00:00Z' ,'2019-06-30T23:59:00Z','June3'],shell=True)
        except:
            print('June3 skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier) ,'2019-07-01T00:00:00Z','2019-07-10T23:59:00Z','July1'],shell=True)
        except:
            print('July skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier) ,'2019-07-10T00:00:00Z','2019-07-20T23:59:00Z','July2'],shell=True)
        except:
            print('July skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier) ,'2019-07-21T00:00:00Z','2019-07-31T23:59:00Z','July3'],shell=True)
        except:
            print('July skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-08-01T00:00:00Z' ,'2019-08-10T23:59:00Z','Aug1'],shell=True)
        except:
            print('Aug skipped')

        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-08-10T00:00:00Z' ,'2019-08-21T23:59:00Z','Aug2'],shell=True)
        except:
            print('Aug skipped')
        try:
            call(["python", 'ticketmaster_eventsfetcher.py', str(classifier), '2019-08-21T00:00:00Z' ,'2019-08-31T23:59:00Z','Aug3'],shell=True)
        except:
            print('Aug skipped')'''
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-09-01T00:00:00Z' ,'2019-09-10T23:59:00Z','Sep1'],shell=True)
        except:
            print('sep skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-09-10T00:00:00Z' ,'2019-09-20T23:59:00Z','Sep2'],shell=True)
        except:
            print('sep2 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-09-20T00:00:00Z' ,'2019-09-30T23:59:00Z','Sep3'],shell=True)
        except:
            print('sep3 skipped')

        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier), '2019-10-01T00:00:00Z' ,'2019-10-10T23:59:00Z','Oct1'],shell=True)
        except:
            print('Oct1 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier), '2019-10-11T00:00:00Z' ,'2019-10-20T23:59:00Z','Oct2'],shell=True)
        except:
            print('Oct2 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier), '2019-10-21T00:00:00Z' ,'2019-10-31T23:59:00Z','Oct3'],shell=True)
        except:
            print('Oct3 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-11-01T00:00:00Z' ,'2019-11-10T23:59:00Z','Nov1'],shell=True)
        except:
            print('Nov1 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-11-11T00:00:00Z' ,'2019-11-20T23:59:00Z','Nov2'],shell=True)
        except:
            print('Nov2 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-11-21T00:00:00Z' ,'2019-11-30T23:59:00Z','Nov3'],shell=True)
        except:
            print('Nov3 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-12-01T00:00:00Z', '2019-12-31T23:59:00Z','Dec'],shell=True)
        except:
            print('Dec1 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-12-01T00:00:00Z', '2019-12-31T23:59:00Z','Dec'],shell=True)
        except:
            print('Dec2 skipped')
        try:
            call(["python", "ticketmaster_eventsfetcher.py", str(classifier) ,'2019-12-01T00:00:00Z', '2019-12-31T23:59:00Z','Dec'],shell=True)
        except:
            print('Dec3 skipped')
