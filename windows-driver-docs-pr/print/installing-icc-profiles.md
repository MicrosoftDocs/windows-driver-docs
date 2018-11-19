---
title: Installing ICC Profiles
description: Installing ICC Profiles
ms.assetid: d9253ee8-c414-46a9-899f-46ae32cee41a
keywords:
- color management WDK print , installing ICC profiles
- ICC profiles WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing ICC Profiles





To install ICC profiles for a printer, the files must be listed in a [printer INF file](printer-inf-files.md).

Following is an example of an .inf file that causes two ICC profile files to be installed. Note that profile files are written to the color directory, which has a [printer dirid](printer-dirids.md) value of 66003.

```cpp
[Version]
Signature="$Windows NT$"
Provider="My Company" 
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
Class=Printer

[My Company]
"My printer model" = MYDRIVER,My_Printer_Model

[MYDRIVER]
DriverFile=DRVR.DRV
DataFile=DRVR.DRV
CopyFiles=@DRVR.DRV,MY_COLOR_PROFILES
DataSection=MYDATA

[MYDATA]
HelpFile=DRVR.HLP
DefaultDataType=EMF

[MY_COLOR_PROFILES]
profile1.icm
profile2.icm

[DestinationDirs]
DefaultDestDir=11
MY_COLOR_PROFILES =66003
```








