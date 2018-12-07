---
title: Framework I/O Queue Object
description: Framework I/O Queue Object
ms.assetid: b343c61a-8252-4e46-9013-bef29d9ec360
keywords:
- UMDF objects WDK , I/O queue objects
- framework objects WDK UMDF , I/O queue objects
- I/O queue objects WDK UMDF
- IWDFIoQueue
- queue objects WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework I/O Queue Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework I/O queue object is exposed to drivers by the [IWDFIoQueue](https://msdn.microsoft.com/library/windows/hardware/ff558943) interface. It represents an I/O queue, which is a container for I/O requests. An I/O queue controls the flow of requests into the driver. When an I/O request arrives, it is placed in the appropriate queue. I/O queue objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to create I/O queue objects. In the call to **IWDFDevice::CreateIoQueue**, the driver can specify whether the queue is the default queue.

When the driver creates an I/O queue, it specifies a dispatch model that controls the delivery of requests to the driver. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md).

When drivers create I/O queues, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [I/O Queue Event Callback Functions](i-o-queue-event-callback-functions.md).

 

 





