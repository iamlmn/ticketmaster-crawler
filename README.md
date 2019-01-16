# ticketmaster-crawler

A crawler using ticket-master api architectured to get all the events in US throughout without exceeding the qouta limit.

code(pip install requirements.txt)
*pandas 
*ticketpy==
*cv2

code(python run.py)
> the above script calls the ticketmaster events fetcher using shell commands for different classes within a period of time and also invokes static map image downloader.


code(python ticketmaster_eventsfetcher.py <Class> [start-date] [end-date])
usage-
  
code(python imagedownloader.py)
  >imagedownloader.mapimagedownloader(filename)-downloads all the images(map image url) with the corresponding venue id.
 
 
