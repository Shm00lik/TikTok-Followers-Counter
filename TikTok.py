from selenium import webdriver

username = input("Username: ")

driver = webdriver.Chrome()

driver.get(f"https://livecounts.io/tiktok-realtime/{username}")

oldFollowers = 0

while True:
    followers = int(driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/div/div/div").text.replace('\n', '').replace(',', ''))

    if followers > oldFollowers and (len(str(followers)) == len(str(oldFollowers)) if oldFollowers != 0 else True):

        if oldFollowers == 0:
            print("Starting amount of followers: ", followers)
            
        else:
            print("New Follower. Now: ", followers)

        oldFollowers = followers

    elif followers < oldFollowers:
        oldFollowers = followers
