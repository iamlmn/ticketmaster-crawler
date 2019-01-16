import urllib.request
import pandas as pd
import time
import os
from tqdm import tqdm
import zipfile
#import cv2
global count
count=0
def imagechecker(a,b):
    difference = cv2.subtract(a, b)
    result = not np.any(difference)
    if result is True:
        return 1
    else:
        #cv2.imwrite("ed.jpg", difference )
        return 0

def mapimagedownloader(filename):

    df1=pd.read_csv(filename)
    #print(df1.columns)
    if os.path.isdir('mapimages/sports'):
        pass
    else:
        os.mkdir('mapimages/sports')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(os.path.join(dir_path,"mapimages/sports"))
    li=[]

    def download_image(url,filename):
        #name = random.randrange(1,100)
        fullname = filename
        urllib.request.urlretrieve(url,fullname)
    print('started')
    for i in tqdm(range(len(df1['map img url']))):

        if str(df1['map img url'].iloc[i]) != 'nan':
      #      try:
            try:
                format_file=str(df1['Venue Id'].iloc[i])+str(df1['map img url'].iloc[i])[-4:]
                '''if os.path.isfile('//'+str(format_file)):

                    if imagechecker(format_file,download_image(str(df1['map img url'].iloc[i]),format_file)):
                        pass
                    else:
                        format_file=str(df1['Venue Id'].iloc[i])+str(i)+str(df1['map img url'].iloc[i])[-4:]
                '''
                #print(str(df1['map img url'].iloc[i]))
                if (os.path.isfile('mapimages/sports/'+str(format_file)))==False:
                    
                    download_image(str(df1['map img url'].iloc[i]),format_file)
                    global count
                    count+=1
                
                #time.sleep(0.1)
            except Exception as e:
                print(e,'Skipped:',format_file,df1['map img url'].iloc[i])
                pass

    zf = zipfile.ZipFile("mapimages.zip", "w")

    for dirname, subdirs, files in os.walk("mapimages\\"):
    	zf.write(dirname)
    	for filename in files:
    	   zf.write(os.path.join(dirname, filename))

    zf.close()
    '''def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('C:\Crawlingstubhub\TicketCrawler-master-new\TicketCrawler-master\mapimages\\', zipf)
    zipf.close()
        '''

if __name__=='__main__':
    mapimagedownloader('ticketmaster_2019-sports.csv')
    print(count,'static seat maps downloaded')
