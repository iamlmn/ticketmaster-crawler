
"""Welcome to the ticket master data crawler .

Usage:
  ticketmaster_events <classifier> [startdate] [enddate]
  Classifier ('Music' or 'Sports' etc)
  Start Date (by default todays date)
  End date  (by default current month end)
  commands.py -h | --help
  date format -YYYY-MM-DDTHH:MM:SSZ (2019-01-01T20:00:00Z)
Options:
  -h --help     Show this screen.
 """
import ticketpy
import pandas as pd
from tqdm import tqdm
import sys
#import argparse
from docopt import docopt
import time
import os
import logging
#arguments = docopt(__doc__)


'''parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
goodbye_parser = subparsers.add_parser('goodbye')
'''


#StartDate=input('Enter the start date (2019-01-01T20:00:00Z):')
#EndDate=input('Enter the End date (2019-01-01T20:00:00Z):')

#df=pd.read_excel("Zipcodes_US.xlsx",sheet_name='Statecode')


'''venues = tm_client.venues.find(utc_datetime='2019-03-01T23:00:00Z').one()
print(type(venues))
callable(venues[0])
len(venues)
for v in venues:
    print("Name: {} / Id:{} / City: {} / url: {} / timezone : {} / address: {} /Location :{} /social : {} ".format(v.name,v.id,v.city, v.url,v.timezone,v.address,v.location,v.social))
'''
#print(list(statecodes))
def EventFiner(classifier,start_date,end_date,mon):

    df=pd.DataFrame(columns=['Event Id','Event name','Start date(local)','Start time(local','Ticket Status','links','Price Range','Genre Segment','Genre','Sub-genre','Classification Type','Classification Subtype'
                     ,'Venue Id','Venue name','Venue URL','Venue Time Zone','Venue Address','Venue City','Venue Postal Code','Venue Location','Venue State Code',
                     'Venue Lat','Venue Long','Social Links','Market Ids'])
    for states in tqdm(statecodes):
        try:
            pages = tm_client.events.find(
                classification_name=classifier,
                state_code=states,
                start_date_time=str(start_date),
                end_date_time=str(end_date)
            )
        except:
            print('Skipping Event from the state {} , Limit exceeded(Try giving the dates more stringent)'.format(states))
            continue
        for page in pages:
            for x in page:
                #print(x.name)
                li=[x.id,x.name,x.local_start_date,x.local_start_time,x.status,x.price_ranges,x.links['self'],str(x.classifications[0].segment),str(x.classifications[0].genre),str(x.classifications[0].subgenre),str(x.classifications[0].type),str(x.classifications[0].subtype),str(x.venues[0].id),str(x.venues[0].name),str(x.venues[0].url),str(x.venues[0].timezone),str(x.venues[0].address),str(x.venues[0].city),str(x.venues[0].postal_code),str(x.venues[0].location),str(x.venues[0].location['state_code']),str(x.venues[0].location['latitude']),str(x.venues[0].location['longitude']),str(x.venues[0].social),str(x.venues[0].markets)]
                head=['Event Id','Event name','Start date(local)','Start time(local','Ticket Status','links','Price Range','Genre Segment','Genre','Sub-genre','Classification Type','Classification Subtype'
                                 ,'Venue Id','Venue name','Venue URL','Venue Time Zone','Venue Address','Venue City','Venue Postal Code','Venue Location','Venue State Code',
                                 'Venue Lat','Venue Long','Social Links','Market Ids','Static/Dynamic map','map img url','URL3','Performer name','header image','promoters name','promoter name','event-description','ticket-limit','boxoffice-ph-no','boxoffice-openhoursDetail','accepted-paymeny-detail','venue parking details','attraction name']
                try:
                    li.append(list(x.json['seatmap'].keys())[0])
                except:
                    li.append('NA')
                try:
                    li.append(list(x.json['seatmap'].values())[0])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['url'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['name'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['images'][0]['url'])
                except:
                    li.append('NA')
                    #print(x.json['ticketLimit']['info'])
                try:
                    li.append(x.json['promoters'][0]['name'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['promoter']['name'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['promoter']['description'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['ticketLimit']['info'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['_embedded']['venues'][0]['boxOfficeInfo']['phoneNumberDetail'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['_embedded']['venues'][0]['boxOfficeInfo']['openHoursDetail'])
                except:

                    li.append('NA')
                try:
                    li.append(x.json['_embedded']['venues'][0]['boxOfficeInfo']['acceptedPaymentDetail'])
                except:
                    li.append('NA')
                try:
                    li.append(x.json['_embedded']['venues'][0]['parkingDetail'])
                except:
                    li.append('NA')
                    #Attractions
                try:
                    li.append(x.json['_embedded']['attractions'][0]['name'])
                except:
                    li.append('NA')
                df=df.append(pd.Series(li,head),ignore_index=True)

        time.sleep(1)

    df.to_csv('TicketMaster_'+classifier+'_data_'+str(mon)+'.csv')

def data_cleansing(classifier,startdate,enddate):
    '''
        Data cleaning code

    '''
def validate_args(**kwargs):
    classifiler_list=['Music','Sports','Family','Miscellaneous','Arts & Theater','Concerts','Film']
    '''
    Method to validate classifier & date

    '''

if __name__=='__main__':

    #args = parser.parse_args()
    api_key='A7Vk7p59KexOjt3e7exhBG47AcnkiC9T'
    tm_client = ticketpy.ApiClient(api_key)
    #classifier=input('Hey enter the class of ticket you want:')
    #State Code to run thru every states event in the given time period
    statecodes=['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND'
        , 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'PR']
    #EventFiner(classifier)
    program_name = sys.argv[0]
    args = sys.argv[1:]
    if len(args)==1:
        startdate='2019-01-05T20:00:00Z'
        enddate='2019-01-20T20:00:00Z'
        #startdate=str(gmtime().tm_year)+'-'+str(gmtime().tm_mon)+'-'+str(gmtime().tm_mday)+'T'+'00:00:00Z'
        #enddate=str(gmtime().tm_year)+'-'+str(gmtime().tm_mon)+'-'+str(31)+'T'+'23:59:59Z'

    elif len(args)==2:
        startdate=args[1]
    else:
        startdate=args[1]
        enddate=args[2]
    mon=args[3]
    #print('Starting' + program_name+'...' )
    #count = len(arguments)
    #Actual
    #EventFiner(arguments[0],arguments[1],arguments[2])
    #print(startdate,enddate)
    EventFiner(args[0],startdate,enddate,mon)
    print('Output has been created for the class {} from date {} to date {}'.format(args[0],startdate,enddate))
