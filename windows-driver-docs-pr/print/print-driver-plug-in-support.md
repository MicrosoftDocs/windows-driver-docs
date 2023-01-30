---
title: Print Driver Plug-in Support
description: Print Driver Plug-in Support
keywords:
- Print Capabilities WDK , plug-ins
- IPrintOemPrintTicketProvider
ms.date: 01/30/2023
---

# Print Driver Plug-in Support

[!include[Print Support Apps](../includes/print-support-apps.md)]

Print driver plug-ins that provide additional or modified functionality to minidriver-based print drivers must support the [IPrintOemPrintTicketProvider interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintoemprintticketprovider) to provide complete and correct Print Capabilities support in a Unidrv or PScript5-based print driver. If a plug-in supports **IPrintOemPrintTicketProvider**, the plug-in will gain the ability to edit the PrintTicket document and modify the configuration user interface (UI). But support for this interface also requires considerably more development effort than just editing a GPD or PPD file.

Plug-ins that do not support the **IPrintOemPrintTicketProvider** interface are limited to their existing [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) support, so some functions that the plug-in provides might not be included in the PrintTicket or PrintCapabilities documents.
