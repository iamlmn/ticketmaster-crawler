# ticketmaster-crawler

A crawler using ticket-master api architectured to get all the events in US throughout without exceeding the qouta limit.

### Necessary packages to be installed
* pandas 
* ticketpy
* cv2
* tqdm

### To install the neccessary dependencies, please run the following command.

```pip install requirements.txt```

### To run the crawler, enter the following command in the terminal:
```python run.py```

> the above script calls the ticketmaster events fetcher using shell commands for different classes within a period of time and also invokes static map image downloader.


```python ticketmaster_eventsfetcher.py <Class> [start-date] [end-date] [filename]```
usage-

  > the ticketmaster_eventsfetcher.py script fetches the event,venue and other required details based on the classifier we give like 'Music' or 'Sports' within the start date and end date given as an argument to the program. if start and end date is not mentioned it will take the current date and end date as current months last date.The output will be saved in the same directory in csv formats.
  

```python imagedownloader.py```
  >imagedownloader.mapimagedownloader(filename)-downloads all the images(map image url) with the corresponding venue id.
 
 
To check the qouta limit for the api run the below curl command.

``` curl -I http://app.ticketmaster.com/discovery/v1/events.json?keyword=Queen&apikey=A7Vk7p59KexOjt3e7exhBG47AcnkiC9T ```

