---
title: Driver Control and Device Control
description: Driver Control and Device Control
ms.assetid: ff515e88-9a94-420f-a6c8-fba3483c00e5
keywords:
- proprietary color management WDK print
- DrvIcmCreateColorTransform
- driver-controlled color management WDK print
- device-controlled color management WDK print
- driver color management WDK See color management WDK
- device color management WDK See color management WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Control and Device Control





If color management control is provided by either the driver or by printer hardware, the driver's [printer graphics DLL](printer-graphics-dll.md) must set the GCAPS\_ICM flag in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

The driver must indicate support for CYMK color space (if appropriate), as described in [Supporting CMYK Color Space](supporting-cmyk-color-space.md).

Printer graphics DLLs must define the following three functions:

[**DrvIcmCreateColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff556239)

[**DrvIcmDeleteColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff556241)

[**DrvIcmCheckBitmapBits**](https://msdn.microsoft.com/library/windows/hardware/ff556238)

GDI calls the [**DrvIcmCreateColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff556239) function to supply the driver with ICC profiles (described in the Microsoft Windows SDK documentation) for the print job. Given these profiles, the function can create an internal color transform to use when correcting color information. A color transform is a driver-specific, internally defined mapping from one color space to another. The function returns a handle to the transform, which GDI stores.

Flags within the [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261) and [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) structures indicate whether color management is being performed by the system (or application) or by the driver (or device). Within each driver-implemented graphics DDI drawing function that receives either (or both) of these structures, the flags must be checked. If the system or application is currently handling color management, the driver or device must not. If driver or device color management is enabled, the graphics DDI function must call [**BRUSHOBJ\_hGetColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff538262) or [**XLATEOBJ\_hGetColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff570639) (or both) to obtain a handle to the color transform to be used. The handle will be one that the driver provided in response to a previous call to its [**DrvIcmCreateColorTransform**](https://msdn.microsoft.com/library/windows/hardware/ff556239) function.

### Handling Proprietary Color Management

For some devices, proprietary color management is performed (either by the driver or by hardware) regardless of whether ICM has been enabled. Drivers for such devices must not allow color correction to be performed if the received image data has already been corrected. Precorrected data can be received if:

-   An application has color-corrected the image "outside the DC" (see the Microsoft Windows SDK documentation).

-   Color management is being handled by the system.

For either of these scenarios, both the BR\_HOST\_ICM flag in the **flColorType** member of [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261) and the XO\_HOST\_ICM flag in the **flXlate** member of [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) will be set. These flags can be set even if the **dmICMMethod** member of [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) is DMICMMETHOD\_NONE.

 

 




