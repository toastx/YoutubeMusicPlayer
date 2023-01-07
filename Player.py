from time import sleep
from sys import exit
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from localStoragePy import localStoragePy
#localStorage config
ls = localStoragePy("playlistDatabase","json")

#driver config
options = webdriver.FirefoxOptions()
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
options.add_argument(user_agent)
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.add_argument("--headless")
options.add_argument("--log-level")
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
options.add_argument('--disable-application-cache')
options.add_argument("--disable-dev-shm-usage")
ser = Service("geckodriver.exe")
extension1 = "C://Users//dipu6//Downloads//ublock_origin-1.46.0.xpi"
extension2 = "C://Users//dipu6//Downloads//image_blocker_plus-0.2.0.xpi"
driver = webdriver.Firefox(service=ser,options=options)
driver.install_addon(extension1, temporary=True)
driver.install_addon(extension2, temporary=True)

#functions
#songs
def stream(MusicName):
    MusicName = MusicName
    driver.get(f"https://m.youtube.com/results?search_query={MusicName}")
    driver.implicitly_wait(3)
    video =driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
    video.click()

def pauseAndPlay():
    pauseVideo = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video")
    driver.implicitly_wait(1)
    pauseVideo.click()

def track():
    track = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")
    artist = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a")
    print(f"{track.text} - {artist.text}")

def next():
    next = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/a[2]")
    driver.implicitly_wait(1)
    next.click()

def previous():
    previous = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/a[1]")
    driver.implicitly_wait(1)
    previous.click()


#playlists
def streamPlaylist(playlistName):
    url = ls.getItem(playlistName)

    if url != None:
        driver.get(url)
        driver.implicitly_wait(2.5)
        shuffle = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[2]/ytd-button-renderer[2]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
        shuffle.click()
    else:
        print("playlist not found......")
        print("re enter name properly")

def addPlaylist(name, url):
    ls.setItem(name,url)
    sleep(1)
    print("stored....")

def removePlaylist(playlistName):
    ls.removeItem(playlistName)
    print("removed....")

def stop():
    driver.quit()
    exit(1)


if __name__ == "__main__":
        print("Enter the name of song or choose playlist:")
        while True:
            uinput = str(input())
            if uinput.split(" ",1)[0] == "st":
                songName = uinput.split(" ",1)[1]
                stream(songName)

            elif uinput == "stop":
                stop()

            elif uinput == "play" or uinput == "pause":
                pauseAndPlay()

            elif uinput == "track":
                track()

            elif uinput.split(" ",1)[0] == "pt":
                pName = uinput.split(" ",1)[1]
                streamPlaylist(pName)

            elif uinput.split(" ",1)[0] == 'add':
                url = uinput.split(" ", 1)[1]
                Name = str(input("enter name of playlist:"))
                addPlaylist(Name, url)

            elif uinput.split(" ",1)[0] == "rem":
                name = uinput.split(" ",1)[1]
                removePlaylist(name)

            elif uinput == "next":
                next()

            elif uinput == "prev":
                previous()

            else:
                print("..Invalid Command..")
