---
title: Installing ICC Profiles
author: windows-driver-content
description: Installing ICC Profiles
ms.assetid: d9253ee8-c414-46a9-899f-46ae32cee41a
keywords:
- color management WDK print , installing ICC profiles
- ICC profiles WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing ICC Profiles


## <a href="" id="ddk-installing-icc-profiles-gg"></a>


To install ICC profiles for a printer, the files must be listed in a [printer INF file](printer-inf-files.md).

Following is an example of an .inf file that causes two ICC profile files to be installed. Note that profile files are written to the color directory, which has a [printer dirid](printer-dirids.md) value of 66003.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20ICC%20Profiles%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


