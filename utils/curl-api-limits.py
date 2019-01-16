from subprocess import call

call(["python","curl","-I", 'http://app.ticketmaster.com/discovery/v1/events.json?keyword=Queen&apikey=A7Vk7p59KexOjt3e7exhBG47AcnkiC9T'],shell=True)
