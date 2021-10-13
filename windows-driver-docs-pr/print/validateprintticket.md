---
title: ValidatePrintTicket overview
description: Each plug-in calls the IPrintOemPrintTicketProvider::ValidatePrintTicket method to validate the PrintTicket.
keywords:
- ValidatePrintTicket
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ValidatePrintTicket overview


Unidrv and PScript5 print drivers validate the Print Ticket by using the sequence that the following illustration and list show.

![diagram illustrating how the unidrv and pscript5 print drivers validate the print ticket.](images/ptpcvalpt-uml.gif)

1.  For each plug-in, call the [**IPrintOemPrintTicketProvider::ExpandIntentOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-expandintentoptions) method.

2.  Call the [**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-convertprinttickettodevmode) method.

3.  For each plug-in, call **IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode** to convert the private portions of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure.

4.  Validate public and private parts of the DEVMODEW structure that the Unidrv or PScript5 print driver supports.

5.  For each plug-in, validate the private parts of the DEVMODEW structure.

6.  Call the [**IPrintTicketProvider::ConvertPrintTicketToDevMode**](/previous-versions/windows/hardware/drivers/ff554363(v=vs.85)) method.

7.  For each plug-in, call the [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](/previous-versions/windows/hardware/drivers/ff553161(v=vs.85)) method to convert the private portions of the DEVMODEW structure.

8.  For each plug-in, call the [**IPrintOemPrintTicketProvider::ValidatePrintTicket**](/previous-versions/windows/hardware/drivers/ff553184(v=vs.85)) method to validate the PrintTicket.

 

