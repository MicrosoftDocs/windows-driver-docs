---
title: Print Ticket Processing in the Print Driver
description: Print Ticket Processing in the Print Driver
ms.assetid: a7295632-0133-4133-b62e-5526dcc12c7d
keywords:
- Print Tickets WDK , print driver processing
- Print Tickets WDK , XPSDrv
- Print Tickets WDK , GDI-based print drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Ticket Processing in the Print Driver


The validated settings in a PrintTicket object are used to configure the print processing that the XPSDrv print driver performs. The components of the print driver, therefore, must read and interpret the settings in the Print Tickets before the driver performs any processing so the driver can process the document according to these settings.

XPSDrv print drivers perform this processing in the print processing filters of the print driver.

GDI-based print drivers continue to use the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure for the settings because of the compatibility support that is built into the Windows Vista print subsystem. For more information about this support, see [Print Ticket Compatibility with Win 32 Applications](print-ticket-compatibility-with-win-32-applications.md).

For more information about implementing Print Ticket processing in the print driver, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

 

 




