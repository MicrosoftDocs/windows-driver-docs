---
title: Print Ticket Interfaces and Print Driver Plug-ins
author: windows-driver-content
description: Print Ticket Interfaces and Print Driver Plug-ins
ms.assetid: 5c5237a1-f4ff-42f9-8992-753743fd5e15
keywords:
- IPrintTicketProvider
- IPrintOemPrintTicketProvider
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Ticket Interfaces and Print Driver Plug-ins


This section describes how the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375) and the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174) work with the Unidrv and PScript5 print drivers and their plug-ins and the context of the application-level functions that call them.

This section discusses the context of the following Microsoft Win32 functions:

[OpenPrinter](openprinter.md)

[ConvertDevModeToPrintTicket](convertdevmodetoprintticket.md)

[ConvertPrintTicketToDevMode](convertprinttickettodevmode.md)

[ValidatePrintTicket](validateprintticket.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20Interfaces%20and%20Print%20Driver%20Plug-ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


