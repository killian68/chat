#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import pygame
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog
import os
from time import strftime
import configparser
from SQLretriever import SQLretriever

global count, users, passwordEntry, listUser, sortie, new, detail


count = 0


def readConfig():  # Lecture du fichier de configuration s'il existe ou création sinon
    config = configparser.ConfigParser()
    if os.path.exists(str(os.getcwd() + '/Ressources/ChatCROM.ini')):
        config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    else:
        config['Network'] = {'location': ''}  #definir host du serveur MySQL distant
        snd = str(os.getcwd() + '/Ressources/beep.wav')
        config['Sound'] = {'newmsg': snd}
        acreer = str(os.getcwd() + '/Ressources/ChatCROM.ini')
        with open(acreer, 'w') as configfile:
            config.write(configfile)
    renvoi = (config['Network']['location'], config['Sound']['newmsg'])
    return renvoi


def configprog():  # interface de changement de config depuis le prog principal
    global fenconfigprog, v, sndvalue, netsel
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    netvalues = [('', 'l'), ('', 'r')]  # netvalues l est IP locale du Serveur MySQL, r est le hostname distant du serveur MySQL
    soundvalues = [('Pas de son', 'n'), ('Son par defaut', 'd'), ('Choisir son fichier', 'c')]
    fenconfigprog = Toplevel()
    fenconfigprog.title('Configuration du programme')
    fenconfigprog.geometry('490x300+' + str(int((largeur / 2) - 490 / 2)) + '+' + str(int((hauteur / 2) - (300 / 2))))
    fenconfigprog.protocol('WM_DELETE_WINDOW', quitconfiglogonprog)
    fenconfigprog.resizable(width=False, height=False)
    netframe = ttk.LabelFrame(fenconfigprog, text='Localisation de la base :')
    netframe.grid(row=0, column=0, padx=5, pady=5)
    netsel = StringVar()
    if str(config['Network']['Location']) == '':  # definir adresse IP locale du Serveur MySQL
        netsel.set('l')
    else:
        netsel.set('r')
    for txt, mode in netvalues:
        d = ttk.Radiobutton(netframe, text=txt, variable=netsel, value=mode, command=selnetprog)
        d.pack(anchor=W)
    soundframe = ttk.LabelFrame(fenconfigprog, text='Son message')
    soundframe.grid(row=1, column=0, padx=5, pady=5)
    v = StringVar()
    if str(config['Sound']['newmsg']) == str(os.getcwd()) + '/Ressources/nosound.wav':
        v.set('n')
    elif str(config['Sound']['newmsg']) == str(os.getcwd()) + '/Ressources/beep.wav':
        v.set('d')
    else:
        v.set('c')
    sndvalue = StringVar()
    fl = config['Sound']['newmsg']
    fl2 = fl.split('/')
    sndvalue.set(fl2[len(fl2) - 1])
    for text, mode in soundvalues:
        b = ttk.Radiobutton(soundframe, text=text, variable=v, value=mode, command=selsoundprog)
        b.pack(anchor=W)
    soundlabel = ttk.Label(fenconfigprog, textvariable=sndvalue)
    soundlabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    valconf = ttk.Button(fenconfigprog, text='Quitter', command=quitconfiglogonprog)
    valconf.grid(row=3, column=0, padx=5, pady=5)


def selsoundprog():
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    selection = str(v.get())
    fl = config['Sound']['newmsg']
    fl2 = fl.split('/')
    sndvalue.set(fl2[len(fl2) - 1])
    if selection == 'n':
        config['Sound']['newmsg'] = str(os.getcwd() + '/Ressources/nosound.wav')
        sndvalue.set('Pas de son')
    elif selection == 'c':
        filename = tkinter.filedialog.askopenfilename(filetypes=[('Audio Files', '*.wav')])
        if str(filename) == '()':
            filename = str(os.getcwd() + '/Ressources/beep.wav')
            sndvalue.set('Son par defaut')
            v.set('d')
        else:
            config['Sound']['newmsg'] = filename
            sndvalue.set(config['Sound']['newmsg'])
    elif selection == 'd':
        config['Sound']['newmsg'] = str(os.getcwd() + '/Ressources/beep.wav')
        sndvalue.set('Son par defaut')
    acreer = str(os.getcwd() + '/Ressources/ChatCROM.ini')
    with open(acreer, 'w') as configfile:
            config.write(configfile)


