---
title: Color Management for Displays
description: Color Management for Displays
ms.assetid: a0c3f35f-3741-4d5a-b7ae-dd177c719508
keywords:
- display drivers WDK Windows 2000 , color management
- color management WDK Windows 2000 display
- Image Color Management WDK Windows 2000 display
- ICM WDK Windows 2000 display
- gamma ramps WDK Windows 2000 display
- color exactness WDK Windows 2000 display
- exact colors WDK Windows 2000 display
- calibrating colors WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Management for Displays


## <span id="ddk_color_management_for_displays_gg"></span><span id="DDK_COLOR_MANAGEMENT_FOR_DISPLAYS_GG"></span>


GDI supports Image Color Management (ICM) version 2.0. Display drivers can use ICM without implementing any special code.

If the display hardware supports a [*gamma ramp*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp), the display driver should implement [**DrvIcmSetDeviceGammaRamp**](https://msdn.microsoft.com/library/windows/hardware/ff556243). Color-calibrating applications that require color exactness use this capability. DirectDraw also uses this function to allow DirectX applications -- such as a game that performs palette animation in RGB modes -- to control the gamma ramp. For example code, refer to the *Permedia* sample display drivers.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

 

 

 





