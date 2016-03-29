---
title: Adding Print Ticket Support to Print Drivers
description: Adding Print Ticket Support to Print Drivers
ms.assetid: ef4db930-2b4c-40b9-b1f4-85767b7f6855
keywords: ["printer driver customizing WDK , Print Tickets", "customizing printer drivers WDK , Print Tickets", "Print Tickets WDK , adding support for", "IPrintTicketProvider"]
---

# Adding Print Ticket Support to Print Drivers


To completely support the [Print Ticket and Print Capabilities technologies](print-ticket-and-print-capabilities-technologies.md), print drivers must:

-   Support the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375), as appropriate, to provide the [Print Capabilities](print-capabilities.md) document for the printer.

-   Support the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174) in print driver plug-ins.

-   Use the [Print Ticket](print-ticket.md) information when processing a print job.

A print driver that supports the IPrintTicketProvider interface accomplishes the first two items in the preceding list but does not address the last item. The print driver must read and process the settings of the Print Tickets in an XPS Document so that these settings affect the printed document. For more information about implementing this support, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

**Note**   GDI-based, version 3 print drivers do not need to add Print Ticket support to the drivers because the print subsystem converts PrintTicket objects to equivalent [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structures for the print driver.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Adding%20Print%20Ticket%20Support%20to%20Print%20Drivers%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