def selnetprog():
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    selection = str(netsel.get())
    if selection == 'l':
        config['Network']['location'] = ''  # Adresse IP locale du Serveur MySQL
    else:
        config['Network']['location'] = ''  # hostname distant du Serveur MySQL
    acreer = str(os.getcwd() + '/Ressources/ChatCROM.ini')
    with open(acreer, 'w') as configfile:
            config.write(configfile)


def quitconfiglogonprog():
    fenconfigprog.destroy()
    tkinter.messagebox.showinfo(title='Configuration Changée', message='Afin que les modifications prennent effet, le programme doit etre redémarré')
    requete2 = "UPDATE `alarme`.`users` SET `actif`='n' WHERE `username`='" + usr + "';"
    desactivation = SQLretriever(requete2, host, user, password, database)
    desactivation.update()
    msg = usr + ' est maintenant déconnecté du chat.'
    tkinter.messagebox.showinfo(title='Sortie', message=msg)
    fen1.destroy()


def changeConfig():  # interface de changement de configuration depuis la fenêtre de logon
    global fenconfig, v, sndvalue, netsel
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    netvalues = [('', 'l'), ('', 'r')]  #net values l = IP locale serveur MySQL r = hostname distant du serveur MySQL distant
    soundvalues = [('Pas de son', 'n'), ('Son par defaut', 'd'), ('Choisir son fichier', 'c')]
    fenconfig = Toplevel()
    fenconfig.title('Configuration du programme')
    fenconfig.geometry('490x300+' + str(int((largeur / 2) - 490 / 2)) + '+' + str(int((hauteur / 2) - (300 / 2))))
    fenconfig.protocol('WM_DELETE_WINDOW', quitconfiglogon)
    fenconfig.resizable(width=False, height=False)
    netframe = ttk.LabelFrame(fenconfig, text='Localisation de la base :')
    netframe.grid(row=0, column=0, padx=5, pady=5)
    netsel = StringVar()
    if str(config['Network']['Location']) == '':  # IP locale du serveur MySQL
        netsel.set('l')
    else:
        netsel.set('r')
    for txt, mode in netvalues:
        d = ttk.Radiobutton(netframe, text=txt, variable=netsel, value=mode, command=selnet)
        d.pack(anchor=W)
    soundframe = ttk.LabelFrame(fenconfig, text='Son message')
    soundframe.grid(row=1, column=0, padx=5, pady=5)
    v = StringVar()
    if str(config['Sound']['newmsg']) == str(os.getcwd()) + '/Ressources/nosound.wav':
        v.set('n')
    elif str(config['Sound']['newmsg']) == str(os.getcwd()) + '/Ressources/beep.wav':
        v.set('d')
    else:
        v.set('c')
    sndvalue = StringVar()
    fl = config['Sound']['newmsg']
    fl2 = fl.split('/')
    sndvalue.set(fl2[len(fl2) - 1])
    for text, mode in soundvalues:
        b = ttk.Radiobutton(soundframe, text=text, variable=v, value=mode, command=selsound)
        b.pack(anchor=W)
    soundlabel = ttk.Label(fenconfig, textvariable=sndvalue)
    soundlabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    valconf = ttk.Button(fenconfig, text='Quitter', command=quitconfiglogon)
    valconf.grid(row=3, column=0, padx=5, pady=5)


def selnet():  # actions sur changement du reseau depuis fenetre de logon
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    selection = str(netsel.get())
    if selection == 'l':
        config['Network']['location'] = ''  # IP locale du servuer MySQL
    else:
        config['Network']['location'] = ''  # hostname distant du Serveur MySQL
    acreer = str(os.getcwd() + '/Ressources/ChatCROM.ini')
    with open(acreer, 'w') as configfile:
            config.write(configfile)


