import PySimpleGUI as sg
import frontend.initial_setup_frontend


def popup_error_101(values):
    sg.popup('Já existe um contato com esse nome.\n'
             'Altere o nome do contato para que possa ser adicionado!',
             font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
             background_color=frontend.initial_setup_frontend.color_medium,
             title='[101] Erro ao adicionar contato',
             button_color=frontend.initial_setup_frontend.color_hard)


def popup_error_102(values):
    sg.popup('Não é permitido adicionar um contato sem nome.\n'
             'Altere o nome do contato para que possa ser adicionado!',
             font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
             background_color=frontend.initial_setup_frontend.color_medium,
             title='[102] Erro ao adicionar contato',
             button_color=frontend.initial_setup_frontend.color_hard)


def popup_error_103(values):
    sg.popup('É necessário selecionar o contato que deseja excluir antes.\n'
             'Selecione o contato e tente novamente!',
             font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
             background_color=frontend.initial_setup_frontend.color_medium,
             title='[103] Erro ao excluir contato',
             button_color=frontend.initial_setup_frontend.color_hard)

def popup_to_do(values):
    sg.popup('Feature não implementada.\n'
             'Essa feature será implementado em versões futuras',
             font=(frontend.initial_setup_frontend.font, frontend.initial_setup_frontend.font_size_text),
             background_color=frontend.initial_setup_frontend.color_medium,
             title='NÃO IMPLEMENTADO',
             button_color=frontend.initial_setup_frontend.color_hard)

