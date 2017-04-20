---
title: Version 3 XPSDrv Print Driver Components
author: windows-driver-content
description: Version 3 XPSDrv Print Driver Components
ms.assetid: 7eced017-a6a6-4fa5-8965-ff6655f86b8c
keywords:
- XPSDrv printer drivers WDK , configuration modules
- configuration modules WDK XPSDrv , Version 3 XPS drivers
- Version 3 XPS drivers WDK XPSDrv
- conversion rendering modules WDK XPSDrv
- Version 3 XPS drivers WDK XPSDrv , about Version 3 XPS drivers
- XPSDrv printer drivers WDK , Version 3 XPS drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Version%203%20XPSDrv%20Print%20Driver%20Components%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


