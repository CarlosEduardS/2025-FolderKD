from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Menu(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Label do título centralizado no topo
        self.title_label = Label(
            text="--Áperos Imperium--",
            font_size=24,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={"center_x": 0.5, "top": 1}
        )

        self.normal_label = Label(text="Compromisso da alta direção: Garantir apoio e recursos para o projeto. \nNomear um responsável pelo SGSI. Definir o escopo: Determinar quais áreas, \nprocessos e ativos de informação serão cobertos. Análise de riscos: \nIdentificar ativos de informação. Avaliar ameaças, vulnerabilidades e impactos. Classificar riscos e definir prioridades. \nPolítica de Segurança da Informação: Criar diretrizes claras para proteger dados. Comunicar a todos os colaboradores. \nSeleção e implementação de controles: Basear-se no Anexo A da norma (controles físicos, lógicos, organizacionais etc.). \nExemplos: controle de acesso, criptografia, backup, segurança física. \nTreinamento e conscientização: \nCapacitar a equipe para seguir as políticas e reconhecer riscos. \nMonitoramento e auditoria interna: \nAvaliar periodicamente se os controles estão funcionando. Corrigir falhas e melhorar continuamente. \nAuditoria externa e certificação (opcional): \nCaso queira o selo ISO 27001, contratar um organismo certificador."
        )
        self.normal_label.opacity = 0
        self.normal_label.pos_hint = {"center_x": 0.5, "top": 0.5}
        self.normal_label.size=(300, 50)
        self.normal_label.size_hint=(None, None)
        self.normal_label.font_size=22
        
        # Botão posicionado mais abaixo
        self.action_button = Button(
            text="~Começar~",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "y": 0.4}
        )
        self.action_button.bind(on_press=self.on_button_click)

        self.add_widget(self.normal_label)
        self.add_widget(self.title_label)
        self.add_widget(self.action_button)

    def on_button_click(self, instance):
        self.normal_label.opacity = 1
        self.title_label.opacity = 0
        self.action_button.opacity = 0

class MyApp(App):
    def build(self):
        return Menu()

if __name__ == "__main__":
    MyApp().run()
