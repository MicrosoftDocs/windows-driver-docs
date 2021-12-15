---
title: Adding Print Ticket Support to Print Drivers
description: Adding Print Ticket Support to Print Drivers
keywords:
- printer driver customizing WDK , Print Tickets
- customizing printer drivers WDK , Print Tickets
- Print Tickets WDK , adding support for
- IPrintTicketProvider
ms.date: 04/20/2017
---

# Adding Print Ticket Support to Print Drivers


To completely support the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md), print drivers must:

-   Support the [IPrintTicketProvider interface](/previous-versions/windows/hardware/drivers/ff554375(v=vs.85)), as appropriate, to provide the [Print Capabilities](print-capabilities.md) document for the printer.

-   Support the [IPrintOemPrintTicketProvider interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintoemprintticketprovider) in print driver plug-ins.

-   Use the [Print Ticket](print-ticket.md) information when processing a print job.

A print driver that supports the IPrintTicketProvider interface accomplishes the first two items in the preceding list but does not address the last item. The print driver must read and process the settings of the Print Tickets in an XPS Document so that these settings affect the printed document. For more information about implementing this support, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

**Note**   GDI-based, version 3 print drivers do not need to add Print Ticket support to the drivers because the print subsystem converts PrintTicket objects to equivalent [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structures for the print driver.

 

 

