from twitter import tweet
from twitter import search

tweet('cool')
for result in search('@lelBotz'):
    print (result)