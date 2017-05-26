---
title: Adding Print Ticket Support to Monolithic Print Drivers
author: windows-driver-content
description: Adding Print Ticket Support to Monolithic Print Drivers
ms.assetid: 82c65b9a-6e7b-4acd-93aa-33d696ddc421
keywords:
- printer interface DLL WDK , Print Ticket support
- monolithic print drivers WDK
- Print Tickets WDK , monolithic print drivers
- IPrintTicketProvider
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding Print Ticket Support to Monolithic Print Drivers


For a monolithic print driver to provide Print Ticket support and support the [Print Ticket and Print Capabilities Technologies](print-ticket-and-print-capabilities-technologies.md), it must implement the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375) and also provide the necessary IClassFactory interface support for the COM-style calling methods used by the print driver. At a minimum, the driver must support the methods of the IPrintTicketProvider interface that are called during the OpenPrinter call in the sequence shown below:

1.  [GetSupportedVersions](getsupportedversions.md)

2.  [BindPrinter](bindprinter.md)

3.  [QueryDeviceNamespace](querydevicenamespace.md)

To complete the support for this interface, the print driver must support the rest of the methods of the IPrintTicketProvider interface:

[GetPrintCapabilities](getprintcapabilities.md)

[ConvertDevModeToPrintTicket](convertdevmodetoprintticket2.md)

[ConvertPrintTicketToDevMode](convertprinttickettodevmode.md)

[ValidatePrintTicket](validateprintticket.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Adding%20Print%20Ticket%20Support%20to%20Monolithic%20Print%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


