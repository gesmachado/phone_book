import PySimpleGUI as sg
import frontend.setup
from backend import operation_system
from backend.files import load_file, read_file
from frontend.window_book_list import window_book_list
from frontend.window_info import window_info
from frontend.window_logo import window_logo
from frontend.window_show import window_show
from frontend.window_statistics import window_statistics
from frontend.window_title import window_title



def main_layout():
    sg.theme(frontend.setup.window_theme)
    values = read_file(load_file())

    layout_title = window_title()
    layout_list = window_book_list(values)
    layout_logo = window_logo()
    layout_info = window_info()
    layout_show = window_show()
    layout_statistics = window_statistics()

    col1 = [
        [sg.Column(layout_logo, background_color=frontend.setup.color_light, size=(140, 140), justification='top'), sg.Column(layout_show, background_color=frontend.setup.color_light, size=(300, 140))],
        [sg.Column(layout_info, size=(449, 200), background_color=frontend.setup.color_light)],
        [sg.Column(layout_statistics, size=(433, 200), background_color=frontend.setup.color_light, scrollable=True, vertical_scroll_only=True)]
    ]

    layout_main =[
        [sg.Column(layout_title, background_color=frontend.setup.color_medium, size=(1000, 35), pad=(1, 1, 1, 1))],
        [sg.Column(col1, background_color=frontend.setup.color_medium, pad=(1, 1, 1, 1)), sg.Column(layout_list, background_color=frontend.setup.color_light, size=(500, 511), pad=(1, 1, 1, 1))],
    ]

    return sg.Window('Lista de Contatos', layout=layout_main, finalize=True, size=(970, 560), background_color=frontend.setup.color_medium).Finalize()


# Use only to unit test
def unit_test():

    # Criar as janelas inicias
    w_main = main_layout()

    while True:
        window, event, values = sg.read_all_windows()



        # # Quando janela for fechada
        if window == w_main and event == sg.WIN_CLOSED:
            break
        if event == 'btn_delete':
            w_main.FindElement('contact_name').Update(name)
            w_main.FindElement('contact_phone').Update(phone)
            w_main.FindElement('contact_sex').Update(sex)
            w_main.FindElement('contact_address').Update(address)
            w_main.FindElement('contact_city').Update(city)
            w_main.FindElement('contact_state').Update(state)


if __name__ == '__main__':
    name = 'Gustavo Eduardo Silva Machado'
    phone = '34991077043'
    sex = 'Masculino'
    address = 'Rua Pádua e Castro, 166'
    city = 'Campinas'
    state = 'São Paulo'
    unit_test()
