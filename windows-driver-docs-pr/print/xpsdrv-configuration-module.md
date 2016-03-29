---
title: XPSDrv Configuration Module
description: XPSDrv Configuration Module
ms.assetid: 439d7769-57d1-41f9-a3db-da254b4b7cae
keywords: ["XPSDrv printer drivers WDK , configuration modules", "configuration modules WDK XPSDrv , about configuration modules", "conversion render modules WDK XPSDrv", "notifications WDK XPSDrv", "event notifications WDK XPSDrv"]
---

# XPSDrv Configuration Module


The XPSDrv print driver is the component of the XPS print path that consumes an XPS spool file and emits page description language (PDL) data that a printer can consume. The configuration module contains the driver components that communicate printer features and settings to applications. XPSDrv printer drivers support the communications methods that Microsoft Win32-based applications and Windows Presentation Foundation (WPF)-based applications use.

Both Win32-based applications and WPF applications can print to XPSDrv print drivers. Win32 applications use the GDI printing application programming interface (API), and the Microsoft-supplied conversion render module creates an XPS spool file for printing to the print filter pipeline. WPF applications use the WPF printing API to create an XPS spool file directly from the application.

The following diagram shows the XPSDrv configuration architecture.

![diagram illustrating the xpsdrv configuration architecture](images/xpsconfig.png)

Note that the three objects in the Configuration Module section are mutually exclusive.

The two main components of an XPSDrv print driver are the [Version 3 print driver modules](version-3-xpsdrv-print-driver-components.md) and the [XPS filter pipeline](filter-pipeline-configuration-file.md). Each of these components requires one or more configuration files and modules.

### XPSDrv Document Events

XPSDrv drivers can receive GDI document events through the [**DrvDocumentEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548544) function when Win32-based applications are printing to them, and the drivers can receive XPS document events through DrvDocumentEvent when WPF applications are printing to them. For more information about XPSDrv document events, see [XPSDrv Driver Document Events](xps-driver-document-events.md).

### XPSDrv Driver Installation

XPSDrv drivers have specific requirements for installation. For more information about XPSDrv driver installation, see [XPSDrv Installation](xpsdrv-installation.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Configuration%20Module%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




