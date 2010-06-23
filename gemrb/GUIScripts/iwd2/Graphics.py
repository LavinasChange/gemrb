# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#
#Graphics Menu
import GemRB
from GUIDefines import *

GraphicsWindow = 0
TextAreaControl = 0

def OnLoad():
	global GraphicsWindow, TextAreaControl
	GemRB.LoadWindowPack("GUIOPT", 800, 600)
	GraphicsWindow = GemRB.LoadWindow(6)
	GraphicsWindow.SetFrame( )
	
	TextAreaControl = GraphicsWindow.GetControl(33)
	BrightnessButton = GraphicsWindow.GetControl(35)
	BrightnessSlider = GraphicsWindow.GetControl(3)
	BrightnessSlider.SetVarAssoc("Brightness Correction",0)

	ContrastButton = GraphicsWindow.GetControl(36)
	ContrastSlider = GraphicsWindow.GetControl(22)
	ContrastSlider.SetVarAssoc("Gamma Correction",1)

	BppButton = GraphicsWindow.GetControl(37)
	BppButtonB1 = GraphicsWindow.GetControl(5)
	BppButtonB2 = GraphicsWindow.GetControl(6)
	BppButtonB3 = GraphicsWindow.GetControl(7)
	BppButtonB1.SetFlags(IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	BppButtonB2.SetFlags(IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	BppButtonB3.SetFlags(IE_GUI_BUTTON_RADIOBUTTON,OP_OR)
	BppButtonB1.SetVarAssoc("BitsPerPixel",16)
	BppButtonB2.SetVarAssoc("BitsPerPixel",24)
	BppButtonB3.SetVarAssoc("BitsPerPixel",32)
	BppButtonB1.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)
	BppButtonB2.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)
	BppButtonB3.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)
	FullScreenButton = GraphicsWindow.GetControl(38)
	FullScreenButtonB = GraphicsWindow.GetControl(9)
	FullScreenButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	FullScreenButtonB.SetVarAssoc("Full Screen",1)
	FullScreenButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)

	SoftMirrBltButton = GraphicsWindow.GetControl(44)
	SoftMirrBltButtonB = GraphicsWindow.GetControl(40)
	SoftMirrBltButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	SoftMirrBltButtonB.SetVarAssoc("SoftMirrorBlt",1)
	SoftMirrBltButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)

	SoftTransBltButton = GraphicsWindow.GetControl(46)
	SoftTransBltButtonB = GraphicsWindow.GetControl(41)
	SoftTransBltButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	SoftTransBltButtonB.SetVarAssoc("SoftSrcKeyBlt",1)
	SoftTransBltButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)

	SoftStandBltButton = GraphicsWindow.GetControl(48)
	SoftStandBltButtonB = GraphicsWindow.GetControl(42)
	SoftStandBltButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	SoftStandBltButtonB.SetVarAssoc("SoftBltFast",1)
	SoftStandBltButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)

	TransShadowButton = GraphicsWindow.GetControl(50)
	TransShadowButtonB = GraphicsWindow.GetControl(51)
	TransShadowButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	TransShadowButtonB.SetVarAssoc("Translucent Shadows",1)
	TransShadowButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)
	
	TransBlitButton = GraphicsWindow.GetControl(52)
	TransBlitButtonB = GraphicsWindow.GetControl(56)
	TransBlitButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	TransBlitButtonB.SetVarAssoc("Translucent Blts",1)
	TransBlitButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)
	
	StaticAniButton = GraphicsWindow.GetControl(54)
	StaticAniButtonB = GraphicsWindow.GetControl(57)
	StaticAniButtonB.SetFlags(IE_GUI_BUTTON_CHECKBOX,OP_OR)
	StaticAniButtonB.SetVarAssoc("Static Animations",1)
	StaticAniButtonB.SetSprites("GBTNOPT4", 0, 0, 1, 2, 3)

	OkButton = GraphicsWindow.GetControl(21)
	CancelButton = GraphicsWindow.GetControl(32)
	TextAreaControl.SetText(18038)
	OkButton.SetText(11973)
	CancelButton.SetText(13727)
	CancelButton.SetFlags (IE_GUI_BUTTON_CANCEL, OP_OR)

	BrightnessButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, BrightnessPress)
	BrightnessSlider.SetEvent(IE_GUI_SLIDER_ON_CHANGE, BrightnessPress)
	ContrastButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, ContrastPress)
	ContrastSlider.SetEvent(IE_GUI_SLIDER_ON_CHANGE, ContrastPress)
	BppButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, BppPress)
	BppButtonB1.SetEvent(IE_GUI_BUTTON_ON_PRESS, BppPress)
	BppButtonB2.SetEvent(IE_GUI_BUTTON_ON_PRESS, BppPress)
	BppButtonB3.SetEvent(IE_GUI_BUTTON_ON_PRESS, BppPress)
	FullScreenButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, FullScreenPress)
	FullScreenButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, FullScreenPress)
	TransShadowButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, TransShadowPress)
	TransShadowButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, TransShadowPress)
	SoftMirrBltButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftMirrBltPress)
	SoftMirrBltButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftMirrBltPress)
	SoftTransBltButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftTransBltPress)
	SoftTransBltButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftTransBltPress)
	SoftStandBltButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftStandBltPress)
	SoftStandBltButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, SoftStandBltPress)
	TransBlitButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, TransBlitPress)
	TransBlitButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, TransBlitPress)
	StaticAniButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, StaticAniPress)
	StaticAniButtonB.SetEvent(IE_GUI_BUTTON_ON_PRESS, StaticAniPress)
	OkButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, OkPress)
	CancelButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, CancelPress)
	
	GraphicsWindow.SetVisible(WINDOW_VISIBLE)
	return
	
def BrightnessPress():
	TextAreaControl.SetText(17203)
	GemRB.SetGamma (GemRB.GetVar("Brightness Correction"),GemRB.GetVar("Gamma Correction")/2)
	return
	
def ContrastPress():
	TextAreaControl.SetText(17204)
	GemRB.SetGamma (GemRB.GetVar("Brightness Correction"),GemRB.GetVar("Gamma Correction")/2)
	return
	
def BppPress():
	TextAreaControl.SetText(17205)
	return
	
def FullScreenPress():
	TextAreaControl.SetText(18000)
	GemRB.SetFullScreen (GemRB.GetVar("Full Screen"))
	return
	
def TransShadowPress():
	TextAreaControl.SetText(20620)
	return
	
def SoftMirrBltPress():
	TextAreaControl.SetText(18004)
	return
	
def SoftTransBltPress():
	TextAreaControl.SetText(18006)
	return
	
def SoftStandBltPress():
	TextAreaControl.SetText(18007)
	return
	
def TransBlitPress():
	TextAreaControl.SetText(15141)
	return
	
def StaticAniPress():
	TextAreaControl.SetText(18004)
	return
	
def OkPress():
	if GraphicsWindow:
		GraphicsWindow.Unload()
	GemRB.SetNextScript("Options")
	return
	
def CancelPress():
	if GraphicsWindow:
		GraphicsWindow.Unload()
	GemRB.SetNextScript("Options")
	return
