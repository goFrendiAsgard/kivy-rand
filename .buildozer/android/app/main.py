import kivy, random
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

__version__ = '0.0.0'

class Screen(BoxLayout):
    def button_click(self, instance):
        lower_bound = self.ids.minInput.text
        upper_bound = self.ids.maxInput.text
        trial       = self.ids.trialInput.text
        lower_bound = int(lower_bound) if lower_bound.isdigit() else 1
        upper_bound = int(upper_bound) if upper_bound.isdigit() and int(upper_bound)>lower_bound else int(lower_bound)+5
        trial       = int(trial) if trial.isdigit() and int(trial)>0 else 1
        self.ids.minInput.text = str(lower_bound)
        self.ids.maxInput.text = str(upper_bound)
        self.ids.trialInput.text    = str(trial)
        # start to random
        random_list = []
        if instance == self.ids.generateNoDuplicateButton:
            number_list = range(lower_bound, upper_bound+1)
            for i in range(len(number_list)*2):
                j = random.randint(0, upper_bound-lower_bound)
                k = random.randint(0, upper_bound-lower_bound)
                number_list[j], number_list[k] = number_list[k], number_list[j]
            random_list = number_list[0:trial]
        else:
            for i in range(trial):
                random_list.append(random.randint(lower_bound, upper_bound))
        for i in range(len(random_list)):
            random_list[i] = str(random_list[i])
        self.ids.randomLabel.text = ', '.join(random_list)

class RandApp(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
    RandApp().run();