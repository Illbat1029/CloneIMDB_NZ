import base64
import re


from PyQt5.QtGui import QPixmap

from LogicApplication.getFilmsDataFromDB import *


def updateTop10Films(listOfFrames):
    top10Films = getViewFilmDataWhereUserNotLogin()
    for i in range(len(listOfFrames)):
        if i<10:
            actors = ", ".join(top10Films[i].actors)
            actors = re.sub("[\[\']", "", actors)
            actors = re.sub("\]", "", actors)
            listOfFrames[i].setText(actors)
        if i in range(10,20):
            listOfFrames[i].setText(str(top10Films[i-10].description))
        if i in range(20, 30):
            binary_data = base64.b64decode(top10Films[i - 20].images)

            image = QPixmap()
            image.loadFromData(binary_data)

            listOfFrames[i].setPixmap(image)
        if i in range(30,40):
            country = ", ".join(top10Films[i-30].country)
            country = re.sub("[\[\']", "", country)
            country = re.sub("\]", "", country)

            lang = ", ".join(top10Films[i-30].lang)
            lang = re.sub("[\[\']", "", lang)
            lang = re.sub("\]", "", lang)

            genre = ", ".join(top10Films[i-30].genres)
            genre = re.sub("[\[\']", "", genre)
            genre = re.sub("\]", "", genre)


            listOfFrames[i].setText(country + " ("+lang +") "
            ""+" \n"+ genre+" | "+ str(top10Films[i-30].runtime)+" min")
        if i in range(40, 50):
            listOfFrames[i].setText(top10Films[i-40].name+" ("+str(top10Films[i-40].release) + ")")
        if i in range(50, 60):
            listOfFrames[i].setText(str(top10Films[i-50].score))
