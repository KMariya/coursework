from kivy.config import Config
Config.set('graphics','resizable', '0')
# Config.set('graphics','borderless', '1')
Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '1024')
Config.set('graphics', 'left', 240)
Config.set('graphics', 'top', 10)
Config.set('graphics', 'position', "custom")
from kivy.core.window import Window

Window.clearcolor = (13 / 255, 16 / 255, 26 / 255, 1)
Window.title = "PolyMoney"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import ScreenManager, Screen

predmeti = ("Спортивная деятельность","Культурно-творческая деятельность","Общественная деятельность","Учебная деятельность","Научная деятельность")
predmet_sport = ("Участие в межвузовских соревнованиях", "Победа в межвузовских соревнованиях", "Участие в киберспортивных соревнованиях", "Победа в киберспортивных соревнованиях")
predmet_culture = ("1", "2", "3")
predmet_society = ("1","2","3","4","5")
predmet_study = ("1", "2")
predmet_science = ("1", "2")
kolvo_ochka = 0
xapp = 1440
yapp = 1024
class  PolyMoneyApp(App):

    def build(self):
        self.sm = ScreenManager()
        screen1 = Screen(name="Menu")
        screen2 = Screen(name="Основа")
        screen3 = Screen(name="Предмет")
        screen4 = Screen(name="Баланс")

        # Screen 1. Начальный экран
        al_menu = FloatLayout()
        al_menu.add_widget(Label(text="Введите ваше ФИО:",font_size=48,size_hint=[467/xapp,58/yapp],pos=(487,840)))
        self.inputa_data = TextInput(size_hint=[850/xapp,50/yapp],pos=(295,770),multiline=False)
        al_menu.add_widget(self.inputa_data)

        al_menu.add_widget(Label(text="Введите вашу группу:", font_size=48, size_hint=[467 / xapp, 58 / yapp], pos=(487, 690)))
        self.inputa_data1 = TextInput(size_hint=[350 / xapp, 50 / yapp], pos=(545, 620), multiline=False)
        al_menu.add_widget(self.inputa_data1)

        self.oshibka_vvoda = Label(text="",font_size=32)
        al_menu.add_widget(self.oshibka_vvoda)
        al_menu.add_widget(Button(text="Войти",
                      font_size = 32,
                      on_press = self.toosn,
                      size_hint=[300/xapp,104/yapp],
                      pos=(570,300),
                      background_normal="",background_color=(159/255,43/255,85/255)))

        al_menu.add_widget(Button(text="Выйти",on_press=self.stop_prog,font_size=32,size_hint=[300/xapp,95/yapp],pos=(570,38),background_normal="",background_color=(40/255,48/255,78/255)))
        screen1.add_widget(al_menu)

        # Screen 2. Основное меню
        al_osnova = FloatLayout()
        self.fio_label = Label(text="",font_size=48,size_hint=[702/xapp,58/yapp],pos=(369,885))
        al_osnova.add_widget(self.fio_label)

        self.grup_label = Label(text="",font_size=48,size_hint=[702/xapp,58/yapp],pos=(369,815))
        al_osnova.add_widget(self.grup_label)

        self.predmet_label = Label(text="Выберите раздел:",font_size=32,size_hint=[283/xapp,39/yapp],pos=(100,686))
        al_osnova.add_widget(self.predmet_label)

        spisok_predmetov = DropDown()
        for i in predmeti:
            btn = Button(text=i,font_size=32,background_normal="",color=(0,0,0,1),background_color=(217/255,217/255,217/255),size_hint_y=None,height=50)
            btn.bind(on_release = lambda btn: spisok_predmetov.select(btn.text))
            spisok_predmetov.add_widget(btn)
        spisok_predmetov.container.spacing = 4

        self.stroka = Button(size_hint=[828 / xapp, 70 / yapp], font_size=32,pos=(512, 671),color=(0,0,0,1),background_normal="",background_color=(157 / 255, 191 / 255, 231 / 255, 1),on_release=spisok_predmetov.open)

        al_osnova.add_widget(self.stroka)
        spisok_predmetov.bind(on_select=lambda instance, x: setattr(self.stroka, 'text', x))

        self.oshibka_vibora_razdela = Label(text="",font_size=32)
        al_osnova.add_widget(self.oshibka_vibora_razdela)

        self.knopka_vibr = Button(text="Выбрать",font_size=32,on_press=self.toachiev,size_hint=[444/xapp,95/yapp],pos=(502,322),background_normal="",background_color=(159/255,43/255,85/255))
        al_osnova.add_widget(self.knopka_vibr)

        self.uznat_den1 = Button(text="Узнать текущий баланс", font_size=32, on_press=self.balans_window,
                                size_hint=[444 / xapp, 95 / yapp], pos=(502, 180), background_normal="",
                                background_color=(59 / 255, 74 / 255, 150 / 255))
        al_osnova.add_widget(self.uznat_den1)

        al_osnova.add_widget(Button(text="Назад",font_size=32,on_press=self.tomenu,size_hint=[300/xapp,95/yapp],pos=(570,38),background_normal="",background_color=(40/255,48/255,78/255)))
        screen2.add_widget(al_osnova)

        # Screen 3. Выбор достижений.
        al_dostizh = FloatLayout()
        self.achiv_label = Label(text="Выберите достижение:",halign="left",font_size=32,size_hint=[366/xapp,39/yapp],text_size=(366,39),pos=(100,636))
        self.fio_label1 = Label(text="", font_size=48, size_hint=[702 / xapp, 58 / yapp],pos=(369, 885))
        al_dostizh.add_widget(self.fio_label1)

        self.grup_label1 = Label(text="", font_size=48, size_hint=[702 / xapp, 58 / yapp], pos=(369, 815))
        al_dostizh.add_widget(self.grup_label1)

        self.razdel = Label(text="Раздел:", halign="left",text_size=(121,39),font_size=32, size_hint=[121 / xapp, 39 / yapp],pos=(100, 735))
        self.vibr_razdel = Label(text="", font_size=32, halign="left",size_hint=[800 / xapp, 39 / yapp],text_size=(800, 39),pos=(271, 735))

        al_dostizh.add_widget(self.razdel)
        al_dostizh.add_widget(self.vibr_razdel)
        al_dostizh.add_widget(self.achiv_label)

        spisok_achiev = DropDown()
        for i in predmet_sport:
            btn = Button(text=i,font_size=32,background_normal="",color=(0,0,0,1),background_color=(217/255,217/255,217/255),size_hint_y=None,height=50)
            btn.bind(on_release = lambda btn: spisok_achiev.select(btn.text))
            spisok_achiev.add_widget(btn)
        spisok_achiev.container.spacing = 4

        self.knopka_vibora_achiv = Button(size_hint=[828 / xapp, 70 / yapp], font_size=32,pos=(512, 621),color=(0,0,0,1),background_normal="",background_color=(157 / 255, 191 / 255, 231 / 255, 1),on_release=spisok_achiev.open)
        al_dostizh.add_widget(self.knopka_vibora_achiv)
        spisok_achiev.bind(on_select=lambda instance, x: setattr(self.knopka_vibora_achiv,'text',x))

        self.knopka_achiv = Button(text="Выбрать",font_size=32,on_press=self.vibor_achiv,size_hint=[444/xapp,95/yapp],pos=(502,322),background_normal="",background_color=(159/255,43/255,85/255))
        al_dostizh.add_widget(self.knopka_achiv)

        self.uznat_den = Button(text="Узнать текущий баланс", font_size=32, on_press=self.balans_window,
                                   size_hint=[444 / xapp, 95 / yapp], pos=(502, 180), background_normal="",
                                   background_color=(59 / 255, 74 / 255, 150 / 255))
        al_dostizh.add_widget(self.uznat_den)

        self.oshibka_vibora_achiv = Label(text="",font_size=32)
        al_dostizh.add_widget(self.oshibka_vibora_achiv)

        self.nach_ball = Label(text="",font_size=32)
        al_dostizh.add_widget(self.nach_ball)

        al_dostizh.add_widget(Button(text="Назад", on_press=self.toosn2,font_size=32,size_hint=[300/xapp,95/yapp],pos=(570,38),background_normal="",background_color=(40/255,48/255,78/255)))

        screen3.add_widget(al_dostizh)

        #Screen 4. Баланс.
        fl_balans = FloatLayout()
        self.fio_label3 = Label(text="",font_size=48,size_hint=[702/xapp,58/yapp],pos=(369,885))
        fl_balans.add_widget(self.fio_label3)

        self.grup_label2 = Label(text="", font_size=48, size_hint=[702 / xapp, 58 / yapp], pos=(369, 815))
        fl_balans.add_widget(self.grup_label2)

        self.balans_label_ball = Label(text = "Ваше количество баллов",font_size=48,pos=(0,150))
        fl_balans.add_widget(self.balans_label_ball)

        self.balans_label_ball_summ = Label(text = str(kolvo_ochka), font_size=48,pos=(0,75))
        fl_balans.add_widget(self.balans_label_ball_summ)

        self.balans_label_den = Label(text="Ваше рекомендательная выплата", font_size=48, pos=(0, -75))
        fl_balans.add_widget(self.balans_label_den)

        self.balans_label_den_summ = Label(text=str(kolvo_ochka*1.9), font_size=48, pos=(0, -150))
        fl_balans.add_widget(self.balans_label_den_summ)

        self.balans_nazad_but = Button(text="Назад",font_size=32,size_hint=[300/xapp,95/yapp],pos=(570,38),background_normal="",background_color=(40/255,48/255,78/255))
        self.balans_nazad_but.bind(on_press=self.toosn2)
        fl_balans.add_widget(self.balans_nazad_but)

        screen4.add_widget(fl_balans)

        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)
        self.sm.add_widget(screen3)
        self.sm.add_widget(screen4)
        self.sm.current = "Menu"
        return self.sm

    def tomenu(self,instance):
        self.inputa_data.text = ""
        self.inputa_data1.text = ""
        self.stroka.text = ""
        self.sm.current = "Menu"
        self.sm.transition.direction = "right"

    def balans_window(self,instance):
        self.sm.current = "Баланс"
        self.sm.transition.direction = "left"

    def toosn(self,instance):
        data = self.inputa_data.text
        data = " ".join(data.split())
        data1 = self.inputa_data1.text
        if data == "" or data1 == "":
            self.oshibka_vvoda.text = "Вы не ввели все данные"
        else:
            self.oshibka_vvoda.text = ""
            self.fio_label.text = data
            self.fio_label1.text = data
            self.fio_label3.text = data
            self.grup_label.text = data1
            self.grup_label1.text = data1
            self.grup_label2.text = data1
            self.sm.current = "Основа"
            self.sm.transition.direction = "left"

    def toachiev1(self,instance):
        self.nach_ball.text = ""
        self.sm.current = "Предмет"
        self.sm.transition.direction = "right"

    def toachiev(self,instance):
        self.nach_ball.text = ""
        data1 = self.stroka.text
        if data1 == "":
            self.oshibka_vibora_razdela.text = "Вы не выбрали раздел"
        else:
            self.balans_nazad_but.unbind(on_press=self.toosn2)
            self.balans_nazad_but.bind(on_press=self.toachiev1)
            self.oshibka_vibora_razdela.text = ""
            self.vibr_razdel.text = self.stroka.text
            self.sm.current = "Предмет"
            self.sm.transition.direction = "left"

    def toosn2(self,instance):
        self.balans_nazad_but.unbind(on_press=self.toachiev1)
        self.balans_nazad_but.bind(on_press=self.toosn2)
        self.sm.current = "Основа"
        self.sm.transition.direction = "right"
        self.oshibka_vibora_achiv.text = ""
        self.knopka_vibora_achiv.text = ""

    def vibor_achiv(self,instance):
        global kolvo_ochka
        data2 = self.knopka_vibora_achiv.text
        if data2 == "":
            self.oshibka_vibora_achiv.text = "Вы не выбрали достижение"
        else:
            self.oshibka_vibora_achiv.text = ""
            self.nach_ball.text = "Вам начислено 20 баллов"
            kolvo_ochka = kolvo_ochka+20
            #изменение суммы
            self.balans_label_ball_summ.text = str(kolvo_ochka)
            self.balans_label_den_summ.text = str(kolvo_ochka*35)

    def stop_prog(self,instance):
        self.root_window.close()

if __name__ == "__main__":
    PolyMoneyApp().run()

