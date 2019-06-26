---
title: ConvertDevModeToPrintTicket overview
description: The ConvertDevModeToPrintTicket method is called for each print driver plug-in that was installed.
ms.assetid: 71387d8b-60ce-4deb-a20b-9d7b0b7be230
keywords:
- ConvertDevModeToPrintTicket
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ConvertDevModeToPrintTicket overview


Unidrv and PScript5 print drivers create the Print Ticket by using the elements from the public and private parts of the [**DEVMODEW**](https://docs.microsoft.com/windows/desktop/api/wingdi/ns-wingdi-_devicemodew) structure that the drivers support. The [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff553161(v=vs.85)) method is called for each print driver plug-in that was installed.

The following illustration shows the order of the calls to IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket when the driver call ConvertDevModeToPrintTicket.

![convertdevmodetoprintticket calling sequence](images/ptpcdm2pt-uml.gif)

 

 




