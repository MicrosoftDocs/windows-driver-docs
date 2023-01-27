---
title: Functions defined by printer graphics DLLs
description: Provides information about functions defined by printer graphics DLLs.
keywords:
- printer graphics DLL WDK, functions
- functions WDK printer graphics DLL
- graphics DLL WDK printer, functions
ms.date: 01/27/2023
---

# Functions defined by printer graphics DLLs

[!include[Print Support Apps](../includes/print-support-apps.md)]

Like all graphics drivers, printer graphics DLLs are responsible for defining the following graphics DDI functions. Following [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver), the initial driver entry point, the remaining functions are listed in alphabetical order. Note that because GDI calls **DrvEnableDriver** by name, its name appears in bold. GDI calls all other display driver functions by way of an array of function pointers that **DrvEnableDriver** returns.

| Function name | Description |
|---|---|
| [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) | Allows the driver to initialize itself and return pointers to supported graphics DDI functions. |
| [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) | Provides the driver with a GDI handle to a device instance. |
| [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver) | (Optional) Allows the driver to perform cleanup operations before being unloaded. |
| [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev) | Allows the driver to remove device instance-specific information. |
| [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface) | Allows the driver to remove a drawing surface. |
| [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) | Allows the driver to provide GDI with physical device characteristics and to initialize device instance-specific information. |
| [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) | Allows the driver to create a drawing surface. |
| [**DrvQueryDeviceSupport**](/windows/win32/api/winddi/nf-winddi-drvquerydevicesupport) | (Optional) Returns requested device-specific information. |
| [**DrvQueryDriverInfo**](/windows/win32/api/winddi/nf-winddi-drvquerydriverinfo) | (Optional) Returns requested driver-specific information. |

Printer graphics DLLs are also responsible for defining the following print-specific graphics DDI functions, which are called at certain points during the rendering of a print job.

| Function | When called |
|--|--|
| [**DrvEndDoc**](/windows/win32/api/winddi/nf-winddi-drvenddoc) | When GDI has finished sending a document to the driver for rendering. |
| [**DrvNextBand**](/windows/win32/api/winddi/nf-winddi-drvnextband) | (Optional) When GDI has finished drawing a band for a physical page, so the driver can send the band to the printer. |
| [**DrvQueryPerBandInfo**](/windows/win32/api/winddi/nf-winddi-drvqueryperbandinfo) | (Optional) Before GDI begins drawing a band for a physical page, so the driver can supply GDI with band-specific information. |
| [**DrvSendPage**](/windows/win32/api/winddi/nf-winddi-drvsendpage) | When GDI has finished drawing a physical page, so the driver can send the page to the printer. |
| [**DrvStartBanding**](/windows/win32/api/winddi/nf-winddi-drvstartbanding) | (Optional) When GDI is ready to start sending bands of a physical page to the driver for rendering. |
| [**DrvStartDoc**](/windows/win32/api/winddi/nf-winddi-drvstartdoc) | When GDI is ready to start sending a document to the driver for rendering. |
| [**DrvStartPage**](/windows/win32/api/winddi/nf-winddi-drvstartpage) | When GDI is ready to start sending a document page to the driver for rendering. |

Typically, a printer graphics DLL also defines whatever additional graphics DDI functions are necessary to accomplish print job rendering. The number and type of functions defined depends on:

- Whether the driver supports use of GDI-managed or device-managed drawing surfaces (or both). For more information, see [Surface Types](../display/surface-types.md).

- The extent to which drawing operations can be handled by GDI instead of being performed by the driver itself. For more information, see [Using the Graphics DDI](../display/using-the-graphics-ddi.md).

All functions defined by printer graphics DLLs are called by GDI's kernel-mode graphics rendering engine (GRE).

The [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) and [**DrvQueryDriverInfo**](/windows/win32/api/winddi/nf-winddi-drvquerydriverinfo) functions are exported by the graphics DLL. The addresses of all other supported graphics DDI functions are placed in a table that is returned by the **DrvEnableDriver** function.