def selsound():  # actions sur changement du son depuis fenetre de logon
    config = configparser.ConfigParser()
    config.read(str(os.getcwd() + '/Ressources/ChatCROM.ini'))
    selection = str(v.get())
    fl = config['Sound']['newmsg']
    fl2 = fl.split('/')
    sndvalue.set(fl2[len(fl2) - 1])
    if selection == 'n':
        config['Sound']['newmsg'] = str(os.getcwd() + '/Ressources/nosound.wav')
        sndvalue.set('Pas de son')
    elif selection == 'c':
        filename = tkinter.filedialog.askopenfilename(filetypes=[('Audio Files', '*.wav')])
        if str(filename) == '()':
            filename = str(os.getcwd() + '/Ressources/beep.wav')
            sndvalue.set('Son par defaut')
            v.set('d')
        else:
            config['Sound']['newmsg'] = filename
            sndvalue.set(config['Sound']['newmsg'])
    elif selection == 'd':
        config['Sound']['newmsg'] = str(os.getcwd() + '/Ressources/beep.wav')
        sndvalue.set('Son par defaut')
    acreer = str(os.getcwd() + '/Ressources/ChatCROM.ini')
    with open(acreer, 'w') as configfile:
            config.write(configfile)


def quitconfiglogon():
    fenconfig.destroy()
    tkinter.messagebox.showinfo(title='Configuration Changée', message='Afin que les modifications prennent effet, le programme doit etre redémarré')
    fen1.destroy()


def sellstalarme(event):  # activation du bouton detail si une alarme est selectionnee
    detail.configure(state=NORMAL)


def dblsellstalarme(event):
    detail.configure(state=DISABLED)
    detailmsg()


def detailmsg():  # construction et affichage de la fenetre detail d'un message'
    global fendetail
    detail.configure(state=DISABLED)
    idx = lstalarme.focus()
    heure = lstalarme.item(idx)['text']
    emeteur = lstalarme.item(idx)['values'][0]
    message = lstalarme.item(idx)['values'][1]
    fendetail = Toplevel()
    fendetail.title("Détail d'un message")
    fendetail.geometry('490x150+' + str(int((largeur / 2) - 490 / 2)) + '+' + str(int((hauteur / 2) - (150 / 2))))
    fendetail.protocol('WM_DELETE_WINDOW', quitdetail)
    fendetail.resizable(width=False, height=False)
    heureLabel = Label(fendetail, text='Heure : ')
    heureLabel.grid(row=0, column=0, sticky='E')
    heurevalLabel = Label(fendetail, text=heure)
    heurevalLabel.grid(row=0, column=1, sticky='W')
    emetLabel = Label(fendetail, text='De : ')
    emetLabel.grid(row=1, column=0, sticky='E')
    emetvalueLabel = Label(fendetail, text=emeteur)
    emetvalueLabel.grid(row=1, column=1, sticky='W')
    msgLabel = Label(fendetail, text='Message : ')
    msgLabel.grid(row=2, column=0, sticky='N,E')
    msgValue = Text(fendetail, width='50', height='4')
    msgValue.grid(row=2, column=1)
    msgValue.insert(END, message)
    yscrollbarlabor = ttk.Scrollbar(fendetail, command=msgValue.yview)
    yscrollbarlabor.grid(row=2, column=2, sticky=(N, S))
    msgValue['yscrollcommand'] = yscrollbarlabor.set
    quitButton = ttk.Button(fendetail, text='Sortie', command=quitdetail)
    quitButton.grid(row=3, column=0, columnspan=2)


def quitdetail():  # sortie de la visualisation detaillée
    detail.configure(state=DISABLED)
    fendetail.destroy()
    execute()


def sortielogon():  # sortie de la procedure de connexion
    fenlog.destroy()
    fen1.destroy()


