import PySimpleGUI as sg
import frontend.initial_setup_frontend

def window_info():

    layout = [
        # Linha 1 - Informações dos Contatos
        [sg.Text('Informações dos Contatos',
                 size=(48, 1),
                 justification='center',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((5, 5), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light)],
        # Linha 2 - Nome
        [sg.Text('Nome  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_name',
                 size=(25, 1))
         ],
        # Linha 3 - Telefone e celular
        [sg.Text('Telefone  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_phone',
                 size=(15, 1)),
         sg.Text('Celular  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('', font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_celphone',
                 size=(15, 1))

         ],
        # Linha 4 - Sexo
        [sg.Text('Sexo  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('', font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_sex',
                 size=(25, 1))

         ],
        # Linha 5 - Endereço e numero
        [sg.Text('Logradouro  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('', font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_address',
                 size=(20, 1)),
         sg.Text('Número  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('', font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_address_number',
                 size=(9, 1))

         ],
        # Linha 6 - Bairro
        [sg.Text('Bairro  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('', font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_address_quarter',
                 size=(25, 1))

         ],
        # Linha 7 - Cidade e estado
        [sg.Text('Cidade  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_city',
                 size=(17, 1)),
         sg.Text('Estado  ',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text_name),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light),
         sg.Text('',
                 font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
                 pad=((1, 1), (1, 2)),
                 background_color=frontend.initial_setup_frontend.color_light,
                 key='contact_state',
                 size=(16, 1))

         ]

    ]

    return layout

