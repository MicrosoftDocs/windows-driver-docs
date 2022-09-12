---
title: Print ticket interfaces and print driver plug-ins
description: Provides information about print ticket interfaces and print driver plug-ins.
keywords:
- IPrintTicketProvider
- IPrintOemPrintTicketProvider
ms.date: 09/07/2022
---

# Print ticket interfaces and print driver plug-ins

This section describes how the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface and the [**IPrintOemPrintTicketProvider**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintoemprintticketprovider) interface work with the Unidrv and PScript5 print drivers and their plug-ins and the context of the application-level functions that call them.

This section discusses the context of the following Microsoft Win32 functions:

[OpenPrinter](openprinter.md)

[ConvertDevModeToPrintTicket](convertdevmodetoprintticket.md)

[ConvertPrintTicketToDevMode](convertprinttickettodevmode.md)

[ValidatePrintTicket](validateprintticket.md)
