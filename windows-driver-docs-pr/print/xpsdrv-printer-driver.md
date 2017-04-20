---
title: XPS Printer Driver (XPSDrv)
author: windows-driver-content
description: XPSDrv is an enhanced, GDI-based Version 3 printer driver that was used prior to Windows Vista.
ms.assetid: 7567c514-3034-4db0-9622-31d14eb3772e
keywords: ["printer drivers WDK , XPSDrv printer drivers", "XPSDrv printer drivers WDK", "XPSDrv printer drivers WDK , about XPSDrv printer drivers", "configuration modules WDK XPSDrv", "render modules WDK XPSDrv"]
---

# XPS Printer Driver (XPSDrv)


The XPS printer driver (XPSDrv) is an enhanced, GDI-based Version 3 printer driver that was used prior to Windows Vista. XPSDrv printer drivers (like the GDI-based ones) consist of three main components.

These are the three main components of XPSDrv printer drivers:

-   [XPSDrv Render Module](xpsdrv-render-module.md)

-   [XPSDrv Configuration Module](xpsdrv-configuration-module.md)

-   [XPSDrv Installation](xpsdrv-installation.md)

The configuration module of an XPSDrv printer driver provides the same functions as the configuration module of the [Printer Interface DLL](printer-interface-dll.md) of a GDI-based driver, but the XPSDrv configuration module also supports the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md).

The render module of an XPSDrv printer driver does not, necessarily, use the GDI-based rendering functions of a GDI-based printer driver. Instead, the render module of an XPSDrv printer driver consists of zero or more filters and a configuration file that describes the actions of each filter. The filters in the rendering module of an XPSDrv printer driver must also support the Print Ticket technology to correctly process the print job for the printer.

For more information about installing XPSDrv drivers, see [XPSDrv Installation](xpsdrv-installation.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPS%20Printer%20Driver%20%28XPSDrv%29%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