def selogguer():  # Construction interface fenetre de connexion
    global passwordEntry, listUser, fenlog
    sortie.configure(state=DISABLED)
    new.configure(state=DISABLED)
    users = []
    log = SQLretriever("SELECT username FROM users ORDER BY username;", host, user, password, database)
    querylog = log.retrieve()
    toaddlog = ''
    for l in querylog:
        toaddlog = l[0]
        users.append(toaddlog)

    fen1.iconify()
    fenlog = Toplevel()
    fenlog.title("Identifiez vous")
    fenlog.geometry('340x338+' + str(int((largeur / 2) - 340 / 2)) + '+' + str(int((hauteur / 2) - (338 / 2))))
    fenlog.protocol('WM_DELETE_WINDOW', sortielogon)
    fenlog.resizable(width=False, height=False)
    log = os.getcwd() + '/Ressources/logocrom.png'
    im = PhotoImage(file=log)
    myvar = tkinter.Label(fenlog, image=im)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    myvar.image = (im)
    buttlog = ttk.Button(fenlog, text='OK', command=saisiepassword)
    buttlog.place(relx=0.5, rely=0.75, anchor=CENTER)
    listUser = Combobox(fenlog, values=users, state='readonly')
    listUser.place(relx=0.5, rely=0.25, anchor=CENTER)
    buttcfg = ttk.Button(fenlog, text='Config', command=changeConfig)
    buttcfg.place(relx=0.95, rely=0.95, anchor=E)

    passwordEntry = Entry(fenlog, text='Password', show='*')
    passwordEntry.place(relx=0.5, rely=0.5, anchor=CENTER)
    passwordEntry.delete(0, END)
    passwordEntry.bind('<Return>', bindsaisiepassword)
    passwordEntry.bind('<KP_Enter>', bindsaisiepassword)


def execute():  # boucle principale. Mise à jour de l'interface de fen1, attente 1 minutes puis appel d'elle même
    global count
    item = ''
    ctlocal = 0
    detail.configure(state=DISABLED)
    lstalarme.delete(*lstalarme.get_children())
    lstusers.delete(*lstusers.get_children())
    requete = "SELECT date, long_desc, emet, dest FROM message WHERE dest='Tous' OR dest='" + usr + "' OR emet='" + usr + "';"
    exe = SQLretriever(requete, host, user, password, database)
    querry = exe.retrieve()
    for j in querry:
        if j[2] == usr:
            toadd = j[0]
            if (('\n' in j[1][0:len(j[1]) - 1]) or (len(j[1]) > 94)):
                item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('emis', 'plus'))
            else:
                item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('emis'))

            ctlocal = ctlocal + 1
        elif j[2] == 'Admin':
            toadd = j[0]
            if (('\n' in j[1][0:len(j[1]) - 1]) or (len(j[1]) > 94)):
                item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('admin', 'plus'))
            else:
                item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('admin'))

            ctlocal = ctlocal + 1
        else:
            if j[3] == usr:
                toadd = j[0]
                if (('\n' in j[1][0:len(j[1]) - 1]) or (len(j[1]) > 94)):
                    item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('recudirect', 'plus'))
                else:
                    item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('recudirect'))
            else:
                toadd = j[0]
                if (('\n' in j[1][0:len(j[1]) - 1]) or (len(j[1]) > 94)):
                    item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('recu', 'plus'))
                else:
                    item = lstalarme.insert('', 'end', text=toadd, values=(j[2], j[1]), tag=('recu'))
            ctlocal = ctlocal + 1

    if ctlocal != count:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        count = ctlocal
    lstalarme.see(item)
    reqlog = SQLretriever("SELECT username,actif FROM users ORDER BY username;", host, user, password, database)
    querylog = reqlog.retrieve()

    for l in querylog:

        if l[1] == 'n':
            item = lstusers.insert('', 'end', text=l[0], tag=('inact'))
        else:
            item = lstusers.insert('', 'end', text=l[0], tag=('actif'))

    lstusers.tag_configure('inact', image=inactifimg)
    lstusers.tag_configure('actif', image=actifimg)

    lstalarme.tag_configure('plus', image=ico)
    lstalarme.tag_configure('admin', background='peachpuff')
    lstalarme.tag_configure('emis', background='white')
    lstalarme.tag_configure('recudirect', background='lightgrey')
    lstalarme.tag_configure('recu', background='whitesmoke')
    fen1.after(60000, execute)


def quitprog():  # nettoyage de l'interface avant sortie du programme
    requete2 = "UPDATE `alarme`.`users` SET `actif`='n' WHERE `username`='" + usr + "';"
    desactivation = SQLretriever(requete2, host, user, password, database)
    desactivation.update()
    msg = usr + ' est maintenant déconnecté du chat.'
    tkinter.messagebox.showinfo(title='Sortie', message=msg)
    fen1.destroy()


def cannew():  # cancel new alarme
    lstusers.bind('<Double-Button-1>', dbl)
    fennew.destroy()
    sortie.configure(state=NORMAL)
    new.configure(state=NORMAL)
    execute()


