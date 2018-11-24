---
title: Version 3 XPSDrv Print Driver Components
description: Version 3 XPSDrv Print Driver Components
ms.assetid: 7eced017-a6a6-4fa5-8965-ff6655f86b8c
keywords:
- XPSDrv printer drivers WDK , configuration modules
- configuration modules WDK XPSDrv , Version 3 XPS drivers
- Version 3 XPS drivers WDK XPSDrv
- conversion rendering modules WDK XPSDrv
- Version 3 XPS drivers WDK XPSDrv , about Version 3 XPS drivers
- XPSDrv printer drivers WDK , Version 3 XPS drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version 3 XPSDrv Print Driver Components


The Version 3 components of a XPSDrv print driver contain a configuration module and aconversion render module.

The configuration module of an XPSDrv print driver is based on the same architecture as earlier Version 3 print drivers. (Windows Vista also supports Universal print drivers (Unidrv) and PostScript (PScript5) print drivers that are based on generic printer definition (GPD) files and PostScript printer definition (PPD) files, respectively. Windows Vista also supports Unidrv or PScript5 print driver configuration plug-ins and monolithic print driver configuration modules.)

Microsoft Win32 applications print to XPSDrv print drivers by using the existing GDI print support API. The Microsoft-supplied conversion rendering module creates an XPS spool file from the incoming device driver interface (DDI) calls that GDI emits.

The following topics cover XPSDrv configuration issues:

[XPDDrv Driver Options](xpsdrv-driver-options.md)

[XPSDrv Driver Requirements](xpsdrv-driver-requirements.md)

[XPSDrv Driver Recommendations](xpsdrv-driver-recommendations.md)

[XPSDrv Driver Implementation](xpsdrv-driver-implementation.md)

[Unidrv-based or PScript5-based XPSDrv Driver Changes](unidrv-based-or-pscript5-based-xpsdrv-driver-changes.md)

 

 




