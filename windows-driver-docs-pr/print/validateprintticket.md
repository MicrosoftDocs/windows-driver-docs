---
title: ValidatePrintTicket overview
description: Each plug-in calls the IPrintOemPrintTicketProvider::ValidatePrintTicket method to validate the PrintTicket.
keywords:
- ValidatePrintTicket
ms.date: 09/07/2022
---

# ValidatePrintTicket overview

Unidrv and PScript5 print drivers validate the PrintTicket by using the sequence that the following illustration and list show.

![diagram illustrating how the unidrv and pscript5 print drivers validate the print ticket.](images/ptpcvalpt-uml.gif)

1. For each plug-in, call the [**IPrintOemPrintTicketProvider::ExpandIntentOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-expandintentoptions) method.

1. Call the [**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-convertprinttickettodevmode) method.

1. For each plug-in, call **IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode** to convert the private portions of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure.

1. Validate public and private parts of the **DEVMODEW** structure that the Unidrv or PScript5 print driver supports.

1. For each plug-in, validate the private parts of the **DEVMODEW** structure.

1. Call the [**IPrintTicketProvider::ConvertPrintTicketToDevMode**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-convertprinttickettodevmode) method.

1. For each plug-in, call the [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-convertdevmodetoprintticket) method to convert the private portions of the DEVMODEW structure.

1. For each plug-in, call the [**IPrintOemPrintTicketProvider::ValidatePrintTicket**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-validateprintticket) method to validate the PrintTicket.
