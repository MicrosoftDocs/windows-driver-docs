---
title: Bidirectional Communication
description: Bidirectional Communication
ms.assetid: c88f5f43-4a14-4f63-9f17-b6680fc0d645
keywords:
- printer configuration WDK , bidirectional communication
- bidirectional communication WDK print
- bidi communication WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




