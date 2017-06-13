import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon('plugin.program.playonmonkey').getAddonInfo('id')
ADDONTITLE     = '[COLOR yellow][B]Playonmonkeys Wizard[/B][/COLOR]'
BUILDERNAME    = 'Playonmonkey'
EXCLUDES       = [ADDON_ID, 'repository.playonmonkey', 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f6275696c64732e747874')
UPDATECHECK    = 0
APKFILE        = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f617070636174732e747874')
YOUTUBETITLE   = 'Help Videos' 
YOUTUBEFILE    = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f796f757475626568656c702e747874')
ADDONFILE      = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f6164646f6e732e747874')
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f6164646f6e66697865732e747874')
PATH           = xbmcaddon.Addon('plugin.program.playonmonkey').getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = os.path.join(ART, 'main.png')
ICONMAINT      = os.path.join(ART, 'main.png')
ICONAPK        = os.path.join(ART, 'main.png')
ICONADDONS     = os.path.join(ART, 'main.png')
ICONYOUTUBE    = os.path.join(ART, 'main.png')
ICONSAVE       = os.path.join(ART, 'main.png')
ICONTRAKT      = os.path.join(ART, 'main.png')
ICONREAL       = os.path.join(ART, 'main.png')
ICONLOGIN      = os.path.join(ART, 'main.png')
ICONCONTACT    = os.path.join(ART, 'main.png')
ICONSETTINGS   = os.path.join(ART, 'main.png')
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '*'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'yellow'
COLOR2         = 'yellow'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Playonmonkeys.\r\nWebsite: http://playonmonkeys.net\r\nContact us on facebook at http://www.mediacenterwizards.com'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f77697a7570646174652e747874')
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = binascii.unhexlify('687474703a2f2f7777772e706c61796f6e6d6f6e6b6579732e636f6d2f77697a6c6973742f676f72696c6c616d6573732e747874')
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font13'
HEADERMESSAGE  = 'Playonmonkey Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = os.path.join(ART, 'notify.jpg')
############################    #############################