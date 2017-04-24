---
title: Identifying a Printer's Color Capability
author: windows-driver-content
description: Identifying a Printer's Color Capability
ms.assetid: 24abf76d-c0f9-440e-b825-8b39ea9ab807
keywords:
- printer interface DLL WDK , color capability supported
- color management WDK print , identifying capabilities
- identifying printer color capabilities
- printer color capabilities WDK
- dmColor
- DC_COLORDEVICE
- DrvDeviceCapabilities
- monochrome output WDK printer
- noncolor output WDK printer
- grayscale output WDK printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Identifying a Printer's Color Capability


## <a href="" id="ddk-identifying-a-printer-s-color-capability-gg"></a>


To distinguish between color and noncolor (monochrome or grayscale) devices, Windows 2000 and later NT-based operating system versions call the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function, passing the DC\_COLORDEVICE constant in the call. This function returns 1 if the device supports color, and 0 if the device produces monochrome or grayscale output. It is recommended that all printer drivers support calls to **DrvDeviceCapabilities** for the DC\_COLORDEVICE constant.

It is very important for drivers to implement the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function. Otherwise it is more difficult for the operating system to distinguish between color and noncolor devices, for the following reasons:

-   A call to the **GetDeviceCaps** function (described in the Windows SDK documentation), in which the NUMCOLORS constant is passed, usually results in a return value less than or equal to 2 for most noncolor devices, and greater than 2 for color devices. The operating system is unable to distinguish between monochrome and grayscale devices.

-   The value of the **dmColor** member of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure is not a reliable indicator of whether the device is a color or noncolor device. Certain printer drivers set this member to DMCOLOR\_COLOR even for devices that are not capable of producing color.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Identifying%20a%20Printer's%20Color%20Capability%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


