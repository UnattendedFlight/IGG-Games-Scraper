import json, os, requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeoptions = Options()
chromeoptions.add_argument("--headless")
chromeoptions.add_argument('--window-size=1200x2900')
chromeoptions.add_argument('--disable-gpu')
chrome_path = r"modules/chromedriver/chromedriver.exe"

testMode = False

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', empty_fill='_', leave_bar=True):
    # Get Percentage based on iteration of total iterations
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    # Calculate the length of filler.
    filledLength = int(length * iteration // total)
    # Create the bar based on filled length. E.g █████_____ = 50%
    bar = fill * filledLength + empty_fill * (length - filledLength)
    # Print bar
    print('\r%s | %s%% |%s|  %s                                   ' % (prefix, percent, bar, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        if leave_bar:
            print('\r%s | %s%% |%s|  %s                                        ' % (prefix, percent, bar, suffix))
        else:
            print('\r                                                          ', end = '\r')
def main():
    print("Please enter link:")
    chosen = False
    igglink = ""
    while not chosen:
        igglink = input()
        if "http://igg-games.com" in igglink:
            chosen = True
            break;
        print("Not a valid IGG link.")
    # Fake userclient to bypass some botting-filters
    req = Request(igglink, headers={'User-Agent': 'Mozilla/5.0'})
    # Open page to read
    page = urlopen(req).read()
    # Read page
    soup = BeautifulSoup(page, "html.parser")

    ### Unbelievably filthy setup of variables, but fuck you I do what i want ###
    mega = {}                                                                   #
    openl = {}                                                                  #
    kuba = {}                                                                   #
    uf = {}                                                                     #
    fcdn = {}                                                                   #
    g4u = {}                                                                    #
    ul = {}                                                                     #
    utb = {}                                                                    #
    gd = {}                                                                     #
                                                                                #
    mega1 = {}                                                                  #
    openl1 = {}                                                                 #
    kuba1 = {}                                                                  #
    uf1 = {}                                                                    #
    fcdn1 = {}                                                                  #
    g4u1 = {}                                                                   #
    ul1 = {}                                                                    #
    utb1 = {}                                                                   #
    gd1 = {}                                                                    #
                                                                                #
    mega2 = {}                                                                  #
    openl2 = {}                                                                 #
    kuba2 = {}                                                                  #
    uf2 = {}                                                                    #
    fcdn2 = {}                                                                  #
    g4u2 = {}                                                                   #
    ul2 = {}                                                                    #
    utb2 = {}                                                                   #
    gd2 = {}                                                                    #
    #############################################################################
    ################################ Random shit ################################
    #############################################################################
    links = {}

    providersDict = { # Different available services.
        "Mega.co.nz":mega,
        "Openload.co":openl,
        "KumpulBagi":kuba,
        "UpFile":uf,
        "FileCDN":fcdn,
        "Go4Up (Multi Links)":g4u,
        "Uploaded":ul,
        "Uptobox":utb,
        "Google Drive":gd
    }
    providers = [ # Different available services.
        "Mega.co.nz",
        "Openload.co",
        "KumpulBagi",
        "UpFile",
        "FileCDN",
        "Go4Up (Multi Links)",
        "Uploaded",
        "Uptobox",
        "Google Drive"
    ]
    links = providersDict # Different available services.
    links2 = { # Different available services.
        "Mega.co.nz":mega1,
        "Openload.co":openl1,
        "KumpulBagi":kuba1,
        "UpFile":uf1,
        "FileCDN":fcdn1,
        "Go4Up (Multi Links)":g4u1,
        "Uploaded":ul1,
        "Uptobox":utb1,
        "Google Drive":gd1
    }
    finLinks = { # Different available services.
        "Mega.co.nz":mega2,
        "Openload.co":openl2,
        "KumpulBagi":kuba2,
        "UpFile":uf2,
        "FileCDN":fcdn2,
        "Go4Up (Multi Links)":g4u2,
        "Uploaded":ul2,
        "Uptobox":utb2,
        "Google Drive":gd2
    }

    #############################################################################
    data = soup.findAll('div', attrs={
        'class':'post-content clear-block'
        }) # Don't even use this. lmao

    counter = 0
    availableProviders = []
    ignore = []
    for p in soup.find_all("p"):
        p = str(p)
        b = p[p.find('<b>'):]
        b = b[:b.find('</b>')]
        b = b.replace("<b>Link ", "").replace(":","")
        if b != "":
            # Check if the text near container is "Uploading", because if so, ignore it
            if "Uploading" not in str(p) and b in providers:
                availableProviders.append(providers.index(b))
            elif "Uploading" in str(p) and b in providers:
                ignore.append(providers.index(b))
    # Print available providers for user
    print("Available Providers: ", end='')
    stringProvd = "["
    for each in availableProviders:
        stringProvd += str(each) + "=" + providers[each] + ", "
    stringProvd +="]"
    stringProvd = stringProvd.replace(", ]", "]")
    print(stringProvd)
    # Let user choose what provider they want links for
    print("Which ones would you like to get links for? (Divide with ',' or space)")
    want = input()
    newAvPro = []
    # Remove from abailable that user does not want.
    try:
        want = want.split(" ")
    except:
        try:
            want = want.split(",")
        except Exception as e:
            print(e.args)
            exit(1)
    for each in want:
        each = str(each).replace(" ", "")
        try:
            sel = int(each)
            if sel in availableProviders:
                newAvPro.append(sel)
            else:
                print("%s not in %s" % (str(sel), str(availableProviders)))
        except Exception as e:
            print(e.args)
            exit(2)
    availableProviders = newAvPro

    provider = 0
    curProvider = 0
    print("Gathering links..")
    for div in data:
        # Find all 'a' tags
        soup = div.findAll('a')
        # Read a tags
        for a in soup:
            # Print progress
            printProgressBar(counter, len(soup), length = 30, prefix="Reading..")
            if curProvider in ignore:
                # If provider is unwanted, skip ahead.
                while curProvider in ignore:
                    curProvider += 1
            # If 'part' is in text, it is a link. Save that shit
            if "Part" in a.get_text():
                if a.get_text() not in links[providers[curProvider]]:
                    links[providers[curProvider]][a.get_text()] = a['href']
                else:
                    curProvider += 1
                    if curProvider in ignore:
                        # If provider is unwanted, skip ahead. (again)
                        while curProvider in ignore:
                            curProvider += 1
                    links[providers[curProvider]][a.get_text()] = a['href']
            counter += 1
    printProgressBar(len(soup), len(soup), length = 30, prefix="Nothing to read..", suffix="Complete")
    counter = 1
    print("Launching browser..")
    # driver = webdriver.Chrome(chrome_path, chrome_options=chromeoptions) # Spawns chrom hidden (creates A LOT of errors. fuck that)
    # Spawns chrome
    driver = webdriver.Chrome(chrome_path)
    print("Browser launched..")
    isLoaded=False
    provider = 0
    curProvider = 0
    totalLength = 0
    for provd in availableProviders:
        # Count total of links to pass through
        totalLength += len(links[providers[provd]])
    # Go through all links according to wanted providers.
    for provd in availableProviders:
        for link in links[providers[provd]]:
            if not isLoaded:
                print("Waiting for browser to get ready..")
            # Open page in chrome
            driver.get(links[providers[provd]][link])
            if not isLoaded:
                print("Browser ready!")
                isLoaded = True;
            # Print progress
            printProgressBar(counter, totalLength, length = 30, prefix=providers[provd] + " | " + link)
            # Get the next url, and add it to dictionary
            URL = driver.find_element_by_tag_name('a').get_attribute('href')
            links2[providers[provd]][link] = URL
            counter += 1
    # Go through all links according to wanted providers.
    for provd in availableProviders:
        counter = 1
        isLoaded = False
        for link in links2[providers[provd]]:
            if not isLoaded:
                print("Waiting for browser to get ready..")
            # Open page in chrome
            driver.get(links2[providers[provd]][link])
            if not isLoaded:
                print("Browser ready! Gathering %s links.." % providers[provd])
                isLoaded = True;

            # Execute javascript on page to retrieve the value of FinishMessage which contains the last link and save it to finLinks.
            URL = driver.execute_script("return FinishMessage;")
            URL = URL[URL.find('https'):]
            URL = URL[:URL.find('" >')]
            URL = str(URL).replace('" >', "")
            printProgressBar(counter, len(links2[providers[provd]]), length = 30, prefix=providers[provd] + " | " + link, suffix=URL, decimals=2)
            # print(URL)
            finLinks[providers[provd]][link] = URL
            counter += 1
    # Shut down chrome.
    driver.quit()


    # Dump all info
    if testMode:
        allLinks = {"links1":links, "links2":links2, "links3":finLinks}
        with open('test.json', 'w') as f:
            f.write(json.dumps(allLinks, indent=4))
    with open('out.txt', 'w') as f:
        for provd in availableProviders:
            for each in finLinks[providers[provd]]:
                f.write(finLinks[providers[provd]][each] + "\n")
    with open('test.txt', 'w') as f:
        for provd in providers:
            for each in links[providers[curProvider]]:
                f.write(each + " : " + links[providers[curProvider]][each] + "\n")
            f.write('\n')
            for each in links2[providers[curProvider]]:
                f.write(each + " : " + links2[providers[curProvider]][each] + "\n")
            f.write('\n')
            for each in finLinks[providers[curProvider]]:
                f.write(finLinks[providers[curProvider]][each] + "\n")
if __name__=="__main__":
    main()
