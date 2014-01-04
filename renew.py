# -*- coding: utf-8 -*-

import urllib, urllib2
import cookielib
# import time

def print_battery(content):
    battery_string = 'Batteries: <script language="Javascript">PrintBatterySpan(); SetBatteryLife('
    pos = content.find(battery_string) + len(battery_string)
    total = int(content[pos : content.find(')', pos)])
    days = int(total / 86400)
    total -= days * 86400
    hours = int(total / 3600)
    total -= hours * 3600
    mins = int(total / 60)
    total -= mins * 60
    print 'Batteries:', str(days) + 'd',
    print '%02d:%02d:%02d' % (hours, mins, total)


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'), ('Referer', 'http://m.newsmth.net/'), ('Host', 'm.newsmth.net')]
urllib2.install_opener(opener)

# Login
f = open('minethings.config')
(usr, pwd) = f.readline().strip().split('\t')
f.close()
post_data = urllib.urlencode({'data[Miner][name]': usr, 'data[Miner][password]': pwd})
req = urllib2.Request('http://www.minethings.com/miners/login', post_data)
conn = urllib2.urlopen(req)

# Find the battery life
print_battery(conn.read())

# Renew
req = urllib2.Request('http://bromo.minethings.com/mines/check_mines')
conn = urllib2.urlopen(req)
# time.sleep(3)

# Ensure the battery life
print_battery(conn.read())
