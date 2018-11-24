---
title: I/O Queue Event Callback Functions
description: I/O Queue Event Callback Functions
ms.assetid: 5aa63c47-493d-4583-9eaa-1e50fdc089dd
keywords:
- I/O queues WDK UMDF
- queues WDK UMDF
- callback functions WDK UMDF
- event callback functions WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Queue Event Callback Functions


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When drivers create I/O queues, or configure default I/O queues, they can register the following interfaces so that the framework notifies the driver--by calling the methods associated with the interfaces--when events related to the interfaces occur. For more information about I/O queues and creating and configuring I/O queues, see [Framework I/O Queue Object](framework-i-o-queue-object.md).

[IQueueCallbackCreate](https://msdn.microsoft.com/library/windows/hardware/ff556837)

[IQueueCallbackDeviceIoControl](https://msdn.microsoft.com/library/windows/hardware/ff556852)

[IQueueCallbackRead](https://msdn.microsoft.com/library/windows/hardware/ff556872)

[IQueueCallbackWrite](https://msdn.microsoft.com/library/windows/hardware/ff556882)

[IQueueCallbackDefaultIoHandler](https://msdn.microsoft.com/library/windows/hardware/ff556843)

 

 





