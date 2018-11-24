---
title: Print Driver Plug-in Support
description: Print Driver Plug-in Support
ms.assetid: fa072fc9-66da-46c2-a270-6f604860aaff
keywords:
- Print Capabilities WDK , plug-ins
- IPrintOemPrintTicketProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Driver Plug-in Support


Print driver plug-ins that provide additional or modified functionality to minidriver-based print drivers must support the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174) to provide complete and correct Print Capabilities support in a Unidrv or PScript5-based print driver. If a plug-in supports **IPrintOemPrintTicketProvider**, the plug-in will gain the ability to edit the PrintTicket document and modify the configuration user interface (UI). But support for this interface also requires considerably more development effort than just editing a GPD or PPD file.

Plug-ins that do not support the **IPrintOemPrintTicketProvider** interface are limited to their existing [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) support, so some functions that the plug-in provides might not be included in the PrintTicket or PrintCapabilities documents.

 

 




