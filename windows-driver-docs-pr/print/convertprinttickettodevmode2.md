---
title: ConvertPrintTicketToDevMode print ticket support
description: This method is called by the print subsystem to convert the PrintTicket object to a DEVMODEW structure.
ms.date: 01/27/2023
---

# ConvertPrintTicketToDevMode print ticket support

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [**IPrintTicketProvider::ConvertPrintTicketToDevMode**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-convertprinttickettodevmode) method is called by the print subsystem to convert the PrintTicket object to a [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure.
