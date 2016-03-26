---
title: I/O Queue Event Callback Functions
description: I/O Queue Event Callback Functions
ms.assetid: 5aa63c47-493d-4583-9eaa-1e50fdc089dd
keywords: ["I/O queues WDK UMDF", "queues WDK UMDF", "callback functions WDK UMDF", "event callback functions WDK UMDF"]
---

# I/O Queue Event Callback Functions


\[This topic applies to UMDF 1.*x*.\]

When drivers create I/O queues, or configure default I/O queues, they can register the following interfaces so that the framework notifies the driver--by calling the methods associated with the interfaces--when events related to the interfaces occur. For more information about I/O queues and creating and configuring I/O queues, see [Framework I/O Queue Object](framework-i-o-queue-object.md).

[IQueueCallbackCreate](https://msdn.microsoft.com/library/windows/hardware/ff556837)

[IQueueCallbackDeviceIoControl](https://msdn.microsoft.com/library/windows/hardware/ff556852)

[IQueueCallbackRead](https://msdn.microsoft.com/library/windows/hardware/ff556872)

[IQueueCallbackWrite](https://msdn.microsoft.com/library/windows/hardware/ff556882)

[IQueueCallbackDefaultIoHandler](https://msdn.microsoft.com/library/windows/hardware/ff556843)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20I/O%20Queue%20Event%20Callback%20Functions%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




