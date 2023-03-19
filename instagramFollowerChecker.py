from bs4 import BeautifulSoup

followers = open("followers.html")
following = open("following.html")

followerSoup = BeautifulSoup(followers, "html.parser")
followingSoup = BeautifulSoup(following, "html.parser")

followers_biglist = followerSoup.find_all("a")
following_biglist = followingSoup.find_all("a")

followerNameList = []
followingNameList = []

for person in followers_biglist:
    followerNameList.append(person.text)

for person in following_biglist:
    followingNameList.append(person.text)

for person in followingNameList:
    if person not in followerNameList:
        print(person)

