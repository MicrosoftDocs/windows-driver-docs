---
title: SerCx2 Handling of Read and Write Requests
author: windows-driver-content
description: A peripheral driver sends write (IRP\_MJ\_WRITE) and read (IRP\_MJ\_READ) requests to a port on a serial controller to transfer data to and from a peripheral device that is connected to the port.
ms.assetid: 98100680-7D27-42B7-A445-C539B2DF95AD
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SerCx2 Handling of Read and Write Requests


A peripheral driver sends write ([**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904)) and read ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883)) requests to a port on a serial controller to transfer data to and from a peripheral device that is connected to the port. The way in which SerCx2 handles these requests is well-defined, even when the requests time out or are canceled.

## Cancellation of a read or write request


Before a read or write request can complete, this request might be canceled by the operating system or by the peripheral driver that sent the request. If cancellation occurs before SerCx2 transfers any data for the request, SerCx2 completes the request with the STATUS\_CANCELLED status code.

However, if the read or write request is canceled after one or more bytes of data are transferred for the request, but before all the data for the request is transferred, SerCx2 completes the request with the STATUS\_SUCCESS status code. The completed request reports the number of bytes read or written by SerCx2 during the handling of the request. If necessary, the peripheral driver that sent the request can use this information to send a second request to finish the partially completed read or write operation.

## Requests that time out


If a read or write request can time out if the request takes too long to process. Also, a read request can time out if the time between two successive bytes received by the serial controller exceeds some maximum allowed time. In either case, when the time-out condition is detected, SerCx2 immediately completes the request with the STATUS\_TIMEOUT status code. The completed request reports the number of bytes read or written by SerCx2 during the handling of the request. If necessary, the peripheral driver that sent the request can use this information to send a second request to finish the partially completed read or write operation. For more information about time-outs, see [**SERIAL\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/hh439614).

## Impact of hardware limitations


Typically, SerCx2 accurately reports the number of bytes transferred by a read or write request that times out or is canceled. However, some hardware used to perform system DMA transactions might not accurately count the number of bytes transferred by a partially completed read or write transaction. If so, the associated read or write request might report only an approximate count of the bytes transferred.

## Requests to transfer zero bytes


In response to a read or write request to transfer zero bytes, SerCx2 completes the request with a STATUS\_SUCCESS status code but performs no operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20SerCx2%20Handling%20of%20Read%20and%20Write%20Requests%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


