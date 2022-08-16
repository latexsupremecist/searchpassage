import json
import codecs
from tkinter import E
from .dict import Dict

class Reader:

    def __init__(self):
        self.chinese = ["CUV", "NCV"]
        self.translation = ""
    
    def my_replace(self, text):
        if self.translation not in self.chinese:
            return text
        return text.replace(" ","")

    def get_translation(self, version):
        f = codecs.open(version,"r",encoding="utf-8-sig")
        self.text = json.load(f)

    def get_book(self, book):
        book = book.lower()
        dictionary = Dict()
        for i in range(len(dictionary.books)):
            if book in dictionary.books[i]:
                self.book = self.text[i]["chapters"]
                return 0
        return 1

    def get_chapter_and_verses(self, location):

        self.text = ""

        if ":" not in location:
            
            if "-" not in location:
            
                chap = int(location) - 1

                try:
                    for i in range(len(self.book[chap])):
                        self.text += f" ({i+1}) "
                        self.text += self.my_replace(self.book[chap][i])
                    return 0
                except:
                    return 1

            chap = location.split("-")
            chap[0] = int(chap[0]) - 1
            chap[1] = int(chap[1]) - 1

            try:
                for i in range(chap[0], chap[1]+1):
                    self.text += f"\n\n[{i+1}]\t"
                    for j in range(len(self.book[i])):
                        self.text += f" ({j+1}) "
                        self.text += self.my_replace(self.book[i][j])
                return 0
            except:
                return 1
        
        if location.count(":") == 1:

            if "-" not in location:
                location = location.split(":")
                try:
                    self.text += self.my_replace(self.book[int(location[0])-1][int(location[1])-1])
                    return 0
                except:
                    return 1

            location = location.split(":")
            chap = int(location[0]) - 1
            location = location[1].split("-")
            versehead = int(location[0]) - 1
            versetail = int(location[1]) - 1

            try:
                for i in range(versehead, versetail+1):
                    self.text += f" ({i+1}) "
                    self.text += self.my_replace(self.book[chap][i])
                return 0
            except:
                return 1

        location = location.split(":")
        chaphead = int(location[0]) - 1
        
        middle = location[1].split("-")

        chaptail = int(middle[1]) - 1
        versehead = int(middle[0]) - 1
        versetail = int(location[2]) - 1

        self.text += f"[{chaphead+1}]\t"

        try:
            for i in range(versehead, len(self.book[chaphead])):
                self.text += f" ({i+1}) "
                self.text += self.my_replace(self.book[chaphead][i])

            for i in range(chaphead+1, chaptail):
                self.text += f"\n\n[{i+1}]\t"

                for j in range(len(self.book[i])):
                    self.text += f" ({j+1}) "
                    self.text += self.my_replace(self.book[i][j])

            self.text += f"\n\n[{chaptail+1}]\t"

            for i in range(versetail+1):
                self.text += f" ({i+1}) "
                self.text += self.my_replace(self.book[chaptail][i])

            return 0
        except:
            return 1