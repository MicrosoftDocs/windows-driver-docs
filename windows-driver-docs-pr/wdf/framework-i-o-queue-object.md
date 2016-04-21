---
title: Framework I/O Queue Object
author: windows-driver-content
description: Framework I/O Queue Object
ms.assetid: b343c61a-8252-4e46-9013-bef29d9ec360
keywords: ["UMDF objects WDK , I/O queue objects", "framework objects WDK UMDF , I/O queue objects", "I/O queue objects WDK UMDF", "IWDFIoQueue", "queue objects WDK UMDF"]
---

# Framework I/O Queue Object


\[This topic applies to UMDF 1.*x*.\]

The framework I/O queue object is exposed to drivers by the [IWDFIoQueue](https://msdn.microsoft.com/library/windows/hardware/ff558943) interface. It represents an I/O queue, which is a container for I/O requests. An I/O queue controls the flow of requests into the driver. When an I/O request arrives, it is placed in the appropriate queue. I/O queue objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to create I/O queue objects. In the call to **IWDFDevice::CreateIoQueue**, the driver can specify whether the queue is the default queue.

When the driver creates an I/O queue, it specifies a dispatch model that controls the delivery of requests to the driver. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md).

When drivers create I/O queues, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [I/O Queue Event Callback Functions](i-o-queue-event-callback-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20I/O%20Queue%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




