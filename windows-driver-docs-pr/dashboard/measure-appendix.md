---
title: Appendix for the Microsoft driver measure dictionary
description: Collection of ancillary materials for the Microsoft driver measure dictionary
ms.topic: article
ms.date: 05/20/2019
---

# Appendix for the Microsoft driver measure dictionary

## Top Microsoft apps example

|Application|Application type|
|----|----|
|Devenv.exe|Developer Tools|
|MS Paint|Entertainment|
|Microsoft Skype App|Comm & Collab|
|Microsoft Windows Photos|Media|
|Microsoft Windows Communications Apps|Productivity|
|Microsoft Paint|Creative|
|Microsoft Solitaire Collection|Games|
|OneDrive|Cloud Storage|
|Windows Component|Windows Component|
|Microsoft Edge|Browser|
|Microsoft Windows DVD Player|Entertainment|
|Microsoft Zune Video|Media|
|Msaccess.exe|Developer Tools|
|Outlook|Productivity|
|Excel|Productivity|
|Internet Explorer|Browser|
|Msvsmon.exe|Developer Tools|
|Minecraft: Windows 10 Edition Beta|Games|
|Powershell_Ise.exe|Developer Tools|
|Skype|Comm & Collab|
|Winword.exe|Productivity|
|Lync.exe|Comm & Collab|
|Msosync.exe|Cloud Storage|
|Microsoft One Connect|Productivity|
|Windbg.exe|Developer Tools|
|Microsoft Office Onenote|Productivity|
|Microsoft Mahjong|Games|
|Power Point|Productivity|
|Windbg.exe|Developer Tools|
|Microsoft Office Onenote|Productivity|
|Microsoft Zune Music|Media|
|Microsoft Mahjong|Games|
|PowerPoint|Productivity|
|Minecraft|Games|
|Microsoft Messaging|Comm & Collab|
|Microsoft Microsoft SkyDrive|Cloud Storage|
|Moviemaker.exe|Creative|

## Creative Applications Example

|Application|
|----|
|MSPaint.exe|
|Photoshop.eve|
|SnagitEditor.exe|
|Adobe Premiere Pro.exe|
|LightRoom.exe|
|AfterFX.eve|
|ClipStudioPaint.exe|
|Audacity.exe|
|SAI.exe|
|FL.exe|

## Audio Initialization Benign Failure Codes

### Common Benign Errors

AEERR_E_EXISTING_DIRECTKS_CLIENT

AEERR_E_EXISTING_EXCLUSIVE_CLIENT

AEERR_E_EXISTING_SHARED_CLIENT

AEERR_E_PIN_LOCKED

AEERR_NO_CONVERTERS_FOUND

AEERR_POLICY_ACCESS_DENIED

AUDCLNT_E_DEVICE_INVALIDATED

### AEERR_DEVICE_IN_USE Benign Errors

HResult == AEERR_DEVICE_IN_USE

Platform == Windows.Mobile

OffloadRequested == 1

There is another AudioClientInitialize event with the same AudioClientGuidId but with OffloadRequested == 0 and HResult == SUCCESS

### Benign Race Condition Errors

HResult == ERROR_PATH_NOT_FOUND or ERROR_NOT_FOUND or ERROR_NOT_CONNECTED

App == Windows Explorer or Windows Shell Experience Host

### Benign Parameter Error

Filter ERROR_INVALID_PARAMETER from the apps "videoeditor(plus)", "screenrecorder", "neilsenonline"
