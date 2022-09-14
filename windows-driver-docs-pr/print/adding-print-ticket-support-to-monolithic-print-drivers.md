---
title: Add print ticket support to monolithic print drivers
description: Provides information about how to add print ticket support to monolithic print drivers.
keywords:
- printer interface DLL WDK , Print Ticket support
- monolithic print drivers WDK
- Print Tickets WDK , monolithic print drivers
- IPrintTicketProvider
ms.date: 09/06/2022
---

# Add print ticket support to monolithic print drivers

For a monolithic print driver to provide Print Ticket support and support the [Print Ticket and Print Capabilities Technologies](print-ticket-and-print-capabilities-technologies.md), it must implement the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface and also provide the necessary **IClassFactory** interface support for the COM-style calling methods used by the print driver. At a minimum, the driver must support the methods of the **IPrintTicketProvider** interface that are called during the **OpenPrinter** call in the sequence shown below:

1. [**GetSupportedVersions**](getsupportedversions.md)

1. [**BindPrinter**](bindprinter.md)

1. [**QueryDeviceNamespace**](querydevicenamespace.md)

To complete the support for this interface, the print driver must support the rest of the methods of the **IPrintTicketProvider** interface:

[**GetPrintCapabilities**](getprintcapabilities.md)

[**ConvertDevModeToPrintTicket**](convertdevmodetoprintticket2.md)

[**ConvertPrintTicketToDevMode**](convertprinttickettodevmode.md)

[**ValidatePrintTicket**](validateprintticket.md)
