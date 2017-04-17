---
title: Bidirectional Communication
author: windows-driver-content
description: Bidirectional Communication
ms.assetid: c88f5f43-4a14-4f63-9f17-b6680fc0d645
keywords: ["printer configuration WDK , bidirectional communication", "bidirectional communication WDK print", "bidi communication WDK print"]
---

# Bidirectional Communication


Bidirectional printer communication (also known as bidi communication) between the print subsystem and the printer is essential for the autoconfiguration of printers. This communication, which is provided with the Windows operating system, beginning with Windows XP, enables drivers and applications to make requests to and get responses from a printer device. With autoconfiguration based on bidirectional communication, users do not have to manually choose installable options because there is a way for applications to configure printers on their own.

Bidi communication support involves two parts:

-   Bidirectional communication interfaces, which consist of spooler APIs

-   Bidirectional communication schema, an XML standard for exchanging information with a device

The schema describes the requests that an application can make to a device and the format for the requests. The spooler APIs send the requests to the device and also send and receive the bidi data. An application can also send a request to a network print provider for a network printer or a printer that is connected to a remote printer server.

For a description of how the print spooler supports bidirectional communication, see [Adding Bidirectional Communication](adding-bidirectional-communication.md) and [Spooler Notification](spooler-notification.md).

## In this section


[Bidirectional Communication Schema](bidirectional-communication-schema.md)

## Related sections


[Bidirectional Communication Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163)

[Bidirectional Communication Schema Reference](https://msdn.microsoft.com/library/windows/hardware/ff545175)

[Bidirectional Communication Error Codes](https://msdn.microsoft.com/library/windows/hardware/dd183367)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Communication%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


