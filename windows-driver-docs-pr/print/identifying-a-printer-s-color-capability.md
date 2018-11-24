---
title: Identifying a Printer's Color Capability
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifying a Printer's Color Capability





To distinguish between color and noncolor (monochrome or grayscale) devices, Windows 2000 and later NT-based operating system versions call the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function, passing the DC\_COLORDEVICE constant in the call. This function returns 1 if the device supports color, and 0 if the device produces monochrome or grayscale output. It is recommended that all printer drivers support calls to **DrvDeviceCapabilities** for the DC\_COLORDEVICE constant.

It is very important for drivers to implement the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function. Otherwise it is more difficult for the operating system to distinguish between color and noncolor devices, for the following reasons:

-   A call to the **GetDeviceCaps** function (described in the Windows SDK documentation), in which the NUMCOLORS constant is passed, usually results in a return value less than or equal to 2 for most noncolor devices, and greater than 2 for color devices. The operating system is unable to distinguish between monochrome and grayscale devices.

-   The value of the **dmColor** member of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure is not a reliable indicator of whether the device is a color or noncolor device. Certain printer drivers set this member to DMCOLOR\_COLOR even for devices that are not capable of producing color.

 

 




