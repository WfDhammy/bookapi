from test import main


class Tecno(main.Phone):
    def portrait(self):
        return f"Tecno has a {self.camera} camera"
    

device = Tecno()
print(device)