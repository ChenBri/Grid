#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on February 18, 2023, at 17:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from functions
# Importing libraries
import random
import copy

# Create a grid
def create_grid(x, y, box_size_x, box_size_y):
    
    start_x = int((x / 2 - x) + (box_size_x / 2))
    start_y = int((y / 2 - y) + (box_size_y / 2))
    x_limit = int(x / 2)
    y_limit = int(y / 2)
    
    grid = []

    while start_x < x_limit:
        while start_y < y_limit:
            grid.append([start_x, start_y])
            start_y += box_size_y

        start_y = int((y / 2 - y) + (box_size_y / 2))
        start_x += box_size_x

    return grid

# Call the function
grid = create_grid(1900, 1000, 190, 100)


# Create a color palette
def create_color_palette(*colors):
    color_palette = []
    for color in colors:
        color_palette.append(color)

    return color_palette

# Call the function
color_palette = create_color_palette('green', 'red', 'blue','saddlebrown', '#ff94c0' , 'cyan', 'purple', 'orange', 'yellow')


# Randomize the grid locations function
def randomize_location(loc, val_x, val_y):
    loc[0] = random.randint(loc[0]-val_x, loc[0]+val_x)
    loc[1] = random.randint(loc[1]-val_y, loc[1]+val_y)
    return [loc[0], loc[1]]

# Run 'Before Experiment' code from trials
# Define the number of training trials
num_of_training = 4

# Define the number of the experiment trials
num_of_trials = 4
# Run 'Before Experiment' code from shape
shapeOrientation = 0
shapeName = ''
# Run 'Before Experiment' code from reset_success_2
answers = []
# Run 'Before Experiment' code from update_answer
def answerType(text, bool):
    if bool:
        text.text = 'V'
        text.color = 'green'
    else:
        text.text = 'X'
        text.color = 'red'
# Run 'Before Experiment' code from code_answer
answerVariant = ''
pressedKey = ''
numOfCorrectAnswers = 0
numOfWrongAnswers = 0
totalNumOfLoops = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'grid'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'gender': ["man", "woman", "other"],
    'age': '',
    'handedness': ["right-handed", "left-handed"],
    'education (years)': '',
    'shape': ["square", "diamond"],
    'controls': ["regular", "reversed"],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\chenb\\Desktop\\Eilay\\Grid Psychology Experiment\\grid_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.5059, 0.5059, 0.5059], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "create_data" ---
# Run 'Begin Experiment' code from shape
if expInfo["shape"] == 'square':
    shapeOrientation = 0
    shapeName = 'Square'
else:
    shapeOrientation = 45
    shapeName = 'Diamond'
# Run 'Begin Experiment' code from controls
identical_key = 0
non_identical_key = 0

if expInfo['controls'] == 'regular':
    identical_key = 112
    non_identical_key = 113
    print('Regular Controls')
    print('P = Identical | Q = Non-Identical')
    
elif expInfo['controls'] == 'reversed':
    identical_key = 113
    non_identical_key = 112
    print('Reversed Controls')
    print('Q = Identical | P = Non-Identical')
    