def newalarme(destinataire='Tous'):  # interface nouveau message
    global fennew, dat_entry, desc_entry, listUser2
    if destinataire == '':
        destinataire = 'Tous'

    sortie.configure(state=DISABLED)
    new.configure(state=DISABLED)
    fennew = Toplevel()
    fennew.title("Saisie d'un nouveau massage")
    fennew.geometry('570x150+' + str(int((largeur / 2) - 570 / 2)) + '+' + str(int((hauteur / 2) - (150 / 2))))
    fennew.protocol('WM_DELETE_WINDOW', cannew)
    fennew.resizable(width=False, height=False)
    dat_label = Label(fennew, text='JJ/MM/AAAA hh:mm : ')
    dat_label.grid(row=1, column=0, sticky='E')
    dat_entry = Entry(fennew)
    dat_entry.grid(row=1, column=1, sticky='W')
    dat_entry.insert(0, strftime("%d/%m/%Y %H:%M"))
    dat_entry.configure(state=DISABLED)
    desc_label = Label(fennew, text='Message (600 max) : ')
    desc_label.grid(row=2, column=0, sticky='NE')
    desc_entry = Text(fennew, height=4, width=50)
    desc_entry.grid(row=2, column=1)
    yscrollbar = ttk.Scrollbar(fennew, command=desc_entry.yview)
    yscrollbar.grid(row=2, column=2, sticky=(N, S))
    desc_entry['yscrollcommand'] = yscrollbar.set
    cancel = ttk.Button(fennew, text='Annuler', command=cannew)
    cancel.grid(row=3, column=0)
    valider = ttk.Button(fennew, text='Valider et envoyer', command=update)
    valider.grid(row=3, column=1)
    users = []
    reqlog = SQLretriever("SELECT username FROM users ORDER BY username;", host, user, password, database)
    querylog = reqlog.retrieve()
    users.append('Tous')
    toaddlog = ''
    for l in querylog:
        toaddlog = l[0]
        users.append(toaddlog)
    userLabel = Label(fennew, text="Choisissez un destinataire : ")
    userLabel.grid(row=0, column=0, sticky='E')
    listUser2 = Combobox(fennew, values=users, state='readonly')
    listUser2.grid(row=0, column=1, sticky='W')
    listUser2.set(destinataire)


def update():  # mise à jour de la base avec le nouveau message
    date = dat_entry.get()
    description = desc_entry.get('1.0', END)
    description = description[0:len(description) - 1]
    destinataire = listUser2.get()
    description2 = ''
    if len(date) > 16:
        date = date[0:16]
    if len(description) > 600:
        description = description[0:600]
    for i in range(len(description)):
        if description[i] != "'":
            description2 = description2 + description[i]
        else:
            description2 = description2 + "\xb4"
    requete = "INSERT INTO `alarme`.`message` (`date`, `long_desc`, `emet`, `dest`) VALUES ('" + date + "', '" + description2 + "', '"\
                                                                                                    + usr + "', '" + destinataire + "');"
    inserter = SQLretriever(requete, host, user, password, database)
    inserter.update()
    sortie.configure(state=NORMAL)
    new.configure(state=NORMAL)
    fennew.destroy()
    lstusers.bind('<Double-Button-1>', dbl)
    execute()


def bindsaisiepassword(event):  # binding valisation du mot de passe
    saisiepassword()


def saisiepassword():  # Controle du mot de passe utilisateur
    global usr
    paswd = passwordEntry.get()
    if not paswd:
        tkinter.messagebox.showwarning(title='Identification', message='Les mots de passes vides sont interdits')
        fenlog.destroy()
        fen1.destroy()
        sys.exit()
    else:
        usr = listUser.get()
        reqpassword = "SELECT pwd FROM users WHERE username='" + usr + "';"
        dbpassword = SQLretriever(reqpassword, host, user, password, database)
        querypassword = dbpassword.retrieve()
        for l in querypassword:
            if paswd != l[0]:
                tkinter.messagebox.showwarning(title='Identification', message='Mot de passe Erronné')
                fenlog.destroy()
                fen1.destroy()
            else:

                requete2 = "UPDATE `alarme`.`users` SET `actif`='o' WHERE `username`='" + usr + "';"
                activation = SQLretriever(requete2, host, user, password, database)
                activation.update()
                fenlog.destroy()
                sortie.configure(state=NORMAL)
                new.configure(state=NORMAL)
                fen1.deiconify()
                execute()


