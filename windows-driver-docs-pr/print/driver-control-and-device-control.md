---
title: Driver Control and Device Control
author: windows-driver-content
description: Driver Control and Device Control
MS-HAID:
- 'printicm\_3232a23d-82a8-47c4-9346-120f7750dc54.xml'
- 'print.driver\_control\_and\_device\_control'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ff515e88-9a94-420f-a6c8-fba3483c00e5
keywords: ["proprietary color management WDK print", "DrvIcmCreateColorTransform", "driver-controlled color management WDK print", "device-controlled color management WDK print", "driver color management WDK See color management WDK", "device color management WDK See color management WDK"]
---

# Driver Control and Device Control


## <a href="" id="ddk-driver-control-and-device-control-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Driver%20Control%20and%20Device%20Control%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


