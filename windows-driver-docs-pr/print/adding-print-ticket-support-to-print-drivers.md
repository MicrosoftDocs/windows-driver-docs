---
title: Adding Print Ticket Support to Print Drivers
description: Adding Print Ticket Support to Print Drivers
ms.assetid: ef4db930-2b4c-40b9-b1f4-85767b7f6855
keywords:
- printer driver customizing WDK , Print Tickets
- customizing printer drivers WDK , Print Tickets
- Print Tickets WDK , adding support for
- IPrintTicketProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Print Ticket Support to Print Drivers


To completely support the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md), print drivers must:

-   Support the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375), as appropriate, to provide the [Print Capabilities](print-capabilities.md) document for the printer.

-   Support the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174) in print driver plug-ins.

-   Use the [Print Ticket](print-ticket.md) information when processing a print job.

A print driver that supports the IPrintTicketProvider interface accomplishes the first two items in the preceding list but does not address the last item. The print driver must read and process the settings of the Print Tickets in an XPS Document so that these settings affect the printed document. For more information about implementing this support, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

**Note**   GDI-based, version 3 print drivers do not need to add Print Ticket support to the drivers because the print subsystem converts PrintTicket objects to equivalent [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structures for the print driver.

 

 

 




