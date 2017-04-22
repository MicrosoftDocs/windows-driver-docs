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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Color Management for Displays


## <span id="ddk_color_management_for_displays_gg"></span><span id="DDK_COLOR_MANAGEMENT_FOR_DISPLAYS_GG"></span>


GDI supports Image Color Management (ICM) version 2.0. Display drivers can use ICM without implementing any special code.

If the display hardware supports a [*gamma ramp*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp), the display driver should implement [**DrvIcmSetDeviceGammaRamp**](https://msdn.microsoft.com/library/windows/hardware/ff556243). Color-calibrating applications that require color exactness use this capability. DirectDraw also uses this function to allow DirectX applications -- such as a game that performs palette animation in RGB modes -- to control the gamma ramp. For example code, refer to the *Permedia* sample display drivers.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Color%20Management%20for%20Displays%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




