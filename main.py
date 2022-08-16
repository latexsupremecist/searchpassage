from reader import Reader
import os

translations = ["KJV", "CUV", "NCV"]

class Main:
    def __init__(self):
        self.input_loop()
    
    def get_version(self,ans):
        
        ans = ans.upper()

        if(ans == "Q"):
            exit()

        self.reader = Reader()

        try:
            self.reader.get_translation("translations/"+ans+".json")
            self.reader.translation = ans
            return 0
        except:
            print("\nInvalid version.\n")
            return 1

    def get_content(self,book,location):
        status = []
        status.append(self.reader.get_book(book))
        status.append(self.reader.get_chapter_and_verses(location))

        return status

    def input_loop(self):

        while(True):
            ans = input("Enter version and passage (or q to quit): ")
            ans = ans.split()
            
            status = self.get_version(ans[0])

            if status == 1:
                continue

            if len(ans) > 5:
                print("\nToo many inputs.\n")
                continue
            
            if len(ans) < 2:
                print("\nToo little input(s).")
                continue

            if len(ans) == 2:
                status = self.get_content(self.cache[0],self.cache[1])

            if len(ans) == 5:
                ans[1] = ans[1] + " " + ans[2] + " " + ans[3]
                ans[2] = ans[4]

            if(len(ans) == 4):
                ans[1] = ans[1] + " " + ans[2]
                ans[2] = ans[3]

            if(len(ans) > 2):
                
                self.cache = []
                self.cache.append(ans[1])
                self.cache.append(ans[2])

                status = self.get_content(ans[1],ans[2])              

            if status[0] == 1:
                print("\nInvalid book.\n")
                continue
            
            if status[1] == 1:
                print("\nInvalid chapters/verses.\n")
                continue

            print("\n\n")
            print(self.reader.text)
            print("\n\n")


Main()
