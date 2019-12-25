import PySimpleGUI as sg 
from apps_instaPostStyle2 import instaPostStyle2MainProgram
import random
sg.ChangeLookAndFeel('DarkAmber') 

DefaultWidth = 40

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Bantuan', ['Tentang Kami', 'Bantuan1']], 
            ]   
layout = [      
    [sg.Menu(menu_def, tearoff=True)],      
    #[sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],   
    [sg.Text('Text Editor', justification='center', size=(DefaultWidth,1),font=("Helvetica",10), relief=sg.RELIEF_RIDGE), 
        sg.T(' '), sg.T(' '),
        sg.Text('Custom Logo', size=(DefaultWidth, 1), justification='center', font=("Helvetica", 10), relief=sg.RELIEF_RIDGE),
        sg.T(' '), sg.T(' '),
        sg.Text('Background Section', size=(DefaultWidth, 1), justification='center', font=("Helvetica", 10), relief=sg.RELIEF_RIDGE),
        ],
    
    [sg.InputText(('Masukkan Judul Besar'),size=(DefaultWidth,2)),
        sg.T(' '), sg.T(' '),
        sg.Text('Logo yang biasa digunakan', size=(DefaultWidth, 1)),
        sg.T(' '), sg.T(' '),
        sg.Text('Pilih Background sesuai kategori', size=(DefaultWidth, 1)),
        ],
    [sg.InputOptionMenu(('-- Pilih Font --', 'Archivo Black','Comfortaa','Great Vibes','Indie Flower','Kaushan Script','Love Ya','Marck Script','Muli','Saira Stencil One')),
        sg.T('   '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '),
        sg.Checkbox('Logo AiDesign', size=(DefaultWidth,1), default=True, disabled=True),
        sg.T(' '),
        sg.InputOptionMenu(('-- Pilih Kategori --', 'City', 'Dawn', 'Dusk', 'Night', 'Light','Dark','Nature')),
        ],
    [sg.Checkbox('Font Judul Otomatis', size=(DefaultWidth,1), default=True),
        sg.T(' '),
        sg.Checkbox('Logo Muslim Designer Community', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Text('Pilih Background sendiri', size=(DefaultWidth, 1)),
        ],
    [sg.T(' ', size=(41,1)),
        sg.T('    '),
        sg.Checkbox('Logo Yuk Share', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Text('Background :'), sg.Input(size=(15,1)), sg.FileBrowse()
        ],

    [sg.InputText(('Masukkan Sub Judul Kecil'),size=(DefaultWidth,2)),
        sg.T(' '), sg.T(' '),
        sg.Text('Upload logo sendiri', size=(DefaultWidth, 1))],
    [sg.InputOptionMenu(('-- Pilih Font --', 'Archivo Black','Comfortaa','Great Vibes','Indie Flower','Kaushan Script','Love Ya','Marck Script','Muli','Saira Stencil One')),
        sg.T('   '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '),
        sg.Text('Logo 1 ', size=(6, 1)), sg.Input(size=(20,1)), sg.FileBrowse()],
    [sg.Checkbox('Font Sub Judul Otomatis', size=(DefaultWidth,1), default=True),
        sg.T(' '),
        sg.Text('Logo 2 ', size=(6, 1)), sg.Input(size=(20,1)), sg.FileBrowse()],
    [sg.T(' ', size=(42,1)),
        sg.T('  '),
        sg.Checkbox('Logo #Hashtag '), sg.Input(default_text='AiDesign Generator',size=(22,1))],
    [sg.T(' ')],
    [sg.T(' ', size=(45,1)),
        sg.Submit(button_text='Generate Design'),
        sg.T(' ', size=(12,1)),
        sg.Exit(),
        ],
]

layout2 = [
    [sg.Text('Custom Logo', size=(30, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Logo yang biasa digunakan')],
    [sg.Checkbox('Logo AiDesign', size=(DefaultWidth,1))],
    [sg.Checkbox('Logo MDC', size=(DefaultWidth,1))],
    [sg.Checkbox('Logo Yuk Share', size=(DefaultWidth,1))],

]

# sg.PopupScrolled('Hallo Semuanya ^^', 
#     'Program ini adalah program gratis.',
#     'Mohon gunakan dengan bijak. Semoga bermanfaat ^^',
#     'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',
#     'More at http://github.com/stacia')

window = sg.Window('AI Design : Your Instant Design Buddy', layout, default_element_size=(DefaultWidth, 1), grab_anywhere=False)      
# window2 = sg.Window('Template Section', layout2, default_element_size=(DefaultWidth, 1), grab_anywhere=False)      

dictionaryFont = {
    'Archivo Black' : 'Font-lib/Archivo_Black/ArchivoBlack-Regular.ttf',
    'Comfortaa' : 'Font-lib/Comfortaa/Comfortaa-SemiBold.ttf',
    'Great Vibes' : 'Font-lib/Great_Vibes/GreatVibes-Regular.ttf',
    'Indie Flower' : 'Font-lib/IndieFlower/IndieFlower.ttf',
    'Kaushan Script' : 'Font-lib/Kaushan_Script/KaushanScript-Regular.ttf',
    'Love Ya' : 'Font-lib/Love_Ya_Like_A_Sister/LoveYaLikeASister-Regular.ttf',
    'Marck Script' : 'Font-lib/Marck_Script/MarckScript-Regular.ttf',
    'Muli' : 'Font-lib/Muli/Muli-Bold.ttf',
    'Saira Stencil One' : 'Font-lib/Saira_Stencil_One/SairaStencilOne-Regular.ttf',
    }

# print(dictionaryFont['Archivo Black']) # Result is Font-lib/Archivo_Black/ArchivoBlack-Regular.ttf
# print(dictionaryFont[2]) # KeyError

listAvailableFont = ('Archivo Black','Comfortaa','Great Vibes','Indie Flower','Kaushan Script','Love Ya','Marck Script','Muli','Saira Stencil One')
randomFont = dictionaryFont[listAvailableFont[random.randint(0,len(listAvailableFont)-1)]]

while True:
    event, values = window.read()
    # event2, values2 = window2.read()
    print('-- // -- / START / -- // --')
    print(event)
    if values[5] == True: # Random title font
        isTitleFont = randomFont
    else:
        isTitleFont = dictionaryFont[values[2]]

    if values[12] == True: # Random sub title font
        isSubTitleFont = randomFont
    else:
        isSubTitleFont = dictionaryFont[values[10]]


    for key,val in values.items():
        print (key, val)
    if event in (None,'Exit'):
        break
    elif event == 'Tentang Kami...':
        sg.PopupScrolled('Tentang Pengembang.', 
            'Program ini adalah program gratis.',
            'Mohon gunakan dengan bijak. Semoga bermanfaat ^^',
            'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',
            'More at http://github.com/stacia')
    elif event == 'Bantuan...':
        sg.Popup('Silahkan kunjungi http://github.com/stacia',
            'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',)
    elif event == 'Generate Design':
        print('------------------------------------')
        print('----- Design Generated by user -----')
        print(isTitleFont)
        print(isSubTitleFont)
        print(values[1], values[9])
        instaPostStyle2MainProgram(
            titleText = values[1],
            fontTitlePath = isTitleFont,
            subTitleText = values[9],
            fontSubTitlePath = isSubTitleFont,
            logoAiDesign = None,
            logoMDC = values[6],
            logoYukShare = values[7],
            customLogo1 = values[11],
            customLogo2 = values[13],
            customHastagLogo = values[15],
            backgroundCategory = values[4],
            backgroundImage = values[8],
            )

# List index of values
# 0 None
# 1 Masukkan Judul Besar
# 2 -- Pilih Font --
# 3 True
# 4 -- Pilih Kategori --
# 5 True
# 6 False
# 7 False
# 8 
# Browse 
# 9 Masukkan Sub Judul Kecil
# 10 -- Pilih Font --
# 11 
# Browse0 
# 12 True
# 13 
# Browse1 
# 14 False
# 15 AiDesign Generator