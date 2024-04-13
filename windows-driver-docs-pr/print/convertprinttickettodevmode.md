---
title: ConvertPrintTicketToDevMode Overview
description: Describes IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method usage from an application's passed print ticket.
keywords:
- ConvertPrintTicketToDevMode
ms.date: 01/27/2023
---

# ConvertPrintTicketToDevMode overview

[!include[Print Support Apps](../includes/print-support-apps.md)]

Unidrv and PScript5 print drivers fill in the public and private parts of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure that they support by using the information from the Print Ticket that was passed in the application's call to ConvertPrintTicketToDevMode. The [**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-convertprinttickettodevmode) method is called for each print driver plug-in that was installed.

The following illustration shows the order of the calls to **IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode** when the driver calls **ConvertPrintTicketToDevMode**.

![diagram illustrating the convertprinttickettodevmode calling sequence.](images/ptpcpt2dm-uml.gif)
