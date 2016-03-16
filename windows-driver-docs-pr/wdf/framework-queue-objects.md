---
title: Framework Queue Objects
description: Framework Queue Objects
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 42736e2d-2482-46b4-bf52-4efe369db40b
keywords: ["I/O requests WDK KMDF queue objects", "I/O queues WDK KMDF", "queue objects WDK KMDF", "I/O queue objects WDK KMDF", "request processing WDK KMDF queue objects", "queues WDK KMDF", "queues WDK KMDF framework objects", "I/O queues WDK KMDF about I/O queues", "callback functions WDK KMDF", "event callback functions WDK KMDF", "framework objects WDK KMDF I/O queue objects"]
---

# Framework Queue Objects


## <a href="" id="ddk-framework-queue-objects-df"></a>


Framework queue objects represent *I/O queues*, which are containers for the I/O requests that a driver receives. Each driver can create one or more I/O queues for each device. The framework queue object defines a set of [event callback functions](https://msdn.microsoft.com/library/windows/hardware/dn265647) that the driver can provide and a set of object methods that the driver can call.

When the framework receives an I/O request that is directed to one of the driver's devices, the framework places the request in the appropriate I/O queue. If your driver registers one or more [request handlers](request-handlers.md), the framework can notify your driver each time an I/O request is available. Alternatively, your driver can poll the I/O queue for requests.

This section includes:

[Creating I/O Queues](creating-i-o-queues.md)

[Deleting I/O Queues](deleting-i-o-queues.md)

[Managing I/O Queues](managing-i-o-queues.md)

[Using Power-Managed I/O Queues](using-power-managed-i-o-queues.md)

[Guaranteeing Forward Progress of I/O Operations](guaranteeing-forward-progress-of-i-o-operations.md)

[I/O Queue States](i-o-queue-states.md)

[Example Uses of I/O Queues](example-uses-of-i-o-queues.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Queue%20Objects%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




