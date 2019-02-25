---
title: SerCx2 Handling of Read and Write Requests
description: A peripheral driver sends write (IRP_MJ_WRITE) and read (IRP_MJ_READ) requests to a port on a serial controller to transfer data to and from a peripheral device that is connected to the port.
ms.assetid: 98100680-7D27-42B7-A445-C539B2DF95AD
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




