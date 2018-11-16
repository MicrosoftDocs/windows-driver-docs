---
title: Supporting Asynchronous I/O
description: Supporting Asynchronous I/O
ms.assetid: b4baf1a9-6156-4bbf-b4d9-7205924c637f
keywords: ["asynchronous I/O WDK kernel", "I/O WDK kernel , asynchronous mode", "status information WDK I/O requests"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Supporting Asynchronous I/O





The I/O manager provides asynchronous I/O support so that the originator of an I/O request (usually a user-mode application but sometimes another driver) can continue executing, rather than wait for its I/O request to be completed. Asynchronous I/O support improves both the overall system throughput and the performance of any code that makes an I/O request.

With asynchronous I/O support, kernel-mode drivers do not necessarily process I/O requests in the same order in which they were sent to the I/O manager. The I/O manager, or a higher-level driver, can reorder I/O requests as they are received. A driver can split a large data transfer request into smaller transfer requests. Moreover, a driver can overlap I/O request processing, particularly in a symmetric multiprocessor platform, as mentioned in [Multiprocessor-Safe](multiprocessor-safe.md).

Furthermore, a kernel-mode driver's processing of an individual I/O request is not necessarily serialized. That is, a driver does not necessarily process each IRP to completion before it starts processing the next incoming I/O request.

When a driver receives an IRP, it responds by carrying out as much IRP-specific processing as it can. If the driver supports asynchronous IRP processing, it can send an IRP to the next driver, if necessary, and begin processing the next IRP without waiting for the first one to be completed. The driver can register a "completion routine," which the I/O manager calls when another driver has finished processing an IRP. Drivers provide a status value in the IRP's I/O status block, which other drivers can access to determine the status of an I/O request.

Drivers can maintain state information about their current I/O operations in a special part of their device objects, called a [device extension](device-extensions.md).

For more information, see [Handling IRPs](handling-irps.md) and [Input/Output Techniques](i-o-programming-techniques.md).

 

 




