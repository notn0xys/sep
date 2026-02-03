from unicodedata import name
import js
from pyscript import document
from pyodide.ffi import create_proxy
from datetime import datetime 
from abc import ABC, abstractmethod 

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if self._element is None:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element

    @abstractmethod
    def draw_widget(self):
        pass

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# class CurrencyConverter(AbstractWidget):
#     def draw_widget(self):
#         container = document.createElement("div")
#         container.className = "currency-converter"

#         title = document.createElement("h2")
#         title.innerText = "Currency Converter"
#         container.appendChild(title)

#         input_amount = document.createElement("input")
#         input_amount.type = "number"
#         input_amount.placeholder = "Amount in THB"
#         container.appendChild(input_amount)

#         convert_button = document.createElement("button")
#         convert_button.innerText = "Convert to USD"
#         container.appendChild(convert_button)

#         result_display = document.createElement("p")
#         result_display.innerText = "Converted Amount: "
#         container.appendChild(result_display)

#         def convert_currency(event):
#             try:
#                 amount_thb = float(input_amount.value)
#                 conversion_rate = 30.0 
#                 amount_usd = amount_thb / conversion_rate
#                 result_display.innerText = f"Converted Amount: {amount_usd:.2f} USD"
#             except ValueError:
#                 result_display.innerText = "Please enter a valid number."

#         convert_button.addEventListener("click", create_proxy(convert_currency))

#         self.element.appendChild(container)

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.counter = 1

    def on_click(self, event):
        if self.button.innerText == "pause":
            self.button.innerText = "play"
            js.clearInterval(self.interval_id)
        else:
            self.button.innerText = "pause"
            self.interval_id = js.setInterval(create_proxy(self.on_setInterval), 100)

    def on_setInterval(self):
        self.counter += 1
        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def draw_widget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        self.interval_id = js.setInterval(create_proxy(self.on_setInterval), 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)
class ColorfulAnimationWidget(AnimationWidget):
    def draw_widget(self):
        super().draw_widget()
        self.color_btn = document.createElement("button")
        self.color_btn.innerText = "Change Background Color"
        self.color_btn.style.width = "600px"
        self.color_btn.onclick = create_proxy(self.color_change)
        self.element.appendChild(self.color_btn)
    def color_change(self, event):
        import random
        r = lambda: random.randint(0,255)
        g = lambda: random.randint(0,255)
        b = lambda: random.randint(0,255)
        random_color = '#%02X%02X%02X' % (r(),g(),b())
        self.element.style.backgroundColor = random_color
if __name__ == "__main__":
    output = ColorfulAnimationWidget("container")
    output.draw_widget()
