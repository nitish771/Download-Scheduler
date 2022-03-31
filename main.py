import os
import datetime as dt
import pytz
import time
import requests
import urllib.request



class Link:
    def __init__(self, link, time=None, save_to='~/Downloads', save_as=None):
        self.link = link
        self.save_to = save_to
        self.save_as = save_as
        self.time = time
    

class Downloader:
    def __init__(self, save_to='~/Downloads'):
        self.save_to = save_to
        self.dl_queues = []

    def _get_time(self):
        '''Returns datetime.now() object'''
        return dt.datetime.now(tz=pytz.timezone('Asia/Kolkata'))

    def _is_binge_time(self):
        cur_time = self._get_time()
        if cur_time.hour > 6 and cur_time.hour <= 23:
            return False        
        if cur_time.hour == 5 and cur_time.minute > 50:
            return False
        return True

    def _is_time(self, hour):
        cur_time = self._get_time()
        if cur_time.hour >= hour and cur_time.hour <= hour:
            return True

    def _default_loc(self, loc):
        self.save_to = loc

    def add(self):
        '''Args
            1st -> link
            2nd -> name
            3rd -> save_to
            4th -> time
        '''
        print("Enter your links in given format\n link [save_as] [save_to] [time]\n")
        while 1:
            link_info = input().split(' ')
            if link_info[0] == '':
                return
            self.dl_queues.append(link_info)

    def print_links(self):
        if len(self.dl_queues) == 0:
            print("No Download Schedule yet")
        return
        for link in self.dl_queues:
            print(link)

    def _print_details(self):
        # print('save to ', self._time_remaining())        
        print('save to ', self.save_to)
        print('links queue ', self.dl_queues)
        

    def download(self):
        for link in self.dl_queues:
                # if self._is_time(link[0]):
                # download
                print('Downloading ', link[0])
                dl_cmd = 'wget -c '

                if len(link) == 2:
                    dl_cmd += ' -O ' + link[1]

                if self.save_to:
                    dl_cmd += ' -P ' + self.save_to + ' '
                
                dl_cmd += link[0]
                print(dl_cmd)
                os.system(dl_cmd)
                # self.dl_queues.remove(link)


if __name__ == '__main__':
    dl = Downloader()
    print('1. Print links')
    print('2. Add link')
    print('3. Start Download')
    print('4. Remainig Time')
    print('5. Change default location')
    print('6. Print Downloader details')
    print('7. Empty Queue')

    while 1:
        try:
            opt = int(input(" "))
        except:
            print('Bye Bye!')
            break
        
        if opt == 1:
            dl.print_links()
            print('\n======\n')

        elif opt == 2:
            dl.add()
            print('\n======\n')

        elif opt == 3:
            dl.download()
            print('\n======\n')

        elif opt == 5:
            dl._default_loc(input("Enter Location : "))
            print('\n======\n')
        
        elif opt == 6:
            dl._print_details()
            print('\n======\n')
        
        else:
            print('Wrong options')
            break


# https://su-link.herokuapp.com/dl/45/sample_video.mkv
# https://su-link.herokuapp.com/dl/0/%40OMniMo3.mkv
# 
