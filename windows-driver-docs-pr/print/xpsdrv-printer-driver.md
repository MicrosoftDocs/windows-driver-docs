---
title: XPS Printer Driver (XPSDrv)
description: Learn about the XPS printer driver, which is an enhanced, GDI-based Version 3 printer driver that was used before Windows Vista.
keywords:
- printer drivers WDK , XPSDrv printer drivers
- XPSDrv printer drivers WDK
- XPSDrv printer drivers WDK , about XPSDrv printer drivers
- configuration modules WDK XPSDrv
- render modules WDK XPSDrv
ms.date: 10/30/2025
ms.topic: concept-article
#customer intent: As a hardware developer, I want to understand the XPS printer driver to support legacy systems.
---

# XPS Printer Driver (XPSDrv)

[!include[Print Support Apps](../includes/print-support-apps.md)]

The XPS printer driver (XPSDrv) is an enhanced, GDI-based Version 3 printer driver that was used before Windows Vista. XPSDrv printer drivers, like the GDI-based ones, consist of three main components:

- [XPSDrv Render Module](xpsdrv-render-module.md)
- [XPSDrv Configuration Module](xpsdrv-configuration-module.md)
- [XPSDrv Installation](xpsdrv-installation.md)

The configuration module of an XPSDrv printer driver provides the same functions as the configuration module of the [Printer Interface DLL](introduction-to-printer-interface-dlls.md) of a GDI-based driver. The XPSDrv configuration module also supports the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md).

The render module of an XPSDrv printer driver doesn't, necessarily, use the GDI-based rendering functions of a GDI-based printer driver. Instead, the render module of an XPSDrv printer driver consists of zero or more filters and a configuration file that describes the actions of each filter. The filters in the rendering module of an XPSDrv printer driver must also support the Print Ticket technology to correctly process the print job for the printer.

## Related content

- [XPSDrv Installation](xpsdrv-installation.md)
