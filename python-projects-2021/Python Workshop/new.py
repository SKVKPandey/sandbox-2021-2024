
class Time:

    def reply(self, string):

        if len(string) < 5:
            self.val = int(string[0])

        else:
            self.val = int(string[:2])
        

        if self.val >= 6 and self.val < 12:
            print("Good Morning")
        elif self.val >= 12 and self.val < 16:
            print("Good Afternoon")
        elif self.val >= 16 and self.val < 20:
            print("Good Evening")
        else:
            print("Good Night")

#reply("21:30")

#19:30
#6:40

    
    