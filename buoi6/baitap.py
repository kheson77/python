
# from dataclasses import dataclass

# @dataclass
# class Product:
#     id: int
#     name: str
    
# @dataclass
# class Inventory:
#     product: Product
    
# @dataclass
# class Item:
#     product: Product
#     quantity: int
    
# @dataclass
# class Cart:
#     cart: list[Item]
#     def addItem(self, obj: Item):
#         self.cart.append(obj)
    
#     def removeItem(self, obj: Item):
#         self.cart.remove(obj)
        
# @dataclass
# class Store:
#     inventory: Inventory
#     cart: Cart

# cart = Cart([Item(Product(1, 'Banh'), 10), Item(Product(2, 'Keo'), 6)])

# def show():
#     print("{:<5} {:<10} {:<10}".format('id', 'name', 'quantity'))
#     print("{:<5} {:<10} {:<10}".format('---', '------', '------', ))
#     for item in cart.cart:
#         print("{:<5} {:<10} {:<10}".format(item.id, item.name, item.quantity))
#     print("{:<5} {:<10} {:<10}".format('---', '------', '------',))
    
# def choose_menu():
#     show()
#     act = input(f"> [A] Add item ~ [R] Remove item ~ (Q) Quit: ")
#     act.lower()
#     if act == "A":
#         id = input('> id: ')
#         name = input('> name: ')
#         quantity = input('> quantity: ')
#         cart.addItem(Product(id, name, quantity))
#         choose_menu()
#     elif act == "R":
#         choose_menu()
#     elif act == "q":
#         exit()
#     else:
#         print('Syntax error.')
#         exit()

# choose_menu()
from datetime import datetime
from tokenize import group

# bai 1
# def timeit(function):

#     def inner_function():
#         before = datetime.now()
#         result = function()
#         after = datetime.now()
#         print('Ham chay mat:', after - before)
#         return result

#     return inner_function


# @timeit
# def my_function():
#     a = 0
#     for i in range(0,1000000):
#         print(i)
#         # a+=i
#     return a

# result = my_function()
# print(result)

# bai 2

# def bold(function):
#     def inner():
#         result = function()
#         result = "<b>" + result + "</b>"
#         return result
    
#     return inner
    
# def italic(function):
#     def inner():
#         result = function()
#         result = "<i>" + result + "</i>"
#         return result
    
#     return inner
    
# def underline(function):
#     def inner():
#         result = function()
#         result = "<u>" + result + "</u>"
#         return result
    
#     return inner

# @bold
# def my_function():
#     string = 'Alo 123456'
#     return string
    
# result = my_function()
# print(result)

# bai regex
log = '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'

