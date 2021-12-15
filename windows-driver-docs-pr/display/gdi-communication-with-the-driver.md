---
title: GDI Communication with the Driver
description: GDI Communication with the Driver
keywords:
- GDI WDK Windows 2000 display , driver communication
- graphics drivers WDK Windows 2000 display , driver communication
- drawing WDK GDI , driver communication
ms.date: 04/20/2017
---

# GDI Communication with the Driver


## <span id="ddk_gdi_communication_with_the_driver_gg"></span><span id="DDK_GDI_COMMUNICATION_WITH_THE_DRIVER_GG"></span>


The driver exports only one function to GDI: [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver). All other driver-supported functions, including the [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver) function, are exposed to GDI through an array of pointers. A GDI call to **DrvEnableDriver** initializes the driver and passes back the list of driver-supported graphics DDI functions. While there are some functions a driver must support, GDI will handle those operations not included in the function list received from the driver's **DrvEnableDriver** routine. GDI calls *DrvDisableDriver* when the driver is to be unloaded. Graphics DDI functions are discussed in depth in [Using the Graphics DDI](using-the-graphics-ddi.md).

GDI makes a large number of objects and services available to the driver. These fall into two categories: user objects and service routines.

 

