
class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("Some noise")

    def get_name(self):
        return  self.inner_name

    def get_name_x(self,x):
        return (self.name + x)


class Drums(Instrument):

    def __init__(self):
        #super().__init__("Drums")
        Instrument.__init__(self,"Drums")
        self.inner_name = "Inner-drums"

    def play(self):
        print("Drums rhytm")

    def get_nameA(self):

        return self.get_name()
        #return super().get_name() + "nadpisana gitara"


class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar")
        #Instrument.__init__("Guitar")

    def play(self):
        print("guitar is playing")


def main():

    beben = Drums()
    gitara = Guitar()

    beben.play()
    print(beben.get_name())

   # gitara.play()
    #print(gitara.get_name())


if __name__ == '__main__':
    main()