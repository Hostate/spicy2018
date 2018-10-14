#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on 十月 14, 2018, at 19:43
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = '1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[800, 600], fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "wel"
welClock = core.Clock()
text_wel = visual.TextStim(win=win, name='text_wel',
    text="本实验是一个词汇判断分类任务\n\n您需要将屏幕中央出现的词语分类到左上角或右上角的类别中。\n\n首先，请把您左右手的食指或中指放在键盘的'E'和'I'上。\n\n如果屏幕中央的词属于左上角的词语类别时，请按'E'键；如果属于右上角的词语类别时，则按'I'键。\n\n每个词只能归入一个类别。\n\n如果您出错了，便会看见一个红色的'X'。请尽可能又快又好地完成任务。\n\n下面将会进入练习任务，请您尽快熟悉实验程序。\n\n请按空格键开始",
    font='Consonlas',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trian_1"
trian_1Clock = core.Clock()
beauty_left = visual.TextStim(win=win, name='beauty_left',
    text='美丽女性',
    font='Consonlas',
    pos=(-0.8, 0.8), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ugly_right = visual.TextStim(win=win, name='ugly_right',
    text='普通女性',
    font='Consonlas',
    pos=(0.8, 0.8), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
or_hot = visual.TextStim(win=win, name='or_hot',
    text='OR\n\n辣味',
    font='Consolas',
    pos=(-0.85, 0.6), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
image_1 = visual.ImageStim(
    win=win, name='image_1',
    image='photo\\\\beauty\\\\mn.png', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.3, 0.3),
    ori=45, pos=(0, -0.8),
    lineWidth=0.2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wel"-------
t = 0
welClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_wel = event.BuilderKeyResponse()
# keep track of which components have finished
welComponents = [text_wel, key_resp_wel]
for thisComponent in welComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wel"-------
while continueRoutine:
    # get current time
    t = welClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_wel* updates
    if t >= 0.0 and text_wel.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_wel.tStart = t
        text_wel.frameNStart = frameN  # exact frame index
        text_wel.setAutoDraw(True)
    
    # *key_resp_wel* updates
    if t >= 0.0 and key_resp_wel.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_wel.tStart = t
        key_resp_wel.frameNStart = frameN  # exact frame index
        key_resp_wel.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_wel.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_wel.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_wel.keys = theseKeys[-1]  # just the last key pressed
            key_resp_wel.rt = key_resp_wel.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wel"-------
for thisComponent in welComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_wel.keys in ['', [], None]:  # No response was made
    key_resp_wel.keys=None
thisExp.addData('key_resp_wel.keys',key_resp_wel.keys)
if key_resp_wel.keys != None:  # we had a response
    thisExp.addData('key_resp_wel.rt', key_resp_wel.rt)
thisExp.nextEntry()
# the Routine "wel" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trian_1"-------
t = 0
trian_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
trian_1Components = [beauty_left, ugly_right, or_hot, image_1, cross, key_resp_2]
for thisComponent in trian_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
theseKeys = []
# -------Start Routine "trian_1"-------
while continueRoutine:
    # get current time
    t = trian_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beauty_left* updates
    if t >= 0.0 and beauty_left.status == NOT_STARTED:
        # keep track of start time/frame for later
        beauty_left.tStart = t
        beauty_left.frameNStart = frameN  # exact frame index
        beauty_left.setAutoDraw(True)
    
    # *ugly_right* updates
    if t >= 0.0 and ugly_right.status == NOT_STARTED:
        # keep track of start time/frame for later
        ugly_right.tStart = t
        ugly_right.frameNStart = frameN  # exact frame index
        ugly_right.setAutoDraw(True)
    
    # *or_hot* updates
    if t >= 0.0 and or_hot.status == NOT_STARTED:
        # keep track of start time/frame for later
        or_hot.tStart = t
        or_hot.frameNStart = frameN  # exact frame index
        or_hot.setAutoDraw(True)
    
    # *image_1* updates
    if t >= 0 and image_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_1.tStart = t
        image_1.frameNStart = frameN  # exact frame index
        image_1.setAutoDraw(True)
    
    # *cross* updates
    if (len(theseKeys) > 0 and ((key_resp_2.keys != str("'e'")) or (key_resp_2.keys != "'e'"))  and cross.status == NOT_STARTED):
        # keep track of start time/frame for later
        cross.tStart = t
        cross.frameNStart = frameN  # exact frame index
        cross.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # was this 'correct'?
            if (key_resp_2.keys == str("'e'")) or (key_resp_2.keys == "'e'"):
                key_resp_2.corr = 1
            else:
                key_resp_2.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trian_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trian_1"-------
for thisComponent in trian_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
    # was no response the correct answer?!
    if str("'e'").lower() == 'none':
       key_resp_2.corr = 1  # correct non-response
    else:
       key_resp_2.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
thisExp.addData('key_resp_2.corr', key_resp_2.corr)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "trian_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
