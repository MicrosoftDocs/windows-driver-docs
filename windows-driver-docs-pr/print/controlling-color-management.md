---
title: Controlling Color Management
description: Color management for a printer can be controlled by an application, the system (GDI), the driver, or device hardware.
keywords:
- color management WDK print , controlling
ms.date: 01/27/2023
---

# Controlling Color Management

[!include[Print Support Apps](../includes/print-support-apps.md)]

Color management for a printer can be controlled by an application, the system (GDI), the driver, or device hardware. The driver determines which component is managing color correction by examining flags within the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) and [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structures that are passed to its implementations of graphics DDI drawing functions. The following flags are defined:

| Flag | Definition |
|---|---|
| BR_DEVICE_ICM in BRUSHOBJ<br><br>XO_DEVICE_ICM in XLATEOBJ | Color management is being performed by the driver or the device. |
| BR_HOST_ICM in BRUSHOBJ<br><br>XO_HOST_ICM in XLATEOBJ | Color management is being performed by the application or the system (GDI). |

The following topics describe driver support for these color management scenarios:

[System Control](system-control.md)

[Driver Control and Device Control](driver-control-and-device-control.md)

[Supporting CMYK Color Space](supporting-cmyk-color-space.md)

[Color Management of JPEG and PNG Images](color-management-of-jpeg-and-png-images.md)
