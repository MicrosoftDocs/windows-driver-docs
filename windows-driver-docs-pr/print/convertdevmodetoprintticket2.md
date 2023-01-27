---
title: ConvertDevModeToPrintTicket print ticket support
description: This method is called by the print subsystem to convert the DEVMODEW structure to a PrintTicket object.
ms.date: 01/27/2023
---

# ConvertDevModeToPrintTicket print ticket support

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [**IPrintTicketProvider::ConvertDevModeToPrintTicket**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-convertdevmodetoprintticket) method is called by the print subsystem to convert the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure to a PrintTicket object.