def dblnew():  # recuperation de l'utilisateur cliqué etdesactivation du double click
    idx = lstusers.focus()
    userselect = lstusers.item(idx)['text']
    lstusers.bind('<Double-Button-1>', func=NONE)
    newalarme(userselect)


def dbl(event):  # interception de l'evenement doubleclick dans le listuser
    dblnew()

#programme principal

config = readConfig()
host = config[0]
user = ''  # username de la base MySQL
password = ''  # password de la base MySQL
database = ''  # base de données du serveur MySQL à utiliser
sound_file = config[1]


#construction de l'interface principale
actif_img = os.getcwd() + '/Ressources/actif.png'
inactif_img = os.getcwd() + '/Ressources/inactif.png'
icone_file = os.getcwd() + '/Ressources/IcChatCROM.gif'
plus_file = os.getcwd() + '/Ressources/plus.png'
fen1 = tkinter.Tk()
titre = 'Liste des messages'
fen1.title(titre)
fen1.option_add('*tearOff', FALSE)
img = tkinter.PhotoImage(file=icone_file)
actifimg = tkinter.PhotoImage(file=actif_img)
inactifimg = tkinter.PhotoImage(file=inactif_img)
ico = tkinter.PhotoImage(file=plus_file)
fen1.tk.call('wm', 'iconphoto', fen1._w, img)
fen1.protocol("WM_DELETE_WINDOW", quitprog)
largeur = fen1.winfo_screenwidth()
hauteur = fen1.winfo_screenheight()
fen1.geometry('985x300+' + str(int((largeur / 2) - 985 / 2)) + '+' + str(int((hauteur / 2) - (300 / 2))))
fen1.minsize(420, 300)
fen1.resizable(width=True, height=False)
menubar = Menu(fen1)
fen1['menu'] = menubar
menu_action = Menu(menubar)
menubar.add_cascade(menu=menu_action, label='Action')
menu_action.add_command(label='Nouvelle Alarme', command=dblnew)
menu_action.add_command(label='Configuration', command=configprog)
menu_action.add_command(label='Quitter', command=quitprog)

lstalarme = Treeview(fen1, selectmode='browse')
lstalarme['columns'] = ('User', 'Message')
lstalarme.heading('#0', text='Heure', anchor='w')
lstalarme.column('#0', anchor='w')
lstalarme.heading('User', text='User')
lstalarme.column('User', anchor='w', width=100)
lstalarme.column('User', stretch=tkinter.YES)
lstalarme.heading('Message', text='Message')
lstalarme.column('Message', anchor='w', width=668)
lstalarme.grid(row=0, column=0, sticky=(N, S, W, E))
fen1.grid_columnconfigure(0, weight=1)
yscrollbar = ttk.Scrollbar(fen1, command=lstalarme.yview)
yscrollbar.grid(row=0, column=1, sticky=(N, S))
lstalarme['yscrollcommand'] = yscrollbar.set
lstusers = Treeview(fen1, selectmode='browse')
lstusers['columns'] = ()
lstusers.heading('#0', text='Membres', anchor='w')
lstusers.column('#0', anchor='w')
lstusers.grid(row=0, column=2, sticky=(N, S, W, E))
sortie = ttk.Button(fen1, text='Quitter', command=quitprog)
sortie.place(relx=0.2, rely=0.8)
detail = ttk.Button(fen1, text='Détail', command=detailmsg)
detail.place(relx=0.4, rely=0.8)
detail.configure(state=DISABLED)
new = ttk.Button(fen1, text='Nouveau Message', command=dblnew)
new.place(relx=0.6, rely=0.8)
lstalarme.bind('<<TreeviewSelect>>', sellstalarme)
lstalarme.bind('<Double-Button-1>', dblsellstalarme)
lstusers.bind('<Double-Button-1>', dbl)


#lancement de la procedure de connexion

selogguer()

#lancement de l'interface principale
fen1.mainloop()
