---
title: Switching Desktops Responding to DrvAssertMode
description: Switching Desktops Responding to DrvAssertMode
ms.assetid: 0e37050f-63db-4e85-840b-c8f817a7f0e8
keywords: ["display drivers WDK Windows 2000 , desktop management", "desktop management WDK Windows 2000 display", "switching desktops WDK Windows 2000 display", "DrvAssertMode"]
---

# Switching Desktops: Responding to DrvAssertMode


## <span id="ddk_switching_desktops_responding_to_drvassertmode_gg"></span><span id="DDK_SWITCHING_DESKTOPS_RESPONDING_TO_DRVASSERTMODE_GG"></span>


When switching between desktops on a display, Window Manager ensures that the desktops are properly redrawn and that a mouse pointer is enabled and displayed in the correct position. The display driver receives a call to [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178) only when there is a desktop switch.

When this function is called, the driver ensures that the indicated [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) is either in the mode specified when the PDEV was created, or in text mode. Window Manager then selects the correct pointer shape and moves it to the current position. GDI, not the driver, is responsible for maintaining the mouse pointer state.

GDI calls *DrvAssertMode* to set the mode of a specified hardware device. This function selects either the mode specified when the display driver-defined PDEV structure was created or the default mode of the hardware. The driver should keep a record of the current mode of the PDEV.

GDI also calls [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178), with the enable parameter set to **FALSE**, when the user switches from a windowed application to a full-screen application in *x*86 applications, or when the user switches desktops (on all platforms). The display driver must restore the video hardware to a default mode by sending [**IOCTL\_VIDEO\_RESET\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff567834) in an [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) call to the video miniport driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Switching%20Desktops:%20Responding%20to%20DrvAssertMode%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




