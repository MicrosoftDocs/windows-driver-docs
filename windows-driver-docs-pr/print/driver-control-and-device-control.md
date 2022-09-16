---
title: Driver control and device control
description: Provides information about driver control and device control.
keywords:
- proprietary color management WDK print
- DrvIcmCreateColorTransform
- driver-controlled color management WDK print
- device-controlled color management WDK print
- driver color management WDK See color management WDK
- device color management WDK See color management WDK
ms.date: 09/12/2022
---

# Driver control and device control

If color management control is provided by either the driver or by printer hardware, the driver's [printer graphics DLL](printer-graphics-dll.md) must set the GCAPS_ICM flag in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure.

The driver must indicate support for CYMK color space (if appropriate), as described in [Supporting CMYK Color Space](supporting-cmyk-color-space.md).

Printer graphics DLLs must define the following three functions:

- [**DrvIcmCreateColorTransform**](/windows/win32/api/winddi/nf-winddi-drvicmcreatecolortransform)

- [**DrvIcmDeleteColorTransform**](/windows/win32/api/winddi/nf-winddi-drvicmdeletecolortransform)

- [**DrvIcmCheckBitmapBits**](/windows/win32/api/winddi/nf-winddi-drvicmcheckbitmapbits)

GDI calls the [**DrvIcmCreateColorTransform**](/windows/win32/api/winddi/nf-winddi-drvicmcreatecolortransform) function to supply the driver with [ICC profiles](/windows-hardware/drivers/print/installing-icc-profiles) for the print job. Given these profiles, the function can create an internal color transform to use when correcting color information. A color transform is a driver-specific, internally defined mapping from one color space to another. The function returns a handle to the transform, which GDI stores.

Flags within the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) and [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structures indicate whether color management is being performed by the system (or application) or by the driver (or device). Within each driver-implemented graphics DDI drawing function that receives either (or both) of these structures, the flags must be checked. If the system or application is currently handling color management, the driver or device must not. If driver or device color management is enabled, the graphics DDI function must call [**BRUSHOBJ_hGetColorTransform**](/windows/win32/api/winddi/nf-winddi-brushobj_hgetcolortransform) or [**XLATEOBJ_hGetColorTransform**](/windows/win32/api/winddi/nf-winddi-xlateobj_hgetcolortransform) (or both) to obtain a handle to the color transform to be used. The handle will be one that the driver provided in response to a previous call to its [**DrvIcmCreateColorTransform**](/windows/win32/api/winddi/nf-winddi-drvicmcreatecolortransform) function.

## Handling proprietary color management

For some devices, proprietary color management is performed (either by the driver or by hardware) regardless of whether ICM has been enabled. Drivers for such devices must not allow color correction to be performed if the received image data has already been corrected. Precorrected data can be received if:

- An application has color-corrected the image "outside the DC" (see the Microsoft Windows SDK documentation).

- Color management is being handled by the system.

For either of these scenarios, both the BR_HOST_ICM flag in the **flColorType** member of [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) and the XO_HOST_ICM flag in the **flXlate** member of [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) will be set. These flags can be set even if the **dmICMMethod** member of [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) is DMICMMETHOD_NONE.
