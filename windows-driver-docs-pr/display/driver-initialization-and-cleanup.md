---
title: Driver Initialization and Cleanup
description: Driver Initialization and Cleanup
keywords:
- drawing WDK GDI , initialization, description
- initializing graphics drivers WDK Windows 2000 display , description
- GDI WDK Windows 2000 display , initialization, description
- graphics drivers WDK Windows 2000 display , initialization, description
- DrvEnableDriver
- drawing WDK GDI , cleanup
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Initialization and Cleanup

While the device driver may implement several or many functions, it exports only [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) to GDI. The driver exposes its other supported functions through a function table. The first call GDI makes to a device driver is to the **DrvEnableDriver** function. Within this function, the driver fills in the passed-in [**DRVENABLEDATA**](/windows/win32/api/winddi/ns-winddi-drvenabledata) structure so that GDI can determine which other *DrvXxx* functions are supported and where they are located. The driver supplies the following information in DRVENABLEDATA:

* The **iDriverVersion** member contains the graphics DDI version number for a particular Windows operating system version. The *winddi.h* header defines the following constants:

   | Constant | Operating System Version |
   | -------- | ------------------------ |
   | DDI_DRIVER_VERSION_NT4 | Windows NT 4.0 |
   | DDI_DRIVER_VERSION_NT5 | Windows 2000 |
   | DDI_DRIVER_VERSION_NT5_01 | Windows XP |

   For more information about how these constants are used, see [**DRVENABLEDATA**](/windows/win32/api/winddi/ns-winddi-drvenabledata).

* The **c** member contains the number of DRVFN structures in the array.

* The **pdrvfn** member points to an array of [**DRVFN**](/windows/win32/api/winddi/ns-winddi-drvfn) structures that lists the supported functions and their indexes.

For GDI to call a function other than the driver's enable and disable functions, the driver must make the function's name and location available to GDI.

While [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) can also perform one-time initializations, such as the allocation of semaphores, a driver should not actually enable the hardware during **DrvEnableDriver**. Hardware initialization should occur in a driver's [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function. Likewise, a driver should enable the surface in the [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) function.

GDI calls the [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver) function to notify the driver that it is about to be unloaded. In response to this call, the driver should free all resources and memory still allocated by the driver at this point.

If the hardware needs to be reset, GDI calls the driver's [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) function.
