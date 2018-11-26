---
title: GetPrintCapabilities
description: The IPrintTicketProvider GetPrintCapabilities routine must return a valid PrintCapabilities document.
ms.assetid: 9c9bd387-5ea2-4758-a967-190a711cd8c3
keywords:
- GetPrintCapabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GetPrintCapabilities


The [**IPrintTicketProvider::GetPrintCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554365) routine must return a valid PrintCapabilities document. For a basic implementation, the document can be very simple however the print driver cannot support any features in a Print Ticket that are not exposed in the PrintCapabilities document. As you add print ticket support to your print driver, you will need to return to this routine and add those features to the PrintCapabilities document.

The system does not provide any default PrintCapabilities document even for the features that the system provides through the DEVMODE-to-PrintTicket conversion. The print driver must create and return the corresponding PrintCapabilities document.

 

 




