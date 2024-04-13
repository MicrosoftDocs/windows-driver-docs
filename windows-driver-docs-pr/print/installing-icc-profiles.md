---
title: Installing ICC Profiles
description: Installing ICC Profiles
keywords:
- color management WDK print , installing ICC profiles
- ICC profiles WDK print
ms.date: 05/08/2023
---

# Installing ICC Profiles

[!include[Print Support Apps](../includes/print-support-apps.md)]

To install ICC profiles for a printer, the files must be listed in a [printer INF file](printer-inf-files.md).

Following is an example of an .inf file that causes two ICC profile files to be installed. Note that profile files are written to the color directory, which has a [printer dirid](printer-dirids.md) value of 66003.

```inf
[Version]
...
Class=Printer
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
...

[My Company.NTamd64]
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
