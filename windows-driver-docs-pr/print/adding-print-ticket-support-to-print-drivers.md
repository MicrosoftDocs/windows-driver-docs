---
title: Add Print Ticket Support to Print Drivers
description: Provides information about how to add print ticket support to print drivers.
keywords:
- printer driver customizing WDK , Print Tickets
- customizing printer drivers WDK , Print Tickets
- Print Tickets WDK , adding support for
- IPrintTicketProvider
ms.date: 01/26/2023
---

# Add print ticket support to print drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

To completely support the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md), print drivers must:

- Support the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface, as appropriate, to provide the [Print Capabilities](print-capabilities.md) document for the printer.

- Support the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface in print driver plug-ins.

- Use the [Print Ticket](print-ticket.md) information when processing a print job.

A print driver that supports the **IPrintTicketProvider** interface accomplishes the first two items in the preceding list but does not address the last item. The print driver must read and process the settings of the Print Tickets in an XPS Document so that these settings affect the printed document. For more information about implementing this support, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

GDI-based version 3 print drivers do not need to add Print Ticket support to the drivers because the print subsystem converts PrintTicket objects to equivalent [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structures for the print driver.
