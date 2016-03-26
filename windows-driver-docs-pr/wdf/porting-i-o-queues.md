---
title: Porting I/O Queues
description: Porting I/O Queues
ms.assetid: 90319342-5FAB-451B-BCA1-B273B81418DB
---

# Porting I/O Queues


WDF drivers create queues and register I/O event callbacks in the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback. By default, each I/O queue object is the child of a device object. The WDF driver can configure the following tasks for each queue:

-   Which I/O request types are directed to the queue.
-   Whether requests are dispatched in parallel (as soon as they arrive), sequentially (one at a time), or manually (upon driver request).
-   Whether I/O event callback routines are called concurrently or serially.
-   Whether the framework or the driver manages the queue through system and device power transitions.

For more information about creating queues, see [Creating I/O Queues](creating-i-o-queues.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20I/O%20Queues%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




