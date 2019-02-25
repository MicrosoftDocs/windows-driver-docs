---
title: Adding Print Ticket Support to Monolithic Print Drivers
description: Adding Print Ticket Support to Monolithic Print Drivers
ms.assetid: 82c65b9a-6e7b-4acd-93aa-33d696ddc421
keywords:
- printer interface DLL WDK , Print Ticket support
- monolithic print drivers WDK
- Print Tickets WDK , monolithic print drivers
- IPrintTicketProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Print Ticket Support to Monolithic Print Drivers


For a monolithic print driver to provide Print Ticket support and support the [Print Ticket and Print Capabilities Technologies](print-ticket-and-print-capabilities-technologies.md), it must implement the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375) and also provide the necessary IClassFactory interface support for the COM-style calling methods used by the print driver. At a minimum, the driver must support the methods of the IPrintTicketProvider interface that are called during the OpenPrinter call in the sequence shown below:

1.  [GetSupportedVersions](getsupportedversions.md)

2.  [BindPrinter](bindprinter.md)

3.  [QueryDeviceNamespace](querydevicenamespace.md)

To complete the support for this interface, the print driver must support the rest of the methods of the IPrintTicketProvider interface:

[GetPrintCapabilities](getprintcapabilities.md)

[ConvertDevModeToPrintTicket](convertdevmodetoprintticket2.md)

[ConvertPrintTicketToDevMode](convertprinttickettodevmode.md)

[ValidatePrintTicket](validateprintticket.md)

 

 




