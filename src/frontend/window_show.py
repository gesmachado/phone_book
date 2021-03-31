import frontend
import PySimpleGUI as sg


def window_show():
    layout = [
        # Linha 1
        [sg.Text('Informações do Software',
                 justification='center',
                 size=(32, 1),
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light)],
        # Linha 2
        [sg.Text('Autor:',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=(1, 1, 1, 1),
                 background_color=frontend.setup.color_light),
         sg.Text('Gustavo Eduardo Silva Machado',
                 font=(frontend.setup.font, frontend.setup.font_size_text),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light)],
        # linha 3
        [sg.Text('Versão:',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light),
         sg.Text('1.0.0',
                 font=(frontend.setup.font, frontend.setup.font_size_text),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light)
         ],
        # Linha 4
        [sg.Text('Data:',
                 font=(frontend.setup.font, frontend.setup.font_size_text_name),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light),
         sg.Text('Em desenvolvimento',
                 font=(frontend.setup.font,
                       frontend.setup.font_size_text),
                 pad=((1, 1), (1, 1)),
                 background_color=frontend.setup.color_light)
         ]
    ]
    return layout

