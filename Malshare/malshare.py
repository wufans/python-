# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:18:36 2018

@author: wufan
# =============================================================================
从malshare.com上按照时间段和文件类型获取malware样本
Thanks to the work of :https://github.com/Bojak4616/Malshare_PE32_Downloader
# =============================================================================
"""
#!/usr/bin/python

from os import listdir, chdir, getcwd, environ
import os
import sys
import argparse
from datetime import date, timedelta
from random import shuffle
import requests

# Add your API-KEY here!!!
os.environ["MAL_KEY"] = ""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dry_run', required=False, dest='dry_run', action='store_true',
                        help='See hashes that would be downloaded')
    parser.add_argument('-dir', '--directory', required=False, dest='directory', default=r"C:\Users\wufan\Desktop\src\data\malware",
                        help='Directory to place malware. Default is CWD')
    parser.add_argument('-c', '--count', required=False, dest='count', default=100,
                        help='Number of malware to download')
    
    return parser.parse_args()

def datespan(startDate, endDate, delta=timedelta(days=1)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

def get_hashes():
    hashes = []
    # you can set your start time and end time(you can get the limitaion  in http://www.malshare.com/daily/)
    for day in datespan(date(2018, 2, 1), date(2018, 3, 1)):
        url = 'http://www.malshare.com/daily/{0}/malshare_fileList.{0}.txt'.format(day.strftime('%Y-%m-%d'))
        try:
            print("[%s] Scraping malware hashes"%url)
            r = requests.get(url)
            hashes += r.content.splitlines()
        except KeyboardInterrupt:
            print('\n'.join(hashes))
            print("[!] Interrupted")
            print("[*] Current scraped hashes")
            sys.exit(0)
        except requests.RequestException as e:
            print(e)
        #break
    #print(hashes)
    # for _ in hashes:
    #     print(_.decode("utf-8"))

    # Shuffling is not optimal, but gets downloading new stuff sooner		
    shuffle(hashes)
    return hashes
    

def dl_mal(directory, hashes, count_max):
    """
    directory:directory to place malware
    hashes:hashes that would be downloaded
    count_max:number of malware to download_define by parser argument
    """
    print("[*] Starting to download malware")

    chdir(directory)    
    files = [_file.rstrip('.exe') for _file in listdir(directory)]
    
    count = 0
    params = {
        'api_key': environ['MAL_KEY']
    }
    
    for _hash in hashes:
        if _hash in files:
            continue

        try:
            params.update({'action': 'details', 'hash': _hash})
            r = requests.get('http://malshare.com/api.php', params=params)
            _json = r.json()
            #print(_json)
            if _json['F_TYPE'] == 'PE32':
                params.update({'action': 'getfile'})
                r = requests.get('http://malshare.com/api.php', params=params)
                #print(r)
                # if 'ERROR!' in r.content:
                #     print("[!] Error: API limit reached for downloads")
                #     break
                with open('{}.exe'.format(_hash.decode("utf-8")), 'wb') as f:
                    print("writing'{}.exe'".format(_hash.decode("utf-8")))
                    f.write(r.content)
                
                count += 1
                #print count
                if count == count_max:
                    break
        except KeyboardInterrupt:
            print("[!] Interrupted")
            print("[!] Last file: {}.exe MAY be corrupted".format(_hash))
            sys.exit(0)
        except requests.RequestException as e:
            print(e)

def main():
    args = parse_args()
    hashes = get_hashes()
    if not args.dry_run:
        dl_mal(args.directory, hashes, args.count) 

    print("[*] All done!")
    sys.exit(0)

if __name__ == '__main__':
    main()