n_log = '''83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:43 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:47 +0000] "GET /presentations/logstash-monitorama-2013/plugin/highlight/highlight.js HTTP/1.1" 200 26185 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:12 +0000] "GET /presentations/logstash-monitorama-2013/plugin/zoom-js/zoom.js HTTP/1.1" 200 7697 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:07 +0000] "GET /presentations/logstash-monitorama-2013/plugin/notes/notes.js HTTP/1.1" 200 2892 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:34 +0000] "GET /presentations/logstash-monitorama-2013/images/sad-medic.png HTTP/1.1" 200 430406 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:57 +0000] "GET /presentations/logstash-monitorama-2013/css/fonts/Roboto-Bold.ttf HTTP/1.1" 200 38720 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:50 +0000] "GET /presentations/logstash-monitorama-2013/css/fonts/Roboto-Regular.ttf HTTP/1.1" 200 41820 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:24 +0000] "GET /presentations/logstash-monitorama-2013/images/frontend-response-codes.png HTTP/1.1" 200 52878 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:50 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard.png HTTP/1.1" 200 321631 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:46 +0000] "GET /presentations/logstash-monitorama-2013/images/Dreamhost_logo.svg HTTP/1.1" 200 2126 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:11 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard2.png HTTP/1.1" 200 394967 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:19 +0000] "GET /presentations/logstash-monitorama-2013/images/apache-icon.gif HTTP/1.1" 200 8095 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:33 +0000] "GET /presentations/logstash-monitorama-2013/images/nagios-sms5.png HTTP/1.1" 200 78075 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:00 +0000] "GET /presentations/logstash-monitorama-2013/images/redis.png HTTP/1.1" 200 25230 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:25 +0000] "GET /presentations/logstash-monitorama-2013/images/elasticsearch.png HTTP/1.1" 200 8026 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:59 +0000] "GET /presentations/logstash-monitorama-2013/images/logstashbook.png HTTP/1.1" 200 54662 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:30 +0000] "GET /presentations/logstash-monitorama-2013/images/github-contributions.png HTTP/1.1" 200 34245 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:53 +0000] "GET /presentations/logstash-monitorama-2013/css/print/paper.css HTTP/1.1" 200 4254 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:24 +0000] "GET /presentations/logstash-monitorama-2013/images/1983_delorean_dmc-12-pic-38289.jpeg HTTP/1.1" 200 220562 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:54 +0000] "GET /presentations/logstash-monitorama-2013/images/simple-inputs-filters-outputs.jpg HTTP/1.1" 200 1168622 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:33 +0000] "GET /presentations/logstash-monitorama-2013/images/tiered-outputs-to-inputs.jpg HTTP/1.1" 200 1079983 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:56 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
24.236.252.67 - - [17/May/2015:10:05:40 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0"
93.114.45.13 - - [17/May/2015:10:05:14 +0000] "GET /articles/dynamic-dns-with-dhcp/ HTTP/1.1" 200 18848 "http://www.google.ro/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CCwQFjAB&url=http%3A%2F%2Fwww.semicomplete.com%2Farticles%2Fdynamic-dns-with-dhcp%2F&ei=W88AU4n9HOq60QXbv4GwBg&usg=AFQjCNEF1X4Rs52UYQyLiySTQxa97ozM4g&bvm=bv.61535280,d.d2k" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:04 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/articles/dynamic-dns-with-dhcp/" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:45 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/articles/dynamic-dns-with-dhcp/" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:14 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:17 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/articles/dynamic-dns-with-dhcp/" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:21 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
66.249.73.135 - - [17/May/2015:10:05:40 +0000] "GET /blog/tags/ipv6 HTTP/1.1" 200 12251 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
50.16.19.13 - - [17/May/2015:10:05:10 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "http://www.semicomplete.com/blog/tags/puppet?flav=rss20" "Tiny Tiny RSS/1.11 (http://tt-rss.org/)"
66.249.73.185 - - [17/May/2015:10:05:37 +0000] "GET / HTTP/1.1" 200 37932 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
110.136.166.128 - - [17/May/2015:10:05:35 +0000] "GET /projects/xdotool/ HTTP/1.1" 200 12292 "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=5&cad=rja&sqi=2&ved=0CFYQFjAE&url=http%3A%2F%2Fwww.semicomplete.com%2Fprojects%2Fxdotool%2F&ei=6cwAU_bRHo6urAeI0YD4Ag&usg=AFQjCNE3V_aCf3-gfNcbS924S6jZ6FqffA&bvm=bv.61535280,d.bmk" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
46.105.14.53 - - [17/May/2015:10:05:03 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "-" "UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/"
110.136.166.128 - - [17/May/2015:10:05:06 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
110.136.166.128 - - [17/May/2015:10:05:03 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
110.136.166.128 - - [17/May/2015:10:05:41 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
110.136.166.128 - - [17/May/2015:10:05:32 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
123.125.71.35 - - [17/May/2015:10:05:46 +0000] "GET /blog/tags/release HTTP/1.1" 200 40693 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
110.136.166.128 - - [17/May/2015:10:05:08 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
50.150.204.184 - - [17/May/2015:10:05:46 +0000] "GET /images/googledotcom.png HTTP/1.1" 200 65748 "http://www.google.com/search?q=https//:google.com&source=lnms&tbm=isch&sa=X&ei=4-r8UvDrKZOgkQe7x4CICw&ved=0CAkQ_AUoAA&biw=320&bih=441" "Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; LG-MS770 Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
207.241.237.225 - - [17/May/2015:10:05:58 +0000] "GET /blog/tags/examples HTTP/1.0" 200 9208 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
200.49.190.101 - - [17/May/2015:10:05:36 +0000] "GET /reset.css HTTP/1.1" 200 1015 "-" "-"
200.49.190.100 - - [17/May/2015:10:05:38 +0000] "GET /blog/tags/web HTTP/1.1" 200 44019 "-" "QS304 Profile/MIDP-2.0 Configuration/CLDC-1.1"
200.49.190.101 - - [17/May/2015:10:05:11 +0000] "GET /style2.css HTTP/1.1" 200 4877 "-" "-"
200.49.190.101 - - [17/May/2015:10:05:37 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "-" "QS304 Profile/MIDP-2.0 Configuration/CLDC-1.1"
66.249.73.185 - - [17/May/2015:10:05:00 +0000] "GET /reset.css HTTP/1.1" 200 1015 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.73.135 - - [17/May/2015:10:05:16 +0000] "GET /blog/tags/munin HTTP/1.1" 200 9746 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.73.135 - - [17/May/2015:10:05:33 +0000] "GET /blog/tags/firefox?flav=rss20 HTTP/1.1" 200 16021 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.73.135 - - [17/May/2015:10:05:17 +0000] "GET /blog/geekery/eventdb-ideas.html HTTP/1.1" 200 11418 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
67.214.178.190 - - [17/May/2015:10:05:48 +0000] "GET / HTTP/1.0" 200 37932 "http://www.semicomplete.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:21.0) Gecko/20100101 Firefox/21.0"
67.214.178.190 - - [17/May/2015:10:05:18 +0000] "GET /blog/geekery/installing-windows-8-consumer-preview.html HTTP/1.0" 200 8948 "http://www.semicomplete.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:21.0) Gecko/20100101 Firefox/21.0"
207.241.237.220 - - [17/May/2015:10:05:28 +0000] "GET /blog/tags/projects HTTP/1.0" 200 28370 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
46.105.14.53 - - [17/May/2015:10:05:44 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "-" "UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/"
207.241.237.227 - - [17/May/2015:10:05:47 +0000] "GET /blog/geekery/soekris-gpio.html HTTP/1.0" 200 9587 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
91.177.205.119 - - [17/May/2015:10:05:22 +0000] "GET /blog/geekery/xvfb-firefox.html HTTP/1.1" 200 10975 "http://en.wikipedia.org/wiki/Xvfb" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
91.177.205.119 - - [17/May/2015:10:05:34 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://semicomplete.com/blog/geekery/xvfb-firefox.html" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
91.177.205.119 - - [17/May/2015:10:05:37 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://semicomplete.com/blog/geekery/xvfb-firefox.html" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
91.177.205.119 - - [17/May/2015:10:05:54 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://semicomplete.com/blog/geekery/xvfb-firefox.html" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
91.177.205.119 - - [17/May/2015:10:05:31 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://semicomplete.com/blog/geekery/xvfb-firefox.html" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
91.177.205.119 - - [17/May/2015:10:05:32 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/6.0)"
66.249.73.185 - - [17/May/2015:10:05:22 +0000] "GET /doc/index.html?org/elasticsearch/action/search/SearchResponse.html HTTP/1.1" 404 294 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
207.241.237.228 - - [17/May/2015:10:05:40 +0000] "GET /blog/tags/defcon HTTP/1.0" 200 24142 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
207.241.237.101 - - [17/May/2015:10:05:51 +0000] "GET /blog/tags/regex HTTP/1.0" 200 14888 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
87.169.99.232 - - [17/May/2015:10:05:59 +0000] "GET /presentations/puppet-at-loggly/puppet-at-loggly.pdf.html HTTP/1.1" 200 24747 "https://www.google.de/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
209.85.238.199 - - [17/May/2015:10:05:30 +0000] "GET /blog/tags/firefox?flav=rss20 HTTP/1.1" 200 16021 "-" "Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 3 subscribers; feed-id=14171215010336145331)"
209.85.238.199 - - [17/May/2015:10:05:15 +0000] "GET /test.xml HTTP/1.1" 200 1370 "-" "Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 1 subscribers; feed-id=11390274670024826467)"
81.220.24.207 - - [17/May/2015:10:05:13 +0000] "GET /blog/geekery/ssl-latency.html HTTP/1.1" 200 17147 "http://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=5&ved=0CE4QFjAE&url=http%3A%2F%2Fwww.semicomplete.com%2Fblog%2Fgeekery%2Fssl-latency.html&ei=ZdEAU9mGGuWX1AW09IDoBw&usg=AFQjCNHw6zioJpizqX8Q0YpKKaF4zdCSEg&bvm=bv.61535280,d.d2k" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
81.220.24.207 - - [17/May/2015:10:05:44 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/blog/geekery/ssl-latency.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
81.220.24.207 - - [17/May/2015:10:05:26 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/blog/geekery/ssl-latency.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
81.220.24.207 - - [17/May/2015:10:05:39 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/blog/geekery/ssl-latency.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
81.220.24.207 - - [17/May/2015:10:05:52 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/blog/geekery/ssl-latency.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
81.220.24.207 - - [17/May/2015:10:05:21 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "http://www.semicomplete.com/blog/geekery/ssl-latency.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
66.249.73.135 - - [17/May/2015:11:05:17 +0000] "GET /blog/geekery/vmware-cpu-performance.html HTTP/1.1" 200 12908 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
46.105.14.53 - - [17/May/2015:11:05:42 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "-" "UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/"
218.30.103.62 - - [17/May/2015:11:05:11 +0000] "GET /robots.txt HTTP/1.1" 200 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
218.30.103.62 - - [17/May/2015:11:05:46 +0000] "GET /robots.txt HTTP/1.1" 200 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
218.30.103.62 - - [17/May/2015:11:05:45 +0000] "GET /projects/fex/ HTTP/1.1" 200 14352 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
74.125.40.20 - - [17/May/2015:11:05:59 +0000] "GET /?flav=rss20 HTTP/1.1" 200 29941 "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"
71.212.224.97 - - [17/May/2015:11:05:05 +0000] "GET /projects/xdotool/ HTTP/1.1" 200 12292 "http://suckless.org/rocks" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
71.212.224.97 - - [17/May/2015:11:05:15 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
71.212.224.97 - - [17/May/2015:11:05:22 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
71.212.224.97 - - [17/May/2015:11:05:11 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
71.212.224.97 - - [17/May/2015:11:05:28 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
108.174.55.234 - - [17/May/2015:11:05:26 +0000] "GET /?flav=rss20 HTTP/1.1" 200 29941 "-" "-"
218.30.103.62 - - [17/May/2015:11:05:37 +0000] "GET /blog/geekery/c-vs-python-bdb.html HTTP/1.1" 200 11388 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
121.107.188.202 - - [17/May/2015:11:05:09 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
218.30.103.62 - - [17/May/2015:11:05:39 +0000] "GET /blog/productivity/better-zsh-xterm-title-fix.html HTTP/1.1" 200 10185 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
218.30.103.62 - - [17/May/2015:11:05:11 +0000] "GET /blog/geekery/xvfb-firefox.html HTTP/1.1" 200 10975 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
218.30.103.62 - - [17/May/2015:11:05:00 +0000] "GET /blog/geekery/puppet-facts-into-mcollective.html HTTP/1.1" 200 9872 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
198.46.149.143 - - [17/May/2015:11:05:10 +0000] "GET /blog/geekery/disabling-battery-in-ubuntu-vms.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+semicomplete%2Fmain+%28semicomplete.com+-+Jordan+Sissel%29 HTTP/1.1" 200 9316 "-" "Tiny Tiny RSS/1.11 (http://tt-rss.org/)"
198.46.149.143 - - [17/May/2015:11:05:48 +0000] "GET /blog/geekery/solving-good-or-bad-problems.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+semicomplete%2Fmain+%28semicomplete.com+-+Jordan+Sissel%29 HTTP/1.1" 200 10756 "-" "Tiny Tiny RSS/1.11 (http://tt-rss.org/)"
218.30.103.62 - - [17/May/2015:11:05:28 +0000] "GET /blog/geekery/jquery-interface-puffer.html%20target= HTTP/1.1" 200 202 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
218.30.103.62 - - [17/May/2015:11:05:05 +0000] "GET /blog/geekery/ec2-reserved-vs-ondemand.html HTTP/1.1" 200 11834 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
66.249.73.135 - - [17/May/2015:11:05:31 +0000] "GET /blog/web/firefox-scrolling-fix.html HTTP/1.1" 200 8956 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
86.1.76.62 - - [17/May/2015:11:05:36 +0000] "GET /projects/xdotool/ HTTP/1.1" 200 12292 "http://www.haskell.org/haskellwiki/Xmonad/Frequently_asked_questions" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
86.1.76.62 - - [17/May/2015:11:05:25 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
86.1.76.62 - - [17/May/2015:11:05:19 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
86.1.76.62 - - [17/May/2015:11:05:03 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
86.1.76.62 - - [17/May/2015:11:05:28 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/projects/xdotool/" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
86.1.76.62 - - [17/May/2015:11:05:07 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0"
66.249.73.135 - - [17/May/2015:11:05:58 +0000] "GET /blog/tags/bdb HTTP/1.1" 200 23099 "-" "DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
107.170.41.69 - - [17/May/2015:11:05:31 +0000] "GET /?flav=atom HTTP/1.1" 200 32352 "-" "Feedbin - 1 subscribers"
50.16.19.13 - - [17/May/2015:11:05:14 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "http://www.semicomplete.com/blog/tags/puppet?flav=rss20" "Tiny Tiny RSS/1.11 (http://tt-rss.org/)"
46.105.14.53 - - [17/May/2015:11:05:02 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "-" "UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/"
208.115.111.72 - - [17/May/2015:11:05:26 +0000] "GET /blog/rants/fedora-yum.html HTTP/1.1" 200 8328 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:32 +0000] "GET /blog/tags/grok HTTP/1.1" 200 30346 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:12 +0000] "GET /blog/tags/is%20it%20done%20yet HTTP/1.1" 200 10544 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:07 +0000] "GET /blog/tags/statistics HTTP/1.1" 200 29706 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
50.180.79.170 - - [17/May/2015:11:05:50 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:16.0) Gecko/20100101 Firefox/16.0"
208.115.111.72 - - [17/May/2015:11:05:05 +0000] "GET /blog/tags/subversion HTTP/1.1" 200 12557 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:52 +0000] "GET /blog/web/194.html HTTP/1.1" 200 8251 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:23 +0000] "GET /files/blogposts/20070901/?C=D;O=A HTTP/1.1" 200 980 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:15 +0000] "GET /files/blogposts/20080109/boost_xpressive_test.cpp HTTP/1.1" 200 1533 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:38 +0000] "GET /files/blogposts/20090520/ HTTP/1.1" 200 966 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:41 +0000] "GET /files/fastsplit/?C=M;O=D HTTP/1.1" 200 958 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:19 +0000] "GET /files/xdotool/docs/man/?C=M;O=D HTTP/1.1" 200 959 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:16 +0000] "GET /scripts/python/wrap/?C=N;O=D HTTP/1.1" 200 2631 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:32 +0000] "GET /files/images/?C=S;O=D HTTP/1.1" 200 944 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:00 +0000] "GET /files/blogposts/20080611/ HTTP/1.1" 200 1175 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:16 +0000] "GET /files/logstash/?C=D;O=D HTTP/1.1" 200 13316 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:53 +0000] "GET /presentations/hackday06/ HTTP/1.1" 200 6719 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:29 +0000] "GET /scripts/grok-py-test/ HTTP/1.1" 200 2362 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:08 +0000] "GET /?N=A&page=21 HTTP/1.1" 200 33514 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:49 +0000] "GET /blog/geekery/oniguruma-named-capture-example.html?commentlimit=0 HTTP/1.1" 200 9208 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:01 +0000] "GET /blog/geekery/ssh-key-invalid-hack.html?commentlimit=0 HTTP/1.1" 200 9335 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:31 +0000] "GET /blog/geekery/server-side-javascript.html HTTP/1.1" 200 8587 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
208.115.111.72 - - [17/May/2015:11:05:15 +0000] "GET /blog/geekery/yahoo-hackday-08.html HTTP/1.1" 200 9882 "-" "Mozilla/5.0 (compatible; Ezooms/1.0; help@moz.com)"
105.235.130.196 - - [17/May/2015:11:05:01 +0000] "GET /images/googledotcom.png HTTP/1.1" 200 65748 "-" "Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-S5282 Build/JZO54K)"
174.37.205.76 - - [17/May/2015:11:05:19 +0000] "GET /blog HTTP/1.1" 200 37936 "-" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19; aggregator:Spinn3r (Spinn3r 3.1); http://spinn3r.com/robot) Gecko/2010040121 Firefox/3.0.19"
54.255.13.204 - - [17/May/2015:11:05:03 +0000] "GET /articles/ssh-security/ HTTP/1.1" 200 16543 "http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&sqi=2&ved=0CCQQFjAA&url=http%3A%2F%2Fwww.semicomplete.com%2Farticles%2Fssh-security%2F&ei=vdMAU8LgLcPorQfR9oHwDQ&usg=AFQjCNHWyA_svkWgk70ovEbZidQhlAC84w&bvm=bv.61535280,d.bmk&cad=rja" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"
105.235.130.196 - - [17/May/2015:11:05:45 +0000] "GET /blog/tags/X11 HTTP/1.1" 200 32742 "-" "Mozilla/5.0 (Linux; Android 4.1.2; GT-S5282 Build/JZO54K) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Mobile Safari/537.31"
54.255.13.204 - - [17/May/2015:11:05:55 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/articles/ssh-security/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"
54.255.13.204 - - [17/May/2015:11:05:32 +0000] "GET /style2.css HTTP/1.1" 200 4877 "http://www.semicomplete.com/articles/ssh-security/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"
54.255.13.204 - - [17/May/2015:11:05:10 +0000] "GET /favicon.ico HTTP/1.1" 200 3638 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"
105.235.130.196 - - [17/May/2015:11:05:20 +0000] "GET /reset.css HTTP/1.1" 200 1015 "http://www.semicomplete.com/blog/tags/X11" "Mozilla/5.0 (Linux; Android 4.1.2; GT-S5282 Build/JZO54K) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Mobile Safari/537.31"
54.255.13.204 - - [17/May/2015:11:05:46 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/articles/ssh-security/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"
54.255.13.204 - - [17/May/2015:11:05:17 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:27.0) Gecko/20100101 Firefox/27.0"'''

pattern = "^(\d{1,3}.{1}\d{1,3}.{1}\d{1,3}.{1}\d{1,3})"

import re

f = open('regex.txt', 'r')
content = f.read()

a = re.findall(pattern, content)
# b = []
# c = []
# for i in range(len(a)-1): 
#     b.append(a.count(a[i]))
    
# print(b)

# for i in range(len(b)-1):
#     if b[i] == max(b):
#         c.append(a[i])
        
# print(c)

print(a)