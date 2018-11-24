---
title: Switching Desktops Responding to DrvAssertMode
description: Switching Desktops Responding to DrvAssertMode
ms.assetid: 0e37050f-63db-4e85-840b-c8f817a7f0e8
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
- switching desktops WDK Windows 2000 display
- DrvAssertMode
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Switching Desktops: Responding to DrvAssertMode


## <span id="ddk_switching_desktops_responding_to_drvassertmode_gg"></span><span id="DDK_SWITCHING_DESKTOPS_RESPONDING_TO_DRVASSERTMODE_GG"></span>


When switching between desktops on a display, Window Manager ensures that the desktops are properly redrawn and that a mouse pointer is enabled and displayed in the correct position. The display driver receives a call to [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178) only when there is a desktop switch.

When this function is called, the driver ensures that the indicated [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) is either in the mode specified when the PDEV was created, or in text mode. Window Manager then selects the correct pointer shape and moves it to the current position. GDI, not the driver, is responsible for maintaining the mouse pointer state.

GDI calls *DrvAssertMode* to set the mode of a specified hardware device. This function selects either the mode specified when the display driver-defined PDEV structure was created or the default mode of the hardware. The driver should keep a record of the current mode of the PDEV.

GDI also calls [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178), with the enable parameter set to **FALSE**, when the user switches from a windowed application to a full-screen application in *x*86 applications, or when the user switches desktops (on all platforms). The display driver must restore the video hardware to a default mode by sending [**IOCTL\_VIDEO\_RESET\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff567834) in an [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) call to the video miniport driver.

 

 





