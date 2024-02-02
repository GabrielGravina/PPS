from abc import ABC

class Button(ABC):
    def display(self):
        pass

class TextBox(ABC):
    def display(self):
        pass

class Menu(ABC):
    def display(self):
        pass

class WidgetFactory(ABC):
    def create_button(self):
        pass

    def create_textbox(self):
        pass

    def create_menu(self):
        pass

class ModernWidgetFactory(WidgetFactory):
    def create_button(self):
        return ModernButton()

    def create_textbox(self):
        return ModernTextBox()

    def create_menu(self):
        return ModernMenu()

class ClassicWidgetFactory(WidgetFactory):
    def create_button(self):
        return ClassicButton()

    def create_textbox(self):
        return ClassicTextBox()

    def create_menu(self):
        return ClassicMenu()

class ModernButton(Button):
    def display(self):
        print("Modern Button")

class ModernTextBox(TextBox):
    def display(self):
        print("Modern TextBox")

class ModernMenu(Menu):
    def display(self):
        print("Modern Menu")

class ClassicButton(Button):
    def display(self):
        print("Classic Button")

class ClassicTextBox(TextBox):
    def display(self):
        print("Classic TextBox")

class ClassicMenu(Menu):
    def display(self):
        print("Classic Menu")

class GUIApplication:
    def __init__(self, widget_factory):
        self.button = widget_factory.create_button()
        self.textbox = widget_factory.create_textbox()
        self.menu = widget_factory.create_menu()

    def display_widgets(self):
        print("Displaying GUI widgets:")
        self.button.display()
        self.textbox.display()
        self.menu.display()

if __name__ == "__main__":
    modern_widget_factory = ModernWidgetFactory()
    classic_widget_factory = ClassicWidgetFactory()

    app_modern = GUIApplication(modern_widget_factory)
    app_modern.display_widgets()

    print("\n---\n")

    app_classic = GUIApplication(classic_widget_factory)
    app_classic.display_widgets()