# --- Initialize components for Routine "instructions_start_1" ---
inst1_square = visual.TextStim(win=win, name='inst1_square',
    text='במטלה זו, כל צעד יחל בסימן + במרכז המסך.\nיש להקפיד להסתכל למרכז המסך לאורך כל הניסוי.\n\nלאחר מכן יופיע מסך עם ריבועים צבעוניים.\nלאחר שמסך זה יעלם, יופיע מסך נוסף עם ריבועים צבעוניים.\nעליך להחליט האם הריבועים במסך השני זהים לחלוטין בצבעם לריבועים במסך הראשון.\nבמידה ויהיה שינוי, הוא ישפיע על צבעו של ריבוע אחד בלבד.\n\nעלייך לבצע את המטלה באופן הטוב ביותר שאת\\ה יכול\\ה. \n\nבמידה ויש לך שאלות, שאל\\י את הנסיינית כעת.\nבמידה ולא, לחצ\\י רווח במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.037, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
inst1_diam = visual.TextStim(win=win, name='inst1_diam',
    text='במטלה זו, כל צעד יחל בסימן + במרכז המסך.\nיש להקפיד להסתכל למרכז המסך לאורך כל הניסוי.\n\nלאחר מכן יופיע מסך עם מעוינים צבעוניים.\nלאחר שמסך זה יעלם, יופיע מסך נוסף עם מעוינים צבעוניים.\nעליך להחליט האם המעוינים במסך השני זהים לחלוטין בצבעם למעוינים במסך הראשון.\nבמידה ויהיה שינוי, הוא ישפיע על צבעו של מעוין אחד בלבד.\n\nעלייך לבצע את המטלה באופן הטוב ביותר שאת\\ה יכול\\ה. \n\nבמידה ויש לך שאלות, שאל\\י את הנסיינית כעת.\nבמידה ולא, לחצ\\י רווח במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.037, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_start_2" ---
inst2_square = visual.TextStim(win=win, name='inst2_square',
    text='אם צבעי כל הריבועים במסך השני זהים לצבעם במסך הראשון, לחצ\\י על \'P\' במקלדת.\nאם צבעו של אחד הריבועים השתנה, לחצ\\י על \'Q\' במקלדת.\nאם ברצונך לראות את המסך הראשון שוב לפני תשובה סופית, לחצ\\י על \'רווח\' במקלדת. \nאין הגבלה על מספר הפעמים שניתן ללחוץ \'רווח\'.\n\nבסוף כל צעד תופיע הודעה:\n"?ready"\nהמכינה לקראת המסך הבא.\n\nבמידה ויש לך שאלות, שאל\\י את הנסיינית כעת.\nבמידה ולא, לחצ\\י רווח במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.037, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
inst2_diam = visual.TextStim(win=win, name='inst2_diam',
    text='אם צבעי כל המעוינים במסך השני זהים לצבעם במסך הראשון, לחצ\\י על \'P\' במקלדת.\nאם צבעו של אחד המעוינים השתנה, לחצ\\י על \'Q\' במקלדת.\nאם ברצונך לראות את המסך הראשון שוב לפני תשובה סופית, לחצ\\י על \'רווח\' במקלדת. \nאין הגבלה על מספר הפעמים שניתן ללחוץ \'רווח\'.\n\nבסוף כל צעד תופיע הודעה:\n"?ready"\nהמכינה לקראת המסך הבא.\n\nבמידה ויש לך שאלות, שאל\\י את הנסיינית כעת.\nבמידה ולא, לחצ\\י רווח במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.037, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_training" ---
inst_training = visual.TextStim(win=win, name='inst_training',
    text='כעת נתרגל את השימוש בלחצים "זהים" (P) ו"שונים" (Q).\n\nכל צעד יחל בסימן + במרכז המסך. \nלאחר מכן, יופיעו שתי צורות על המסך.\nבמידה והצורות זהות בצורתן ובצבען - אנא לחצ\\י "זהים", P במקלדת.\nבמידה והצורות שונות בצורתן ו\\או בצבען - אנא לחצ\\י "שונים", Q במקלדת.\n\nבמידה ויש לך שאלות, שאל\\י את הנסיינית כעת. \nבמידה ואת\\ה מוכן להתחיל, לחצ\\י "רווח" במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.037, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
skip_inst_training = keyboard.Keyboard()

# --- Initialize components for Routine "reset_success" ---

# --- Initialize components for Routine "fixation" ---
fixation_point = visual.TextStim(win=win, name='fixation_point',
    text='Ready?\n+',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "steps" ---
circle_1 = visual.ShapeStim(
    win=win, name='circle_1',units='pix', 
    size=(20, 20), vertices='circle',
    ori=0.0, pos=(50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0824, -0.6627, 0.7725],
    opacity=None, depth=0.0, interpolate=True)
triangle_1 = visual.ShapeStim(
    win=win, name='triangle_1',units='pix', 
    size=(20, 20), vertices='triangle',
    ori=0.0, pos=(50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0824, -0.6627, 0.7725],
    opacity=None, depth=-1.0, interpolate=True)
square_1 = visual.Rect(
    win=win, name='square_1',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=0.0, pos=(50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0824, -0.6627, 0.7725],
    opacity=None, depth=-2.0, interpolate=True)
circle_2 = visual.ShapeStim(
    win=win, name='circle_2',units='pix', 
    size=(20, 20), vertices='circle',
    ori=0.0, pos=(-50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.9216, 0.9216, 0.7255],
    opacity=None, depth=-3.0, interpolate=True)
triangle_2 = visual.ShapeStim(
    win=win, name='triangle_2',units='pix', 
    size=(20, 20), vertices='triangle',
    ori=0.0, pos=(-50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0824, -0.6627, 0.7725],
    opacity=None, depth=-4.0, interpolate=True)
square_2 = visual.Rect(
    win=win, name='square_2',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=0.0, pos=(-50, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0824, -0.6627, 0.7725],
    opacity=None, depth=-5.0, interpolate=True)
# Run 'Begin Experiment' code from key_press
thisKey = ''

# --- Initialize components for Routine "answer_feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "calculate_success" ---
calculate_text = visual.TextStim(win=win, name='calculate_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);

# --- Initialize components for Routine "instructions_t" ---
inst_t = visual.TextStim(win=win, name='inst_t',
    text='כעת יחל שלב האימון. מטרת שלב זה לוודא כי המטלה ברורה. \nבשלב זה ניתן לעצור בכל זמן ע"מ לשאול שאלות.\n\nלחצ\\י "רווח" במקלדת ע"מ להתחיל. \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
skip_t = keyboard.Keyboard()

# --- Initialize components for Routine "images_randomization_t" ---

# --- Initialize components for Routine "fixation" ---
fixation_point = visual.TextStim(win=win, name='fixation_point',
    text='Ready?\n+',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "redisplay_blank" ---
redisplay_blank_text = visual.TextStim(win=win, name='redisplay_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "image_1_t" ---
img_1_bg_t = visual.Rect(
    win=win, name='img_1_bg_t',units='pix', 
    width=(1920, 1080)[0], height=(1920, 1080)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.5059, 0.5059, 0.5059],
    opacity=None, depth=0.0, interpolate=True)
img1_b1_t = visual.Rect(
    win=win, name='img1_b1_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
img1_b2_t = visual.Rect(
    win=win, name='img1_b2_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
img1_b3_t = visual.Rect(
    win=win, name='img1_b3_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
img1_b4_t = visual.Rect(
    win=win, name='img1_b4_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "blank" ---
blank_text = visual.TextStim(win=win, name='blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "image_2_t" ---
img2_bg_t = visual.Rect(
    win=win, name='img2_bg_t',units='pix', 
    width=(1920, 1080)[0], height=(1920, 1080)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.5059, 0.5059, 0.5059],
    opacity=None, depth=0.0, interpolate=True)
img2_b1_t = visual.Rect(
    win=win, name='img2_b1_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
img2_b2_t = visual.Rect(
    win=win, name='img2_b2_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
img2_b3_t = visual.Rect(
    win=win, name='img2_b3_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
img2_b4_t = visual.Rect(
    win=win, name='img2_b4_t',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
redisplay_key_t = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_answer_t
current_key = 0

# --- Initialize components for Routine "instructions_exp" ---
exp_text = visual.TextStim(win=win, name='exp_text',
    text='שלב האימון הסתיים, כעת יתחיל שלב הניסוי. \n\nבמידה ויש לך שאלות נוספות, שאל\\י את הנסיינית כעת. \nלא יהיה ניתן לעצור לשאלות נוספות בזמן שלב הניסוי. \n\nבמידה ואת\\ה מוכנ\\ה להתחיל, לחצ\\י "רווח" במקלדת.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "images_randomization" ---

# --- Initialize components for Routine "fixation" ---
fixation_point = visual.TextStim(win=win, name='fixation_point',
    text='Ready?\n+',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "redisplay_blank" ---
redisplay_blank_text = visual.TextStim(win=win, name='redisplay_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "image_1" ---
img1_bg = visual.Rect(
    win=win, name='img1_bg',units='pix', 
    width=(1920, 1080)[0], height=(1920, 1080)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.5059, 0.5059, 0.5059],
    opacity=None, depth=0.0, interpolate=True)
img1_b1 = visual.Rect(
    win=win, name='img1_b1',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
img1_b2 = visual.Rect(
    win=win, name='img1_b2',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
img1_b3 = visual.Rect(
    win=win, name='img1_b3',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
img1_b4 = visual.Rect(
    win=win, name='img1_b4',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "blank" ---
blank_text = visual.TextStim(win=win, name='blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "image_2" ---
img2_bg = visual.Rect(
    win=win, name='img2_bg',units='pix', 
    width=(1920, 1080)[0], height=(1920, 1080)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.5059, 0.5059, 0.5059],
    opacity=None, depth=0.0, interpolate=True)
img2_b1 = visual.Rect(
    win=win, name='img2_b1',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
img2_b2 = visual.Rect(
    win=win, name='img2_b2',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
img2_b3 = visual.Rect(
    win=win, name='img2_b3',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
img2_b4 = visual.Rect(
    win=win, name='img2_b4',units='pix', 
    width=(20, 20)[0], height=(20, 20)[1],
    ori=shapeOrientation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
redisplay_key = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_answer
current_key = 0

# --- Initialize components for Routine "finish" ---
finish_text = visual.TextStim(win=win, name='finish_text',
    text='מטלה זו הסתיימה, נא עדכן\\י את הנסיינית.\nתודה רבה.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=800.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "create_data" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from trials
# Create trials
trial_order = []
training_order = []

# Regular trials
for trial in range(num_of_trials):
    if trial >= num_of_trials/2:
        trial_order.append(1)
    else:
        trial_order.append(0)

# Training trials
for trial in range(num_of_training):
    if trial >= num_of_training/2:
        training_order.append(1)
    else:
        training_order.append(0)

# Shuffle the trials order
random.shuffle(trial_order)
random.shuffle(training_order)
# Run 'Begin Routine' code from training
# Order:           1          0          1          0             0           0              1          1
shape_answers = [  1,         0,         1,         0,            0,          0,             1,         1]
shape1_shape = ['square', 'square'  , 'circle', 'triangle'   ,'triangle' ,'square'      ,'square' , 'triangle']
shape2_shape = ['square', 'triangle', 'circle', 'circle'     , 'circle'  , 'triangle'   , 'square', 'triangle']
shape1_color = ['red'   , 'red'     , 'blue'  , 'saddlebrown', 'cyan'    , 'purple'     , 'orange', 'yellow']
shape2_color = ['red'   , 'purple'  , 'blue'  , 'green'      , 'cyan'    , 'saddlebrown', 'orange', 'yellow']


# keep track of which components have finished
create_dataComponents = []
for thisComponent in create_dataComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "create_data" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in create_dataComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "create_data" ---
for thisComponent in create_dataComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "create_data" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_start_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructions_start_1Components = [inst1_square, inst1_diam, key_resp]
for thisComponent in instructions_start_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_start_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst1_square* updates
    if inst1_square.status == NOT_STARTED and shapeName=='Square':
        # keep track of start time/frame for later
        inst1_square.frameNStart = frameN  # exact frame index
        inst1_square.tStart = t  # local t and not account for scr refresh
        inst1_square.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst1_square, 'tStartRefresh')  # time at next scr refresh
        inst1_square.setAutoDraw(True)
    
    # *inst1_diam* updates
    if inst1_diam.status == NOT_STARTED and shapeName=='Diamond':
        # keep track of start time/frame for later
        inst1_diam.frameNStart = frameN  # exact frame index
        inst1_diam.tStart = t  # local t and not account for scr refresh
        inst1_diam.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst1_diam, 'tStartRefresh')  # time at next scr refresh
        inst1_diam.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_start_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_start_1" ---
for thisComponent in instructions_start_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_start_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_start_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instructions_start_2Components = [inst2_square, inst2_diam, key_resp_2]
for thisComponent in instructions_start_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_start_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst2_square* updates
    if inst2_square.status == NOT_STARTED and shapeName=='Square':
        # keep track of start time/frame for later
        inst2_square.frameNStart = frameN  # exact frame index
        inst2_square.tStart = t  # local t and not account for scr refresh
        inst2_square.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst2_square, 'tStartRefresh')  # time at next scr refresh
        inst2_square.setAutoDraw(True)
    
    # *inst2_diam* updates
    if inst2_diam.status == NOT_STARTED and shapeName=='Diamond':
        # keep track of start time/frame for later
        inst2_diam.frameNStart = frameN  # exact frame index
        inst2_diam.tStart = t  # local t and not account for scr refresh
        inst2_diam.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst2_diam, 'tStartRefresh')  # time at next scr refresh
        inst2_diam.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_start_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_start_2" ---
for thisComponent in instructions_start_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_start_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_training" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip_inst_training.keys = []
skip_inst_training.rt = []
_skip_inst_training_allKeys = []
# keep track of which components have finished
instructions_trainingComponents = [inst_training, skip_inst_training]
for thisComponent in instructions_trainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_training" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_training* updates
    if inst_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_training.frameNStart = frameN  # exact frame index
        inst_training.tStart = t  # local t and not account for scr refresh
        inst_training.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_training, 'tStartRefresh')  # time at next scr refresh
        inst_training.setAutoDraw(True)
    
    # *skip_inst_training* updates
    waitOnFlip = False
    if skip_inst_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip_inst_training.frameNStart = frameN  # exact frame index
        skip_inst_training.tStart = t  # local t and not account for scr refresh
        skip_inst_training.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip_inst_training, 'tStartRefresh')  # time at next scr refresh
        skip_inst_training.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip_inst_training.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip_inst_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip_inst_training.status == STARTED and not waitOnFlip:
        theseKeys = skip_inst_training.getKeys(keyList=['space'], waitRelease=False)
        _skip_inst_training_allKeys.extend(theseKeys)
        if len(_skip_inst_training_allKeys):
            skip_inst_training.keys = _skip_inst_training_allKeys[-1].name  # just the last key pressed
            skip_inst_training.rt = _skip_inst_training_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_trainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_training" ---
for thisComponent in instructions_trainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_training" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeat_training = data.TrialHandler(nReps=999.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeat_training')
thisExp.addLoop(repeat_training)  # add the loop to the experiment
thisRepeat_training = repeat_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat_training.rgb)
if thisRepeat_training != None:
    for paramName in thisRepeat_training:
        exec('{} = thisRepeat_training[paramName]'.format(paramName))

for thisRepeat_training in repeat_training:
    currentLoop = repeat_training
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_training.rgb)
    if thisRepeat_training != None:
        for paramName in thisRepeat_training:
            exec('{} = thisRepeat_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "reset_success" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from reset_success_2
    answers = []
    trainingCorrectAnswers = 0
    successRate = 0
    # keep track of which components have finished
    reset_successComponents = []
    for thisComponent in reset_successComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reset_success" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reset_successComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reset_success" ---
    for thisComponent in reset_successComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "reset_success" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training_loop = data.TrialHandler(nReps=8.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='training_loop')
    thisExp.addLoop(training_loop)  # add the loop to the experiment
    thisTraining_loop = training_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_loop.rgb)
    if thisTraining_loop != None:
        for paramName in thisTraining_loop:
            exec('{} = thisTraining_loop[paramName]'.format(paramName))
    
    for thisTraining_loop in training_loop:
        currentLoop = training_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_loop.rgb)
        if thisTraining_loop != None:
            for paramName in thisTraining_loop:
                exec('{} = thisTraining_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation_point]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_point* updates
            if fixation_point.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation_point.frameNStart = frameN  # exact frame index
                fixation_point.tStart = t  # local t and not account for scr refresh
                fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_point, 'tStartRefresh')  # time at next scr refresh
                fixation_point.setAutoDraw(True)
            if fixation_point.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_point.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_point.tStop = t  # not accounting for scr refresh
                    fixation_point.frameNStop = frameN  # exact frame index
                    fixation_point.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "steps" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from shapes_creator
        currentStep = training_loop.thisN
        
        circle_1.color = triangle_1.color = square_1.color = shape1_color[currentStep]
        circle_2.color = triangle_2.color = square_2.color = shape2_color[currentStep]
        
        currentShape1 = shape1_shape[currentStep]
        currentShape2 = shape2_shape[currentStep]
        # keep track of which components have finished
        stepsComponents = [circle_1, triangle_1, square_1, circle_2, triangle_2, square_2]
        for thisComponent in stepsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "steps" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_1* updates
            if circle_1.status == NOT_STARTED and currentShape1 == 'circle':
                # keep track of start time/frame for later
                circle_1.frameNStart = frameN  # exact frame index
                circle_1.tStart = t  # local t and not account for scr refresh
                circle_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_1, 'tStartRefresh')  # time at next scr refresh
                circle_1.setAutoDraw(True)
            
            # *triangle_1* updates
            if triangle_1.status == NOT_STARTED and currentShape1 == 'triangle':
                # keep track of start time/frame for later
                triangle_1.frameNStart = frameN  # exact frame index
                triangle_1.tStart = t  # local t and not account for scr refresh
                triangle_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triangle_1, 'tStartRefresh')  # time at next scr refresh
                triangle_1.setAutoDraw(True)
            
            # *square_1* updates
            if square_1.status == NOT_STARTED and currentShape1 == 'square':
                # keep track of start time/frame for later
                square_1.frameNStart = frameN  # exact frame index
                square_1.tStart = t  # local t and not account for scr refresh
                square_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_1, 'tStartRefresh')  # time at next scr refresh
                square_1.setAutoDraw(True)
            
            # *circle_2* updates
            if circle_2.status == NOT_STARTED and currentShape2 == 'circle':
                # keep track of start time/frame for later
                circle_2.frameNStart = frameN  # exact frame index
                circle_2.tStart = t  # local t and not account for scr refresh
                circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_2, 'tStartRefresh')  # time at next scr refresh
                circle_2.setAutoDraw(True)
            
            # *triangle_2* updates
            if triangle_2.status == NOT_STARTED and currentShape2 == 'triangle':
                # keep track of start time/frame for later
                triangle_2.frameNStart = frameN  # exact frame index
                triangle_2.tStart = t  # local t and not account for scr refresh
                triangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triangle_2, 'tStartRefresh')  # time at next scr refresh
                triangle_2.setAutoDraw(True)
            
            # *square_2* updates
            if square_2.status == NOT_STARTED and currentShape2 == 'square':
                # keep track of start time/frame for later
                square_2.frameNStart = frameN  # exact frame index
                square_2.tStart = t  # local t and not account for scr refresh
                square_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_2, 'tStartRefresh')  # time at next scr refresh
                square_2.setAutoDraw(True)
            # Run 'Each Frame' code from key_press
            keys = event.getKeys()
            
            if len(keys)>0:
                for thisKey in keys:
                    current_key = ord(thisKey[0])
                    
                    # Skip to next routine
                    if current_key == identical_key or current_key == non_identical_key:
                        # P - 112 | Identical
                        if current_key == identical_key:
                            answers.append(identical_key)
                 
                        # Q - 113 | Non-Identical
                        if current_key == non_identical_key:
                            answers.append(non_identical_key)
                            
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stepsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "steps" ---
        for thisComponent in stepsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "steps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "answer_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from update_answer
        if shape1_shape[training_loop.thisN] == shape2_shape[training_loop.thisN] and shape1_color[training_loop.thisN] == shape1_color[training_loop.thisN]:
            if answers[training_loop.thisN] == identical_key:
                answerType(feedback_text, True)
            else:
                answerType(feedback_text, False)
            
        else:
            if answers[training_loop.thisN] == non_identical_key:
                answerType(feedback_text, True)
            else:
                answerType(feedback_text, False)
        
        # keep track of which components have finished
        answer_feedbackComponents = [feedback_text]
        for thisComponent in answer_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "answer_feedback" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                feedback_text.setAutoDraw(True)
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in answer_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "answer_feedback" ---
        for thisComponent in answer_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
    # completed 8.0 repeats of 'training_loop'
    
    
    # --- Prepare to start Routine "calculate_success" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from calc_success
    for trial in range(8):
        
        # Identical
        if shape_answers[trial] == 1:
            # Correct Answer
            if answers[trial] == identical_key:
                trainingCorrectAnswers += 1
        
        
        # Non-identical
        else:
            # Correct Answer
            if answers[trial] == non_identical_key:
                trainingCorrectAnswers += 1
                
    
    successRate = trainingCorrectAnswers / 8 * 100
    calculate_text.text = str(successRate) + '\n' + 'אנא פנה\י לנסיינית.'
    
    # If the participant successfully answered at least 75% of the answers
    if successRate >= 75:
        repeat_training.finished = True
        continueRoutine = False
    # keep track of which components have finished
    calculate_successComponents = [calculate_text]
    for thisComponent in calculate_successComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calculate_success" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calculate_text* updates
        if calculate_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calculate_text.frameNStart = frameN  # exact frame index
            calculate_text.tStart = t  # local t and not account for scr refresh
            calculate_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calculate_text, 'tStartRefresh')  # time at next scr refresh
            calculate_text.setAutoDraw(True)
        # Run 'Each Frame' code from calc_success
        keys = event.getKeys()
        
        if len(keys)>0:
            for thisKey in keys:
                current_key = ord(thisKey[0])
                
                # Repeat the initial training - 'r'
                if current_key == 114:  
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calculate_successComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calculate_success" ---
    for thisComponent in calculate_successComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from calc_success
    # Save success rate
    thisExp.addData('initialTraining_sucessRate', successRate)
    thisExp.addData('initialTraining_loopNum', repeat_training.thisN)
    
    
    thisExp.nextEntry()
    # the Routine "calculate_success" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 999.0 repeats of 'repeat_training'


# --- Prepare to start Routine "instructions_t" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skip_t.keys = []
skip_t.rt = []
_skip_t_allKeys = []
# keep track of which components have finished
instructions_tComponents = [inst_t, skip_t]
for thisComponent in instructions_tComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_t" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_t* updates
    if inst_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_t.frameNStart = frameN  # exact frame index
        inst_t.tStart = t  # local t and not account for scr refresh
        inst_t.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_t, 'tStartRefresh')  # time at next scr refresh
        inst_t.setAutoDraw(True)
    
    # *skip_t* updates
    waitOnFlip = False
    if skip_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skip_t.frameNStart = frameN  # exact frame index
        skip_t.tStart = t  # local t and not account for scr refresh
        skip_t.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip_t, 'tStartRefresh')  # time at next scr refresh
        skip_t.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip_t.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip_t.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip_t.status == STARTED and not waitOnFlip:
        theseKeys = skip_t.getKeys(keyList=['space'], waitRelease=False)
        _skip_t_allKeys.extend(theseKeys)
        if len(_skip_t_allKeys):
            skip_t.keys = _skip_t_allKeys[-1].name  # just the last key pressed
            skip_t.rt = _skip_t_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_tComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_t" ---
for thisComponent in instructions_tComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_t" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
show_images_t = data.TrialHandler(nReps=num_of_training, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='show_images_t')
thisExp.addLoop(show_images_t)  # add the loop to the experiment
thisShow_images_t = show_images_t.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShow_images_t.rgb)
if thisShow_images_t != None:
    for paramName in thisShow_images_t:
        exec('{} = thisShow_images_t[paramName]'.format(paramName))

for thisShow_images_t in show_images_t:
    currentLoop = show_images_t
    # abbreviate parameter names if possible (e.g. rgb = thisShow_images_t.rgb)
    if thisShow_images_t != None:
        for paramName in thisShow_images_t:
            exec('{} = thisShow_images_t[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "images_randomization_t" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from location_t
    # Randomize the grid locations
    current_grid = copy.deepcopy(grid)
    random.shuffle(current_grid)
    
    # Add randomization for each block
    # Set the block location
    for idx, block in enumerate([[img1_b1_t, img2_b1_t], [img1_b2_t, img2_b2_t], [img1_b3_t, img2_b3_t], [img1_b4_t, img2_b4_t]]):
        current_location = randomize_location(current_grid[idx], 38, 20)
        block[0].pos = block[1].pos = current_location
    # Run 'Begin Routine' code from color_t
    import random
    
    # Randomize the color palette
    random.shuffle(color_palette)
    
    # Pick 5 Random colors
    random_colors = []
    random_colors+=random.sample(color_palette, 5)
    
    # Assign the first 5 colors to the blocks
    for idx, block in enumerate([[img1_b1_t, img2_b1_t], [img1_b2_t, img2_b2_t], [img1_b3_t, img2_b3_t], img1_b4_t, img2_b4_t]):
        current_color = random_colors[idx]
    
        if type(block) == list:
            block[0].color = block[1].color = current_color
        else:
            if training_order[show_images_t.thisN] == 1:
                img1_b4_t.color = img2_b4_t.color = current_color
                break
            else:
                block.color = current_color
    
    # keep track of which components have finished
    images_randomization_tComponents = []
    for thisComponent in images_randomization_tComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "images_randomization_t" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in images_randomization_tComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "images_randomization_t" ---
    for thisComponent in images_randomization_tComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "images_randomization_t" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_point]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_point* updates
        if fixation_point.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point.frameNStart = frameN  # exact frame index
            fixation_point.tStart = t  # local t and not account for scr refresh
            fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point, 'tStartRefresh')  # time at next scr refresh
            fixation_point.setAutoDraw(True)
        if fixation_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point.tStop = t  # not accounting for scr refresh
                fixation_point.frameNStop = frameN  # exact frame index
                fixation_point.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # set up handler to look after randomisation of conditions etc
    redisplay_image_loop_t = data.TrialHandler(nReps=999.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='redisplay_image_loop_t')
    thisExp.addLoop(redisplay_image_loop_t)  # add the loop to the experiment
    thisRedisplay_image_loop_t = redisplay_image_loop_t.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRedisplay_image_loop_t.rgb)
    if thisRedisplay_image_loop_t != None:
        for paramName in thisRedisplay_image_loop_t:
            exec('{} = thisRedisplay_image_loop_t[paramName]'.format(paramName))
    
    for thisRedisplay_image_loop_t in redisplay_image_loop_t:
        currentLoop = redisplay_image_loop_t
        # abbreviate parameter names if possible (e.g. rgb = thisRedisplay_image_loop_t.rgb)
        if thisRedisplay_image_loop_t != None:
            for paramName in thisRedisplay_image_loop_t:
                exec('{} = thisRedisplay_image_loop_t[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "redisplay_blank" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        redisplay_blankComponents = [redisplay_blank_text]
        for thisComponent in redisplay_blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "redisplay_blank" ---
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *redisplay_blank_text* updates
            if redisplay_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                redisplay_blank_text.frameNStart = frameN  # exact frame index
                redisplay_blank_text.tStart = t  # local t and not account for scr refresh
                redisplay_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(redisplay_blank_text, 'tStartRefresh')  # time at next scr refresh
                redisplay_blank_text.setAutoDraw(True)
            if redisplay_blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > redisplay_blank_text.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    redisplay_blank_text.tStop = t  # not accounting for scr refresh
                    redisplay_blank_text.frameNStop = frameN  # exact frame index
                    redisplay_blank_text.setAutoDraw(False)
            # Run 'Each Frame' code from redisplay_blank_code
            if currentLoop.thisN == 0:
                continueRoutine = False
            else:
                continueRoutine = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in redisplay_blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "redisplay_blank" ---
        for thisComponent in redisplay_blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "image_1_t" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        image_1_tComponents = [img_1_bg_t, img1_b1_t, img1_b2_t, img1_b3_t, img1_b4_t]
        for thisComponent in image_1_tComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "image_1_t" ---
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img_1_bg_t* updates
            if img_1_bg_t.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img_1_bg_t.frameNStart = frameN  # exact frame index
                img_1_bg_t.tStart = t  # local t and not account for scr refresh
                img_1_bg_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_1_bg_t, 'tStartRefresh')  # time at next scr refresh
                img_1_bg_t.setAutoDraw(True)
            if img_1_bg_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_1_bg_t.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img_1_bg_t.tStop = t  # not accounting for scr refresh
                    img_1_bg_t.frameNStop = frameN  # exact frame index
                    img_1_bg_t.setAutoDraw(False)
            
            # *img1_b1_t* updates
            if img1_b1_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b1_t.frameNStart = frameN  # exact frame index
                img1_b1_t.tStart = t  # local t and not account for scr refresh
                img1_b1_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b1_t, 'tStartRefresh')  # time at next scr refresh
                img1_b1_t.setAutoDraw(True)
            if img1_b1_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b1_t.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b1_t.tStop = t  # not accounting for scr refresh
                    img1_b1_t.frameNStop = frameN  # exact frame index
                    img1_b1_t.setAutoDraw(False)
            
            # *img1_b2_t* updates
            if img1_b2_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b2_t.frameNStart = frameN  # exact frame index
                img1_b2_t.tStart = t  # local t and not account for scr refresh
                img1_b2_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b2_t, 'tStartRefresh')  # time at next scr refresh
                img1_b2_t.setAutoDraw(True)
            if img1_b2_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b2_t.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b2_t.tStop = t  # not accounting for scr refresh
                    img1_b2_t.frameNStop = frameN  # exact frame index
                    img1_b2_t.setAutoDraw(False)
            
            # *img1_b3_t* updates
            if img1_b3_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b3_t.frameNStart = frameN  # exact frame index
                img1_b3_t.tStart = t  # local t and not account for scr refresh
                img1_b3_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b3_t, 'tStartRefresh')  # time at next scr refresh
                img1_b3_t.setAutoDraw(True)
            if img1_b3_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b3_t.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b3_t.tStop = t  # not accounting for scr refresh
                    img1_b3_t.frameNStop = frameN  # exact frame index
                    img1_b3_t.setAutoDraw(False)
            
            # *img1_b4_t* updates
            if img1_b4_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b4_t.frameNStart = frameN  # exact frame index
                img1_b4_t.tStart = t  # local t and not account for scr refresh
                img1_b4_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b4_t, 'tStartRefresh')  # time at next scr refresh
                img1_b4_t.setAutoDraw(True)
            if img1_b4_t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b4_t.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b4_t.tStop = t  # not accounting for scr refresh
                    img1_b4_t.frameNStop = frameN  # exact frame index
                    img1_b4_t.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in image_1_tComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_1_t" ---
        for thisComponent in image_1_tComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank_text]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        while continueRoutine and routineTimer.getTime() < 0.9:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_text* updates
            if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_text.frameNStart = frameN  # exact frame index
                blank_text.tStart = t  # local t and not account for scr refresh
                blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                blank_text.setAutoDraw(True)
            if blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_text.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_text.tStop = t  # not accounting for scr refresh
                    blank_text.frameNStop = frameN  # exact frame index
                    blank_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.900000)
        
        # --- Prepare to start Routine "image_2_t" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        redisplay_key_t.keys = []
        redisplay_key_t.rt = []
        _redisplay_key_t_allKeys = []
        # keep track of which components have finished
        image_2_tComponents = [img2_bg_t, img2_b1_t, img2_b2_t, img2_b3_t, img2_b4_t, redisplay_key_t]
        for thisComponent in image_2_tComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "image_2_t" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img2_bg_t* updates
            if img2_bg_t.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img2_bg_t.frameNStart = frameN  # exact frame index
                img2_bg_t.tStart = t  # local t and not account for scr refresh
                img2_bg_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_bg_t, 'tStartRefresh')  # time at next scr refresh
                img2_bg_t.setAutoDraw(True)
            
            # *img2_b1_t* updates
            if img2_b1_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b1_t.frameNStart = frameN  # exact frame index
                img2_b1_t.tStart = t  # local t and not account for scr refresh
                img2_b1_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b1_t, 'tStartRefresh')  # time at next scr refresh
                img2_b1_t.setAutoDraw(True)
            
            # *img2_b2_t* updates
            if img2_b2_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b2_t.frameNStart = frameN  # exact frame index
                img2_b2_t.tStart = t  # local t and not account for scr refresh
                img2_b2_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b2_t, 'tStartRefresh')  # time at next scr refresh
                img2_b2_t.setAutoDraw(True)
            
            # *img2_b3_t* updates
            if img2_b3_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b3_t.frameNStart = frameN  # exact frame index
                img2_b3_t.tStart = t  # local t and not account for scr refresh
                img2_b3_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b3_t, 'tStartRefresh')  # time at next scr refresh
                img2_b3_t.setAutoDraw(True)
            
            # *img2_b4_t* updates
            if img2_b4_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b4_t.frameNStart = frameN  # exact frame index
                img2_b4_t.tStart = t  # local t and not account for scr refresh
                img2_b4_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b4_t, 'tStartRefresh')  # time at next scr refresh
                img2_b4_t.setAutoDraw(True)
            
            # *redisplay_key_t* updates
            waitOnFlip = False
            if redisplay_key_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                redisplay_key_t.frameNStart = frameN  # exact frame index
                redisplay_key_t.tStart = t  # local t and not account for scr refresh
                redisplay_key_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(redisplay_key_t, 'tStartRefresh')  # time at next scr refresh
                redisplay_key_t.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(redisplay_key_t.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(redisplay_key_t.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if redisplay_key_t.status == STARTED and not waitOnFlip:
                theseKeys = redisplay_key_t.getKeys(keyList=['space'], waitRelease=False)
                _redisplay_key_t_allKeys.extend(theseKeys)
                if len(_redisplay_key_t_allKeys):
                    redisplay_key_t.keys = _redisplay_key_t_allKeys[-1].name  # just the last key pressed
                    redisplay_key_t.rt = _redisplay_key_t_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_answer_t
            keys = event.getKeys()
            
            if len(keys)>0:
                for thisKey in keys:
                    current_key = ord(thisKey[0])
                    
                    if current_key == identical_key or current_key == non_identical_key:
                        redisplay_image_loop_t.finished = True
                        continueRoutine = False   
            
            #        elif current_key == 115:
            #            redisplay_image_loop_t.finished = False
            #            continueRoutine = False
            #
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in image_2_tComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_2_t" ---
        for thisComponent in image_2_tComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "image_2_t" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'redisplay_image_loop_t'
    
# completed num_of_training repeats of 'show_images_t'


# --- Prepare to start Routine "instructions_exp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instructions_expComponents = [exp_text, key_resp_4]
for thisComponent in instructions_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_exp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exp_text* updates
    if exp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exp_text.frameNStart = frameN  # exact frame index
        exp_text.tStart = t  # local t and not account for scr refresh
        exp_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_text, 'tStartRefresh')  # time at next scr refresh
        exp_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_exp" ---
for thisComponent in instructions_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
show_images = data.TrialHandler(nReps=num_of_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='show_images')
thisExp.addLoop(show_images)  # add the loop to the experiment
thisShow_image = show_images.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShow_image.rgb)
if thisShow_image != None:
    for paramName in thisShow_image:
        exec('{} = thisShow_image[paramName]'.format(paramName))

