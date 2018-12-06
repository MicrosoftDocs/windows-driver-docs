---
title: XPS Printer Driver (XPSDrv)
description: XPSDrv is an enhanced, GDI-based Version 3 printer driver that was used prior to Windows Vista.
ms.assetid: 7567c514-3034-4db0-9622-31d14eb3772e
keywords:
- printer drivers WDK , XPSDrv printer drivers
- XPSDrv printer drivers WDK
- XPSDrv printer drivers WDK , about XPSDrv printer drivers
- configuration modules WDK XPSDrv
- render modules WDK XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




