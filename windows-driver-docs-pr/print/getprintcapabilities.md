---
title: GetPrintCapabilities
description: The IPrintTicketProvider GetPrintCapabilities method must return a valid PrintCapabilities document.
keywords:
- GetPrintCapabilities
ms.date: 09/06/2022
---

# GetPrintCapabilities

The [**IPrintTicketProvider::GetPrintCapabilities**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-getprintcapabilities) method must return a valid **PrintCapabilities** document. For a basic implementation, the document can be very simple however the print driver cannot support any features in a Print Ticket that are not exposed in the **PrintCapabilities** document. As you add print ticket support to your print driver, you will need to return to this routine and add those features to the **PrintCapabilities** document.

The system does not provide any default **PrintCapabilities** document even for the features that the system provides through the DEVMODE-to-PrintTicket conversion. The print driver must create and return the corresponding **PrintCapabilities** document.