for thisShow_image in show_images:
    currentLoop = show_images
    # abbreviate parameter names if possible (e.g. rgb = thisShow_image.rgb)
    if thisShow_image != None:
        for paramName in thisShow_image:
            exec('{} = thisShow_image[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "images_randomization" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from location
    # List of locations
    locations = []
    
    # Randomize the grid locations
    current_grid = copy.deepcopy(grid)
    random.shuffle(current_grid)
    
    # Add randomization for each block
    # Set the block location
    for idx, block in enumerate([[img1_b1, img2_b1], [img1_b2, img2_b2], [img1_b3, img2_b3], [img1_b4, img2_b4]]):
        current_location = randomize_location(current_grid[idx], 38, 20)
        block[0].pos = block[1].pos = current_location
        locations.append(current_location)
    
    
    # Run 'Begin Routine' code from color
    import random
    
    # Randomize the color palette
    random.shuffle(color_palette)
    
    # Pick 5 Random colors
    random_colors = []
    random_colors+=random.sample(color_palette, 5)
    
    # Assign the first 5 colors to the blocks
    for idx, block in enumerate([[img1_b1, img2_b1], [img1_b2, img2_b2], [img1_b3, img2_b3], img1_b4, img2_b4]):
        current_color = random_colors[idx]
    
        if type(block) == list:
            block[0].color = block[1].color = current_color
        else:
            if trial_order[show_images.thisN] == 1:
                img1_b4.color = img2_b4.color = current_color
                break
            else:
                block.color = current_color
    
    
    if trial_order[show_images.thisN] == 1:
        img1_colors = img2_colors = random_colors[0:4]
    else:
        img1_colors = random_colors[0:4]
        img2_colors = random_colors[0:3]
        img2_colors.append(random_colors[4])
    
    
    
    # keep track of which components have finished
    images_randomizationComponents = []
    for thisComponent in images_randomizationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "images_randomization" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in images_randomizationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "images_randomization" ---
    for thisComponent in images_randomizationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "images_randomization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_point]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_point* updates
        if fixation_point.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point.frameNStart = frameN  # exact frame index
            fixation_point.tStart = t  # local t and not account for scr refresh
            fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point, 'tStartRefresh')  # time at next scr refresh
            fixation_point.setAutoDraw(True)
        if fixation_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point.tStop = t  # not accounting for scr refresh
                fixation_point.frameNStop = frameN  # exact frame index
                fixation_point.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # set up handler to look after randomisation of conditions etc
    redisplay_image_loop = data.TrialHandler(nReps=999.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='redisplay_image_loop')
    thisExp.addLoop(redisplay_image_loop)  # add the loop to the experiment
    thisRedisplay_image_loop = redisplay_image_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRedisplay_image_loop.rgb)
    if thisRedisplay_image_loop != None:
        for paramName in thisRedisplay_image_loop:
            exec('{} = thisRedisplay_image_loop[paramName]'.format(paramName))
    
    for thisRedisplay_image_loop in redisplay_image_loop:
        currentLoop = redisplay_image_loop
        # abbreviate parameter names if possible (e.g. rgb = thisRedisplay_image_loop.rgb)
        if thisRedisplay_image_loop != None:
            for paramName in thisRedisplay_image_loop:
                exec('{} = thisRedisplay_image_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "redisplay_blank" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        redisplay_blankComponents = [redisplay_blank_text]
        for thisComponent in redisplay_blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "redisplay_blank" ---
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *redisplay_blank_text* updates
            if redisplay_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                redisplay_blank_text.frameNStart = frameN  # exact frame index
                redisplay_blank_text.tStart = t  # local t and not account for scr refresh
                redisplay_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(redisplay_blank_text, 'tStartRefresh')  # time at next scr refresh
                redisplay_blank_text.setAutoDraw(True)
            if redisplay_blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > redisplay_blank_text.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    redisplay_blank_text.tStop = t  # not accounting for scr refresh
                    redisplay_blank_text.frameNStop = frameN  # exact frame index
                    redisplay_blank_text.setAutoDraw(False)
            # Run 'Each Frame' code from redisplay_blank_code
            if currentLoop.thisN == 0:
                continueRoutine = False
            else:
                continueRoutine = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in redisplay_blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "redisplay_blank" ---
        for thisComponent in redisplay_blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "image_1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from routine_start
        # Records the `fullRoutineRT` start
        
        if redisplay_image_loop.thisN == 0:
            fullRoutineStart = core.getTime()
        # keep track of which components have finished
        image_1Components = [img1_bg, img1_b1, img1_b2, img1_b3, img1_b4]
        for thisComponent in image_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "image_1" ---
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img1_bg* updates
            if img1_bg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img1_bg.frameNStart = frameN  # exact frame index
                img1_bg.tStart = t  # local t and not account for scr refresh
                img1_bg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_bg, 'tStartRefresh')  # time at next scr refresh
                img1_bg.setAutoDraw(True)
            if img1_bg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_bg.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_bg.tStop = t  # not accounting for scr refresh
                    img1_bg.frameNStop = frameN  # exact frame index
                    img1_bg.setAutoDraw(False)
            
            # *img1_b1* updates
            if img1_b1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b1.frameNStart = frameN  # exact frame index
                img1_b1.tStart = t  # local t and not account for scr refresh
                img1_b1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b1, 'tStartRefresh')  # time at next scr refresh
                img1_b1.setAutoDraw(True)
            if img1_b1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b1.tStop = t  # not accounting for scr refresh
                    img1_b1.frameNStop = frameN  # exact frame index
                    img1_b1.setAutoDraw(False)
            
            # *img1_b2* updates
            if img1_b2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b2.frameNStart = frameN  # exact frame index
                img1_b2.tStart = t  # local t and not account for scr refresh
                img1_b2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b2, 'tStartRefresh')  # time at next scr refresh
                img1_b2.setAutoDraw(True)
            if img1_b2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b2.tStop = t  # not accounting for scr refresh
                    img1_b2.frameNStop = frameN  # exact frame index
                    img1_b2.setAutoDraw(False)
            
            # *img1_b3* updates
            if img1_b3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img1_b3.frameNStart = frameN  # exact frame index
                img1_b3.tStart = t  # local t and not account for scr refresh
                img1_b3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b3, 'tStartRefresh')  # time at next scr refresh
                img1_b3.setAutoDraw(True)
            if img1_b3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b3.tStop = t  # not accounting for scr refresh
                    img1_b3.frameNStop = frameN  # exact frame index
                    img1_b3.setAutoDraw(False)
            
            # *img1_b4* updates
            if img1_b4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img1_b4.frameNStart = frameN  # exact frame index
                img1_b4.tStart = t  # local t and not account for scr refresh
                img1_b4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img1_b4, 'tStartRefresh')  # time at next scr refresh
                img1_b4.setAutoDraw(True)
            if img1_b4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img1_b4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    img1_b4.tStop = t  # not accounting for scr refresh
                    img1_b4.frameNStop = frameN  # exact frame index
                    img1_b4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in image_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_1" ---
        for thisComponent in image_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [blank_text]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        while continueRoutine and routineTimer.getTime() < 0.9:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_text* updates
            if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_text.frameNStart = frameN  # exact frame index
                blank_text.tStart = t  # local t and not account for scr refresh
                blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                blank_text.setAutoDraw(True)
            if blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_text.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_text.tStop = t  # not accounting for scr refresh
                    blank_text.frameNStop = frameN  # exact frame index
                    blank_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.900000)
        
        # --- Prepare to start Routine "image_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        redisplay_key.keys = []
        redisplay_key.rt = []
        _redisplay_key_allKeys = []
        # Run 'Begin Routine' code from code_answer
        # Records the `singleRoutineRT` start
        singleRoutineStart = core.getTime()
        
        
        
        # keep track of which components have finished
        image_2Components = [img2_bg, img2_b1, img2_b2, img2_b3, img2_b4, redisplay_key]
        for thisComponent in image_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "image_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img2_bg* updates
            if img2_bg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img2_bg.frameNStart = frameN  # exact frame index
                img2_bg.tStart = t  # local t and not account for scr refresh
                img2_bg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_bg, 'tStartRefresh')  # time at next scr refresh
                img2_bg.setAutoDraw(True)
            
            # *img2_b1* updates
            if img2_b1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b1.frameNStart = frameN  # exact frame index
                img2_b1.tStart = t  # local t and not account for scr refresh
                img2_b1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b1, 'tStartRefresh')  # time at next scr refresh
                img2_b1.setAutoDraw(True)
            
            # *img2_b2* updates
            if img2_b2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b2.frameNStart = frameN  # exact frame index
                img2_b2.tStart = t  # local t and not account for scr refresh
                img2_b2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b2, 'tStartRefresh')  # time at next scr refresh
                img2_b2.setAutoDraw(True)
            
            # *img2_b3* updates
            if img2_b3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b3.frameNStart = frameN  # exact frame index
                img2_b3.tStart = t  # local t and not account for scr refresh
                img2_b3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b3, 'tStartRefresh')  # time at next scr refresh
                img2_b3.setAutoDraw(True)
            
            # *img2_b4* updates
            if img2_b4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img2_b4.frameNStart = frameN  # exact frame index
                img2_b4.tStart = t  # local t and not account for scr refresh
                img2_b4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img2_b4, 'tStartRefresh')  # time at next scr refresh
                img2_b4.setAutoDraw(True)
            
            # *redisplay_key* updates
            waitOnFlip = False
            if redisplay_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                redisplay_key.frameNStart = frameN  # exact frame index
                redisplay_key.tStart = t  # local t and not account for scr refresh
                redisplay_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(redisplay_key, 'tStartRefresh')  # time at next scr refresh
                redisplay_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(redisplay_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(redisplay_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if redisplay_key.status == STARTED and not waitOnFlip:
                theseKeys = redisplay_key.getKeys(keyList=['space'], waitRelease=False)
                _redisplay_key_allKeys.extend(theseKeys)
                if len(_redisplay_key_allKeys):
                    redisplay_key.keys = _redisplay_key_allKeys[-1].name  # just the last key pressed
                    redisplay_key.rt = _redisplay_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_answer
            keys = event.getKeys()
            
            if len(keys)>0:
                for thisKey in keys:
                    current_key = ord(thisKey[0])
                    
                    if current_key == identical_key or current_key == non_identical_key:
                        redisplay_image_loop.finished = True
                        continueRoutine = False   
            
            #        elif current_key == 115:
            #            redisplay_image_loop.finished = False
            #            continueRoutine = False
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in image_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_2" ---
        for thisComponent in image_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_answer
        # Records the `singleRoutineRT` and `fullRoutineRT` end
        routineEnd = core.getTime()
        
        
        # imagesVariation:
        # 1 - '==' Identical Images
        # 0 - '!=' Non-Identical Images
        redisplay_image_loop.addData('imagesVariation', trial_order[show_images.thisN])
        
        if trial_order[show_images.thisN] == 0:
            redisplay_image_loop.addData('imagesVariationSign', '!=')
        elif trial_order[show_images.thisN] == 1:
            redisplay_image_loop.addData('imagesVariationSign', '==')
        
        
        # Key 112
        if current_key == identical_key:
            
            pressedKey = 'p' if identical_key == 112 else 'q'
            
            if trial_order[show_images.thisN] == 1:
                redisplay_image_loop.addData('correctAnswerBoolean', True)
                redisplay_image_loop.addData('correctAnswer', 1)
                numOfCorrectAnswers += 1
            else:
                redisplay_image_loop.addData('correctAnswerBoolean', False)
                redisplay_image_loop.addData('correctAnswer', 0)
                numOfWrongAnswers += 1
                
            redisplay_image_loop.addData('fullRoutineRT', routineEnd - fullRoutineStart)
            redisplay_image_loop.addData('locations', locations)
            redisplay_image_loop.addData('img1Colors', img1_colors)
            redisplay_image_loop.addData('img2Colors', img2_colors)
            
         
        # Key 113
        elif current_key == non_identical_key:
            
            pressedKey = 'q' if non_identical_key == 113 else 'p'
            
            if trial_order[show_images.thisN] == 0:
                redisplay_image_loop.addData('correctAnswerBoolean', True)
                redisplay_image_loop.addData('correctAnswer', 1)
                numOfCorrectAnswers += 1
            else:
                redisplay_image_loop.addData('correctAnswerBoolean', False)
                redisplay_image_loop.addData('correctAnswer', 0)
                numOfWrongAnswers += 1
            
            redisplay_image_loop.addData('fullRoutineRT', routineEnd - fullRoutineStart)
            redisplay_image_loop.addData('locations', locations)
            redisplay_image_loop.addData('img1Colors', img1_colors)
            redisplay_image_loop.addData('img2Colors', img2_colors)
        
        # Key 115 = 'space'
        elif current_key == 115:
            pressedKey = 'space'
            totalNumOfLoops += 1
        
        
        # Saving data
        redisplay_image_loop.addData('routineNumber', show_images.thisN)
        redisplay_image_loop.addData('pressedKey', pressedKey)
        redisplay_image_loop.addData('numOfCorrectAnswers', numOfCorrectAnswers)
        redisplay_image_loop.addData('numOfWrongAnswers', numOfWrongAnswers)
        redisplay_image_loop.addData('numOfLoops', redisplay_image_loop.thisN)
        redisplay_image_loop.addData('totalNumOfLoops', totalNumOfLoops)
        redisplay_image_loop.addData('singleRoutineRT', routineEnd - singleRoutineStart)
        
        
        # the Routine "image_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'redisplay_image_loop'
    
# completed num_of_trials repeats of 'show_images'


# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
finishComponents = [finish_text, key_resp_3]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from data_summary
# Data Overview

thisExp.addData('numOfCorrectAnswers', numOfCorrectAnswers)
thisExp.addData('numOfWrongAnswers', numOfWrongAnswers)
thisExp.addData('totalNumOfLoops', totalNumOfLoops)
thisExp.addData('totalNumOfTrials', num_of_trials)
thisExp.addData('trialsOrder', trial_order)

genderBoolean = 0
if expInfo["gender"] == 'woman':
    genderBoolean = 0
elif expInfo["gender"] == 'man':
    genderBoolean = 1
else:
    genderBoolean = 2
       
thisExp.addData('genderBoolean', genderBoolean)
thisExp.addData('shapeBoolean', 0 if expInfo["shape"] == 'square' else 1)
thisExp.addData('handednessBoolean', 0 if expInfo["handedness"] == 'right-handed' else 1)

thisExp.nextEntry()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
